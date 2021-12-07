from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtCore import QRegExp, qDebug, QThread
from PyQt5.QtGui import QRegExpValidator
import cv2

from ui_CameraConnectDialog import Ui_CameraConnectDialog
from Config import *


class CameraConnectDialog(QDialog, Ui_CameraConnectDialog):
    def __init__(self, parent=None, isStreamSyncEnabled=False):
        super(CameraConnectDialog, self).__init__(parent)
        self.setupUi(self)
        self.resWEdit.setValidator(QRegExpValidator(QRegExp("^[0-9]{1,4}$")))  # Integers 0 to 9999
        self.resHEdit.setValidator(QRegExpValidator(QRegExp("^[0-9]{1,4}$")))  # Integers 0 to 9999
        self.apiPreference = {'CAP_ANY': cv2.CAP_ANY,
                              'CAP_DSHOW': cv2.CAP_DSHOW,
                              'CAP_MSMF': cv2.CAP_MSMF,
                              }
        self.deviceUrlList = {'Kamera Webcam': '0',
                              'Kamera External 1 (DroidCam)': '1',
                              'Kamera External 1 (Nikon D330)': '2',
                              'Kamera lainnya': '3',}
        self.deviceUrlEdit.addItems(self.deviceUrlList.keys())
        self.resetToDefaultsPushButton.released.connect(self.resetToDefaults)
        self.deviceUrlRadioButton.clicked.connect(lambda: self.setUrlMode('device url'))
        self.filenameRadioButton.clicked.connect(lambda: self.setUrlMode('filename'))
        self.importFilePushButton.clicked.connect(self.openFile)
        self.deviceUrlRadioButton.setChecked(True)
        self.deviceUrlEdit.setEnabled(True)
        self.filenameEdit.setEnabled(False)
        self.importFilePushButton.setEnabled(False)

    def getDeviceUrl(self):
        if self.filenameRadioButton.isChecked():
            if self.filenameEdit.text().strip() == '':
                if DEFAULT_FILENAME.strip() == '':
                    QMessageBox.warning(self.parentWidget(),
                                        "PERINGATAN",
                                        "URL Perangkat Kosong.\n"
                                        "Set Otomatis ke Webcam.")
                    return '0'
                else:
                    QMessageBox.warning(self.parentWidget(),
                                        "PERINGATAN:",
                                        "URL Perangkat Kosong.\n"
                                        "Set Otomatis ke %s." % DEFAULT_FILENAME)
                    return DEFAULT_FILENAME
            else:
                return self.filenameEdit.text()
        else:
            deviceUrlStart = str(self.deviceUrlEdit.currentIndex())
            return deviceUrlStart

    def getResolutionWidth(self):
        if self.resWEdit.text().strip() == '':
            return -1
        else:
            return int(self.resWEdit.text())

    def getResolutionHeight(self):
        if self.resHEdit.text().strip() == '':
            return -1
        else:
            return int(self.resHEdit.text())

    def setUrlMode(self, mode):
        if mode == 'device url':
            self.deviceUrlEdit.setEnabled(True)
            self.filenameEdit.setEnabled(False)
            self.importFilePushButton.setEnabled(False)
            self.deviceUrlRadioButton.setChecked(True)
        elif mode == 'filename':
            self.deviceUrlEdit.setEnabled(False)
            self.filenameEdit.setEnabled(True)
            self.importFilePushButton.setEnabled(True)
            self.filenameRadioButton.setChecked(True)

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self.parent(), 'Buka file', '.', 'Video files(*.mp4 , *.avi)')[0]
        self.filenameEdit.setText(filename)

    def getImageBufferSize(self):
        return 1

    def getApiPreference(self):
        return cv2.CAP_ANY

    def getDropFrameCheckBoxState(self):
        return

    def getCaptureThreadPrio(self):
        return QThread.HighestPriority

    def getProcessingThreadPrio(self):
        return QThread.HighestPriority

    def getTabLabel(self):
        return self.tabLabelEdit.text()

    def getEnableFrameProcessingCheckBoxState(self):
        return True

    def resetToDefaults(self):
        self.filenameEdit.clear()
        self.deviceUrlEdit.setCurrentIndex(0)
        self.resWEdit.clear()
        self.resHEdit.clear()
