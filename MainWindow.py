from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QDialog, QTabWidget, QAbstractButton
from PyQt5.QtCore import Qt, QSize

from ui_MainWindow import Ui_MainWindow
from SharedImageBuffer import SharedImageBuffer
from CameraConnectDialog import CameraConnectDialog
from CameraView import CameraView
from Buffer import *
from Config import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.deviceUrlDict = dict()
        self.cameraViewDict = dict()
        newTab = QLabel(self.tabWidget)
        newTab.setText("Kamera/Video tidak terdeteksi")
        newTab.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(newTab, "")
        self.tabWidget.setTabsClosable(False)
        self.connectToCameraButton = QPushButton()
        self.connectToCameraButton.setText("Hubungkan kamera/video")
        self.tabWidget.setCornerWidget(self.connectToCameraButton, Qt.TopLeftCorner)
        self.connectToCameraButton.released.connect(self.connectToCamera)
        self.tabWidget.tabCloseRequested.connect(self.disconnectCamera)
        self.connectToCameraButton.setFocus()
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.actionQuit.triggered.connect(self.close)
        self.actionFullScreen.toggled.connect(self.setFullScreen)
        self.sharedImageBuffer = SharedImageBuffer()
        self.cameraNum = 0

    def connectToCamera(self):
        if (len(self.deviceUrlDict) > 0):
            QMessageBox.warning(self, "YOLOv3: Deteksi Komponen Elektronika",
                                            "Kamera tidak tersedia",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        else:
            nextTabIndex = 0 if len(self.deviceUrlDict) == 0 else self.tabWidget.count()
            cameraConnectDialog = CameraConnectDialog(self)
            if cameraConnectDialog.exec() == QDialog.Accepted:
                deviceUrl = cameraConnectDialog.getDeviceUrl()

                if deviceUrl not in self.deviceUrlDict:
                    imageBuffer = Buffer(cameraConnectDialog.getImageBufferSize())
                    self.sharedImageBuffer.add(deviceUrl, imageBuffer)
                    cameraView = CameraView(self.tabWidget, deviceUrl, self.sharedImageBuffer, self.cameraNum)

                if cameraView.connectToCamera(
                cameraConnectDialog.getDropFrameCheckBoxState(),
                cameraConnectDialog.getApiPreference(),
                cameraConnectDialog.getCaptureThreadPrio(),
                cameraConnectDialog.getProcessingThreadPrio(),
                cameraConnectDialog.getEnableFrameProcessingCheckBoxState(),
                cameraConnectDialog.getResolutionWidth(),
                cameraConnectDialog.getResolutionHeight()):

                    self.cameraNum += 1
                    tabLabel = cameraConnectDialog.getTabLabel()
                    self.tabWidget.setTabsClosable(True)
                    if nextTabIndex == 0:
                        self.tabWidget.removeTab(0)
                        self.tabWidget.addTab(cameraView, '%s [%s]' % (tabLabel, deviceUrl))
                        self.tabWidget.setCurrentWidget(cameraView)
                        self.setTabCloseToolTips(self.tabWidget, "Memutuskan koneksi kamera")
                        self.cameraViewDict[deviceUrl] = cameraView
                        self.deviceUrlDict[deviceUrl] = nextTabIndex
                    else:
                        QMessageBox.warning(self,
                                            "ERROR:",
                                            "Tidak dapat terhubung ke kamera"
                                            "Silahkan cek kembali kamera anda")
                        cameraView.delete()
                        self.sharedImageBuffer.removeByDeviceUrl(deviceUrl)
                        del imageBuffer
                else:
                    QMessageBox.warning(self,
                                        "ERROR:",
                                        "Kamera tidak tersedia")

    def disconnectCamera(self, index):
        doDisconnect = True

        if doDisconnect:
            nTabs = self.tabWidget.count()
            self.tabWidget.removeTab(index)
            deviceUrl = self.getFromDictByTabIndex(self.deviceUrlDict, index)
            self.cameraViewDict[deviceUrl].delete()

            self.cameraViewDict.pop(deviceUrl)
            self.deviceUrlDict.pop(deviceUrl)

            if index != (nTabs - 1):
                self.updateDictValues(self.deviceUrlDict, index)

            if nTabs == 1:
                newTab = QLabel(self.tabWidget)
                newTab.setText("Tidak ada Kamera/Video yang terhubung.")
                newTab.setAlignment(Qt.AlignCenter)
                self.tabWidget.addTab(newTab, "")
                self.tabWidget.setTabsClosable(False)

    def showAboutDialog(self):
        QMessageBox.information(self, "Tentang",
                                "Media Pembelajaran Deteksi Objek Komponen Elektronika\n"
                                "Menggunakan Algoritma YOLOv3\n"
                                "Dirancang oleh\n"
                                "Derwin Mahardika\n"
                                "Jurusan Pendidikan Teknik Elektro\n"
                                "Program Studi Pendidikan Teknik Mekatronika\n"
                                "Fakultas Teknik\n"
                                "Universitas Negeri Yogyakarta\n")

    def getFromDictByTabIndex(self, dic, tabIndex):
        for k, v in dic.items():
            if v == tabIndex:
                return k

    def updateDictValues(self, dic, tabIndex):
        for k, v in dic.items():
            if v > tabIndex:
                dic[k] = v - 1

    def setFullScreen(self, flag):
        if flag:
            self.showFullScreen()
        else:
            self.showNormal()


    def setTabCloseToolTips(self, tabs, tooltip):
        for item in tabs.findChildren(QAbstractButton):
            if item.inherits("CloseButton"):
                item.setToolTip(tooltip)
