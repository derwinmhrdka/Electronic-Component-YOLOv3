from PyQt5.QtCore import QThread, QTime, QMutexLocker, QMutex, pyqtSignal, qDebug
from PyQt5.QtWidgets import QMessageBox
import cv2
from queue import Queue
import os

from Structures import *
from Config import *


class CaptureThread(QThread):
    updateStatisticsInGUI = pyqtSignal(ThreadStatisticsData)
    end = pyqtSignal()

    def __init__(self, sharedImageBuffer, deviceUrl, dropFrameIfBufferFull, apiPreference, width, height, parent=None):
        super(CaptureThread, self).__init__(parent)
        self.cap = cv2.VideoCapture()
        self.t = QTime()
        self.doStopMutex = QMutex()
        self.fps = Queue()
        self.sharedImageBuffer = sharedImageBuffer
        self.dropFrameIfBufferFull = dropFrameIfBufferFull
        self.deviceUrl = deviceUrl
        self._deviceUrl = int(deviceUrl) if deviceUrl.isdigit() else deviceUrl
        self.localVideo = True if os.path.exists(self._deviceUrl) else False
        self.apiPreference = apiPreference
        self.width = width
        self.height = height
        self.captureTime = 0
        self.doStop = False
        self.sampleNumber = 0
        self.fpsSum = 0.0
        self.statsData = ThreadStatisticsData()
        self.defaultTime = 0

    def run(self):
        pause = False
        while True:
            self.doStopMutex.lock()
            if self.doStop:
                self.doStop = False
                self.doStopMutex.unlock()
                break
            self.doStopMutex.unlock()

            self.sharedImageBuffer.sync(self.deviceUrl)

            if not self.cap.grab():
                if pause or not self.localVideo:
                    continue
                pause = True
                self.end.emit()
                continue

            _, self.grabbedFrame = self.cap.retrieve()
            self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl).add(self.grabbedFrame, self.dropFrameIfBufferFull)

            self.statsData.nFramesProcessed += 1
            self.updateStatisticsInGUI.emit(self.statsData)

            delta = self.defaultTime - self.t.elapsed()
            if delta > 0:
                self.msleep(delta)
            self.captureTime = self.t.elapsed()

            self.updateFPS(self.captureTime)

            self.t.start()

        qDebug("Menghentikan tangkapan citra...")

    def stop(self):
        with QMutexLocker(self.doStopMutex):
            self.doStop = True

    def connectToCamera(self):
        camOpenResult = self.cap.open(self._deviceUrl, self.apiPreference)
        if self.width != -1:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        if self.height != -1:
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        if camOpenResult:
            try:
                self.defaultTime = int(1000 / self.cap.get(cv2.CAP_PROP_FPS))
            except:
                self.defaultTime = 40
        return camOpenResult

    def disconnectCamera(self):
        if self.cap.isOpened():
            self.cap.release()
            return True
        else:
            return False

    def isCameraConnected(self):
        return self.cap.isOpened()

    def getInputSourceWidth(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    def getInputSourceHeight(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def updateFPS(self, timeElapsed):
        if timeElapsed > 0:
            self.fps.put(1000 / timeElapsed)
            self.sampleNumber += 1

        if self.fps.qsize() > CAPTURE_FPS_STAT_QUEUE_LENGTH:
            self.fps.get()
        if self.fps.qsize() == CAPTURE_FPS_STAT_QUEUE_LENGTH and self.sampleNumber == CAPTURE_FPS_STAT_QUEUE_LENGTH:
            while not self.fps.empty():
                self.fpsSum += self.fps.get()
            self.statsData.averageFPS = self.fpsSum / CAPTURE_FPS_STAT_QUEUE_LENGTH
            self.fpsSum = 0.0
            self.sampleNumber = 0
