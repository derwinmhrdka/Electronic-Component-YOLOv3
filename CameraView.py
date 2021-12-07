from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog
from PyQt5.QtCore import qDebug, QRect, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap

from ui_CameraView import Ui_CameraView
from CaptureThread import CaptureThread
from ImageProcessingSettingsDialog import ImageProcessingSettingsDialog
from ProcessingThread import ProcessingThread
from Structures import *
from collections import Counter


class CameraView(QWidget, Ui_CameraView):
    newImageProcessingFlags = pyqtSignal(ImageProcessingFlags)
    setROI = pyqtSignal(QRect)

    def __init__(self, parent, deviceUrl, sharedImageBuffer, cameraId):
        super(CameraView, self).__init__(parent)
        self.sharedImageBuffer = sharedImageBuffer
        self.cameraId = cameraId
        self.imageProcessingSettingsDialog = ImageProcessingSettingsDialog(self)
        self.setupUi(self)
        self.deviceUrl = deviceUrl
        self.isCameraConnected = False
        self.frameLabel.setText("Tidak ada kamera terhubung.")
        self.imageBufferBar.setValue(0)
        self.imageBufferLabel.setText("[000/000]")
        self.captureRateLabel.setText("")
        self.processingRateLabel.setText("")
        self.deviceUrlLabel.setText("")
        self.cameraResolutionLabel.setText("")
        self.roiLabel.setText("")
        self.mouseCursorPosLabel.setText("")
        self.clearImageBufferButton.setDisabled(True)
        self.imageProcessingFlags = ImageProcessingFlags()
        self.clearImageBufferButton.released.connect(self.clearImageBuffer)
        self.frameLabel.onMouseMoveEvent.connect(self.updateMouseCursorPosLabel)
        self.frameLabel.menu.triggered.connect(self.handleContextMenuAction)

    def delete(self):
        if self.isCameraConnected:
            if self.processingThread.isRunning():
                self.stopProcessingThread()
            if self.captureThread.isRunning():
                self.stopCaptureThread()

            if self.sharedImageBuffer.isSyncEnabledForDeviceUrl(self.deviceUrl):
                self.sharedImageBuffer.setSyncEnabled(True)

            # Disconnect camera
            if self.captureThread.disconnectCamera():
                qDebug("[%s] Koneksi kamera berhasil diputus." % self.deviceUrl)
            else:
                qDebug("[%s] Peringatan: Kamera sudah tidak tersambung." % self.deviceUrl)

    def afterCaptureThreadFinshed(self):
        # Delete Buffer
        self.sharedImageBuffer.removeByDeviceUrl(self.deviceUrl)

    def afterProcessingThreadFinshed(self):
        qDebug("[%s] Peringatan: SQL sudah terputus." % self.deviceUrl)

    def connectToCamera(self, dropFrameIfBufferFull, apiPreference, capThreadPrio,
                        procThreadPrio, enableFrameProcessing, width, height):
        if self.sharedImageBuffer.isSyncEnabledForDeviceUrl(self.deviceUrl):
            self.frameLabel.setText("Menghubungkan Kamera. Menunggu...")
        else:
            self.frameLabel.setText("Menghubungkan ke kamera...")

        self.captureThread = CaptureThread(self.sharedImageBuffer, self.deviceUrl, dropFrameIfBufferFull,
                                           apiPreference, width, height)
        if self.captureThread.connectToCamera():
            self.processingThread = ProcessingThread(self.sharedImageBuffer, self.deviceUrl, self.cameraId)

            self.processingThread.newFrame.connect(self.updateFrame)
            self.processingThread.updateStatisticsInGUI.connect(self.updateProcessingThreadStats)
            self.captureThread.updateStatisticsInGUI.connect(self.updateCaptureThreadStats)
            self.imageProcessingSettingsDialog.newImageProcessingSettings.connect(
                self.processingThread.updateImageProcessingSettings)
            self.newImageProcessingFlags.connect(self.processingThread.updateImageProcessingFlags)
            self.setROI.connect(self.processingThread.setROI)

            self.captureThread.finished.connect(self.afterCaptureThreadFinshed)
            self.processingThread.finished.connect(self.afterProcessingThreadFinshed)

            if enableFrameProcessing:
                self.frameLabel.newMouseData.connect(self.newMouseData)

            self.setROI.emit(
                QRect(0, 0, self.captureThread.getInputSourceWidth(), self.captureThread.getInputSourceHeight()))
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
            self.imageProcessingSettingsDialog.updateStoredSettingsFromDialog()

            self.captureThread.start(capThreadPrio)            
            if enableFrameProcessing:
                self.processingThread.start(procThreadPrio)

            self.imageBufferBar.setMinimum(0)
            self.imageBufferBar.setMaximum(self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl).maxSize())

            self.clearImageBufferButton.setEnabled(True)

            self.deviceUrlLabel.setText(self.deviceUrl)
            self.cameraResolutionLabel.setText("%dx%d" % (self.captureThread.getInputSourceWidth(),
                                                          self.captureThread.getInputSourceHeight()))
            self.isCameraConnected = True
            if not enableFrameProcessing:
                self.frameLabel.setText("Frame processing dimatikan.")
            return True
        else:
            return False

    def stopCaptureThread(self):
        qDebug("[%s] Mengentikan tangkapan citra..." % self.deviceUrl)
        self.captureThread.stop()
        self.sharedImageBuffer.wakeAll()
        if self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl).isFull():
            self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl).get()
        self.captureThread.wait()
        qDebug("[%s] Tangkapan citra berhasil dihentikan." % self.deviceUrl)

    def stopProcessingThread(self):
        qDebug("[%s] Menghentikan pemrosesan citra..." % self.deviceUrl)
        self.processingThread.stop()
        self.sharedImageBuffer.wakeAll()
        self.processingThread.wait()
        qDebug("[%s] Pemrosesan citra berhasil dihentikan." % self.deviceUrl)

    def updateCaptureThreadStats(self, statData):
        imageBuffer = self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl)
        self.imageBufferLabel.setText("[%d/%d]" % (imageBuffer.size(), imageBuffer.maxSize()))
        self.imageBufferBar.setValue(imageBuffer.size())

        self.captureRateLabel.setText("{:>6,.2f} fps".format(statData.averageFPS))
        self.nFramesCapturedLabel.setText("[%d]" % statData.nFramesProcessed)

    def updateProcessingThreadStats(self, statData):
        jumlah_objek = self.processingThread.getDaftar()
        print("Resistor      = " + str(jumlah_objek[0]))
        print("Transistor    = " + str(jumlah_objek[1]))
        print("Kapasitor     = " + str(jumlah_objek[2]))
        print("Dioda         = " + str(jumlah_objek[3]))
        print("Transformator = " + str(jumlah_objek[4]) + '\n')

        resistor_obj = "Resistor\t\t: " + str(jumlah_objek[0])
        transistor_obj = "Transistor\t: " + str(jumlah_objek[1])
        kapasitor_obj = "Kapasitor\t\t: " + str(jumlah_objek[2])
        dioda_obj = "Dioda\t\t: " + str(jumlah_objek[3])
        transformator_obj = "Transformator\t: " + str(jumlah_objek[4])

        self.objek1.setText(resistor_obj)
        self.objek2.setText(transistor_obj)
        self.objek3.setText(kapasitor_obj)
        self.objek4.setText(dioda_obj)
        self.objek5.setText(transformator_obj)
        self.processingRateLabel.setText("{:>6,.2f} fps".format(statData.averageFPS))
        self.roiLabel.setText("(%d,%d) %dx%d" % (self.processingThread.getCurrentROI().x(),
                                                 self.processingThread.getCurrentROI().y(),
                                                 self.processingThread.getCurrentROI().width(),
                                                 self.processingThread.getCurrentROI().height()))
        self.nFramesProcessedLabel.setText("[%d]" % statData.nFramesProcessed)

    def updateFrame(self, frame):
        self.frameLabel.setPixmap(
            QPixmap.fromImage(frame).scaled(self.frameLabel.width(), self.frameLabel.height(), Qt.KeepAspectRatio))

    def clearImageBuffer(self):
        if self.sharedImageBuffer.getByDeviceUrl(self.deviceUrl).clear():
            qDebug("[%s] Image buffer berhasil dibersihkan." % self.deviceUrl)
        else:
            qDebug("[%s] Peringatan: Tidak bisa membersihkan Image Buffer." % self.deviceUrl)

    def setImageProcessingSettings(self):
        if self.imageProcessingSettingsDialog.exec() == QDialog.Accepted:
            self.imageProcessingSettingsDialog.updateStoredSettingsFromDialog()
        else:
            self.imageProcessingSettingsDialog.updateDialogSettingsFromStored()

    def updateMouseCursorPosLabel(self):
        self.mouseCursorPosLabel.setText(
            "(%d,%d)" % (self.frameLabel.getMouseCursorPos().x(), self.frameLabel.getMouseCursorPos().y()))

        if self.frameLabel.pixmap():
            if not self.frameLabel.hasScaledContents():
                xScalingFactor = (self.frameLabel.getMouseCursorPos().x() - (
                        self.frameLabel.width() - self.frameLabel.pixmap().width()) / 2) / self.frameLabel.pixmap().width()
                yScalingFactor = (self.frameLabel.getMouseCursorPos().y() - (
                        self.frameLabel.height() - self.frameLabel.pixmap().height()) / 2) / self.frameLabel.pixmap().height()
            else:
                xScalingFactor = self.frameLabel.getMouseCursorPos().x() / self.frameLabel.width()
                yScalingFactor = self.frameLabel.getMouseCursorPos().y() / self.frameLabel.height()

            self.mouseCursorPosLabel.setText(
                '%s [%d,%d]' % (self.mouseCursorPosLabel.text(),
                                xScalingFactor * self.processingThread.getCurrentROI().width(),
                                yScalingFactor * self.processingThread.getCurrentROI().height()))

    def newMouseData(self, mouseData):
        selectionBox = QRect()
        if mouseData.leftButtonRelease and self.frameLabel.pixmap():
            if not self.frameLabel.hasScaledContents():
                xScalingFactor = (mouseData.selectionBox.x() - (
                        self.frameLabel.width() - self.frameLabel.pixmap().width()) / 2) / self.frameLabel.pixmap().width()
                yScalingFactor = (mouseData.selectionBox.y() - (
                        self.frameLabel.height() - self.frameLabel.pixmap().height()) / 2) / self.frameLabel.pixmap().height()
                wScalingFactor = self.processingThread.getCurrentROI().width() / self.frameLabel.pixmap().width()
                hScalingFactor = self.processingThread.getCurrentROI().height() / self.frameLabel.pixmap().height()
            else:
                xScalingFactor = mouseData.selectionBox.x() / self.frameLabel.width()
                yScalingFactor = mouseData.selectionBox.y() / self.frameLabel.height()
                wScalingFactor = self.processingThread.getCurrentROI().width() / self.frameLabel.width()
                hScalingFactor = self.processingThread.getCurrentROI().height() / self.frameLabel.height()

            selectionBox.setX(
                xScalingFactor * self.processingThread.getCurrentROI().width() + self.processingThread.getCurrentROI().x())
            selectionBox.setY(
                yScalingFactor * self.processingThread.getCurrentROI().height() + self.processingThread.getCurrentROI().y())
            selectionBox.setWidth(wScalingFactor * mouseData.selectionBox.width())
            selectionBox.setHeight(hScalingFactor * mouseData.selectionBox.height())

            if selectionBox.width() != 0 and selectionBox.height() != 0:
                if selectionBox.width() < 0:
                    x_temp = selectionBox.x()
                    width_temp = selectionBox.width()
                    selectionBox.setX(x_temp + selectionBox.width())
                    selectionBox.setWidth(width_temp * -1)
                if selectionBox.height() < 0:
                    y_temp = selectionBox.y()
                    height_temp = selectionBox.height()
                    selectionBox.setY(y_temp + selectionBox.height())
                    selectionBox.setHeight(height_temp * -1)

                if (selectionBox.x() < 0 or selectionBox.y() < 0 or
                        selectionBox.x() + selectionBox.width() > self.processingThread.getCurrentROI().x() + self.processingThread.getCurrentROI().width() or
                        selectionBox.y() + selectionBox.height() > self.processingThread.getCurrentROI().y() + self.processingThread.getCurrentROI().height() or
                        selectionBox.x() < self.processingThread.getCurrentROI().x() or
                        selectionBox.y() < self.processingThread.getCurrentROI().y()):
                    QMessageBox.warning(self,
                                        "ERROR:",
                                        "Seleksi box diluar area. Coba lagi.")
                else:
                    self.setROI.emit(selectionBox)

    def handleContextMenuAction(self, action):
        if action.text() == "Reset ROI":
            self.setROI.emit(
                QRect(0, 0, self.captureThread.getInputSourceWidth(), self.captureThread.getInputSourceHeight()))
        elif action.text() == "Paskan Layar":
            self.frameLabel.setScaledContents(action.isChecked())
        elif action.text() == "Grayscale":
            self.imageProcessingFlags.grayscaleOn = action.isChecked()
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
        elif action.text() == "Smooth":
            self.imageProcessingFlags.smoothOn = action.isChecked()
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
        elif action.text() == "Dilate":
            self.imageProcessingFlags.dilateOn = action.isChecked()
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
        elif action.text() == "Erode":
            self.imageProcessingFlags.erodeOn = action.isChecked()
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
        elif action.text() == "Flip":
            self.imageProcessingFlags.flipOn = action.isChecked()
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
        elif action.text() == "Canny":
            self.imageProcessingFlags.cannyOn = action.isChecked()
            self.newImageProcessingFlags.emit(self.imageProcessingFlags)
        elif action.text() == "Pengaturan...":
            self.setImageProcessingSettings()
