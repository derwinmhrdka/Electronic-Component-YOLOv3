from PyQt5.QtCore import QThread, QMutex, QTime, qDebug, QMutexLocker, pyqtSignal
from PyQt5.QtGui import QImage
from queue import Queue
import cv2
import numpy as np

from MatToQImage import matToQImage
from Structures import *
from Config import *
from collections import Counter


class ProcessingThread(QThread):
    newFrame = pyqtSignal(QImage)
    updateStatisticsInGUI = pyqtSignal(ThreadStatisticsData)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    def __init__(self, sharedImageBuffer, deviceUrl, cameraId, parent=None):
        super(QThread, self).__init__(parent)
        self.sharedImageBuffer = sharedImageBuffer
        self.cameraId = cameraId
        self.deviceUrl = deviceUrl
        self.doStopMutex = QMutex()
        self.processingMutex = QMutex()
        self.t = QTime()
        self.processingTime = 0
        self.doStop = False
        self.enableFrameProcessing = False
        self.sampleNumber = 0
        self.fpsSum = 0.0
        self.fps = Queue()
        self.currentROI = QRect()
        self.imgProcFlags = ImageProcessingFlags()
        self.imgProcSettings = ImageProcessingSettings()
        self.statsData = ThreadStatisticsData()
        self.frame = None
        self.currentFrame = None
        self.label=""
        self.daftar_objek=[]

    def run(self):
        net = cv2.dnn.readNet("Files\yolov3_training_30000.weights", "Files\yolov3-tiny-test.cfg")
        classes = []
        with open("Files\classes.txt", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        #colors = {'resistor':(255,255,0),'transistor':(255,0,255),'kapasitor':(0,255,255),'dioda':(0,0,255),'transformator':(0,255,0)}
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            self.doStopMutex.lock()
            if self.doStop:
                self.doStop = False
                self.doStopMutex.unlock()
                break
            self.doStopMutex.unlock()
            self.processingTime = self.t.elapsed()
            self.t.start()

            with QMutexLocker(self.processingMutex):
                self.currentFrame = self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl).get()[
                                    self.currentROI.y():(self.currentROI.y() + self.currentROI.height()),
                                    self.currentROI.x():(self.currentROI.x() + self.currentROI.width())].copy()

                height, width, channels = self.currentFrame.shape
                blob = cv2.dnn.blobFromImage(self.currentFrame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
                self.currentFrame=self.currentFrame
                net.setInput(blob)
                outs = net.forward(output_layers)
                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                            scores = detection[5:]
                            class_id = np.argmax(scores)
                            confidence = scores[class_id]
                            if confidence > 0.3:
                                center_x = int(detection[0] * width)
                                center_y = int(detection[1] * height)
                                w = int(detection[2] * width)
                                h = int(detection[3] * height)
                                x = int(center_x - w / 2)
                                y = int(center_y - h / 2)
                                boxes.append([x, y, w, h])
                                confidences.append(float(confidence))
                                class_ids.append(class_id)

                self.daftar_objek = Counter(class_ids)
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        self.label = str(classes[class_ids[i]])
                        confidence = confidences[i]
                        confidence = confidence*100
                        confidence = round(confidence, 1)
                        color = colors[class_ids[i]]
                        cv2.rectangle(self.currentFrame, (x, y), (x + w, y + h), color, 2)
                        cv2.rectangle(self.currentFrame, (x, y-30),(x + w, y),
                                                      color, thickness=cv2.FILLED)
                        cv2.putText(self.currentFrame, self.label + " " + str(confidence)+"%", (x, y-5), font, 0.8, (0,0,0), 1, cv2.LINE_AA)


                #Grayscale
                if self.imgProcFlags.grayscaleOn and (
                        self.currentFrame.shape[2] == 3 or self.currentFrame.shape[2] == 4):
                    self.currentFrame = cv2.cvtColor(self.currentFrame, cv2.COLOR_BGR2GRAY)

                # Smooth
                if self.imgProcFlags.smoothOn:
                    if self.imgProcSettings.smoothType == 0:
                        #BLUR
                        self.currentFrame = cv2.blur(self.currentFrame,
                                                     (self.imgProcSettings.smoothParam1,
                                                      self.imgProcSettings.smoothParam2))
                    elif self.imgProcSettings.smoothType == 1:
                        # GAUSSIAN
                        self.currentFrame = cv2.GaussianBlur(self.currentFrame,
                                                             (self.imgProcSettings.smoothParam1,
                                                              self.imgProcSettings.smoothParam2),
                                                             sigmaX=self.imgProcSettings.smoothParam3,
                                                             sigmaY=self.imgProcSettings.smoothParam4)
                    elif self.imgProcSettings.smoothType == 2:
                        # MEDIAN
                        self.currentFrame = cv2.medianBlur(self.currentFrame, self.imgProcSettings.smoothParam1)

                # Dilate
                if self.imgProcFlags.dilateOn:
                    self.currentFrame = cv2.dilate(self.currentFrame, self.kernel,
                                                   iterations=self.imgProcSettings.dilateNumberOfIterations)
                # Erode
                if self.imgProcFlags.erodeOn:
                    self.currentFrame = cv2.erode(self.currentFrame, self.kernel,
                                                  iterations=self.imgProcSettings.erodeUrlOfIterations)
                # Flip
                if self.imgProcFlags.flipOn:
                    height, width, channels = self.currentFrame.shape
                    blob = cv2.dnn.blobFromImage(self.currentFrame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
                    self.currentFrame=self.currentFrame


                # Canny edge detection
                if self.imgProcFlags.cannyOn:
                    self.currentFrame = cv2.Canny(self.currentFrame,
                                                  threshold1=self.imgProcSettings.cannyThreshold1,
                                                  threshold2=self.imgProcSettings.cannyThreshold2,
                                                  apertureSize=self.imgProcSettings.cannyApertureSize,
                                                  L2gradient=self.imgProcSettings.cannyL2gradient)

                self.frame = matToQImage(self.currentFrame)
                self.newFrame.emit(self.frame)

            self.updateFPS(self.processingTime)
            self.statsData.nFramesProcessed += 1
            self.updateStatisticsInGUI.emit(self.statsData)

        qDebug("Menghentikan pengolahan citra...")

    def doShowImage(self, val):
        with QMutexLocker(self.processingMutex):
            self.doShow = val

    def updateFPS(self, timeElapsed):
        if timeElapsed > 0:
            self.fps.put(1000 / timeElapsed)
            self.sampleNumber += 1

        if self.fps.qsize() > PROCESSING_FPS_STAT_QUEUE_LENGTH:
            self.fps.get()

        if self.fps.qsize() == PROCESSING_FPS_STAT_QUEUE_LENGTH and self.sampleNumber == PROCESSING_FPS_STAT_QUEUE_LENGTH:
            while not self.fps.empty():
                self.fpsSum += self.fps.get()
            self.statsData.averageFPS = self.fpsSum / PROCESSING_FPS_STAT_QUEUE_LENGTH
            self.fpsSum = 0.0
            self.sampleNumber = 0

    def stop(self):
        with QMutexLocker(self.doStopMutex):
            self.doStop = True

    def updateBoxesBufferMax(self, boxesBufferMax):
        with QMutexLocker(self.processingMutex):
            self.boxesBufferMax = boxesBufferMax

    def updateImageProcessingFlags(self, imgProcFlags):
        with QMutexLocker(self.processingMutex):
            self.imgProcFlags.grayscaleOn = imgProcFlags.grayscaleOn
            self.imgProcFlags.smoothOn = imgProcFlags.smoothOn
            self.imgProcFlags.dilateOn = imgProcFlags.dilateOn
            self.imgProcFlags.erodeOn = imgProcFlags.erodeOn
            self.imgProcFlags.flipOn = imgProcFlags.flipOn
            self.imgProcFlags.cannyOn = imgProcFlags.cannyOn

    def updateImageProcessingSettings(self, imgProcSettings):
        with QMutexLocker(self.processingMutex):
            self.imgProcSettings.smoothType = imgProcSettings.smoothType
            self.imgProcSettings.smoothParam1 = imgProcSettings.smoothParam1
            self.imgProcSettings.smoothParam2 = imgProcSettings.smoothParam2
            self.imgProcSettings.smoothParam3 = imgProcSettings.smoothParam3
            self.imgProcSettings.smoothParam4 = imgProcSettings.smoothParam4
            self.imgProcSettings.dilateNumberOfIterations = imgProcSettings.dilateNumberOfIterations
            self.imgProcSettings.erodeUrlOfIterations = imgProcSettings.erodeUrlOfIterations
            self.imgProcSettings.flipCode = imgProcSettings.flipCode
            self.imgProcSettings.cannyThreshold1 = imgProcSettings.cannyThreshold1
            self.imgProcSettings.cannyThreshold2 = imgProcSettings.cannyThreshold2
            self.imgProcSettings.cannyApertureSize = imgProcSettings.cannyApertureSize
            self.imgProcSettings.cannyL2gradient = imgProcSettings.cannyL2gradient

    def setROI(self, roi):
        with QMutexLocker(self.processingMutex):
            self.currentROI.setX(roi.x())
            self.currentROI.setY(roi.y())
            self.currentROI.setWidth(roi.width())
            self.currentROI.setHeight(roi.height())

    def getCurrentROI(self):
        return QRect(self.currentROI.x(), self.currentROI.y(), self.currentROI.width(), self.currentROI.height())

    def getLabel(self):
        return self.label

    def getDaftar(self):
        return self.daftar_objek
