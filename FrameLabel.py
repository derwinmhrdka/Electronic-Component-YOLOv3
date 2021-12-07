from PyQt5.QtWidgets import QLabel, QMenu, QAction
from PyQt5.QtCore import QPoint, pyqtSignal, Qt
from PyQt5.QtGui import QPainter

from Structures import *


class FrameLabel(QLabel):
    newMouseData = pyqtSignal(MouseData)
    onMouseMoveEvent = pyqtSignal()

    def __init__(self, parent=None):
        super(FrameLabel, self).__init__(parent)
        self.menu = None
        self.mouseData = MouseData()
        self.startPoint = QPoint()
        self.mouseCursorPos = QPoint()
        self.drawBox = False
        self.box = QRect()

        self.startPoint.setX(0)
        self.startPoint.setY(0)
        self.mouseCursorPos.setX(0)
        self.mouseCursorPos.setY(0)
        self.mouseData.leftButtonRelease = False
        self.mouseData.rightButtonRelease = False
        self.createContextMenu()

    def mouseMoveEvent(self, ev):
        self.setMouseCursorPos(ev.pos())
        if self.drawBox:
            self.box.setWidth(self.getMouseCursorPos().x() - self.startPoint.x())
            self.box.setHeight(self.getMouseCursorPos().y() - self.startPoint.y())
        self.onMouseMoveEvent.emit()

    def setMouseCursorPos(self, data):
        self.mouseCursorPos = data

    def getMouseCursorPos(self):
        return self.mouseCursorPos

    def mouseReleaseEvent(self, ev):
        self.setMouseCursorPos(ev.pos())
        if ev.button() == Qt.LeftButton:
            self.mouseData.leftButtonRelease = True
            if self.drawBox:
                self.drawBox = False
                self.mouseData.selectionBox.setX(self.box.left())
                self.mouseData.selectionBox.setY(self.box.top())
                self.mouseData.selectionBox.setWidth(self.box.width())
                self.mouseData.selectionBox.setHeight(self.box.height())
                self.mouseData.leftButtonRelease = True
                self.newMouseData.emit(self.mouseData)
            self.mouseData.leftButtonRelease = False
        elif ev.button() == Qt.RightButton:
            if self.drawBox:
                self.drawBox = False
            else:
                self.menu.exec(ev.globalPos())

    def mousePressEvent(self, ev):
        self.setMouseCursorPos(ev.pos())
        if ev.button() == Qt.LeftButton:
            self.startPoint = ev.pos()
            self.box = QRect(self.startPoint.x(), self.startPoint.y(), 0, 0)
            self.drawBox = True

    def paintEvent(self, ev):
        QLabel.paintEvent(self, ev)
        painter = QPainter(self)
        if self.drawBox:
            painter.setPen(Qt.blue)
            painter.drawRect(self.box)

    def createContextMenu(self):
        self.menu = QMenu(self)
        action = QAction(self)
        action.setText("Reset ROI")
        self.menu.addAction(action)
        action = QAction(self)
        action.setText("Paskan ke layar")
        action.setCheckable(True)
        self.menu.addAction(action)
        self.menu.addSeparator()
        menu_imgProc = QMenu(self)
        menu_imgProc.setTitle("Image Processing")
        self.menu.addMenu(menu_imgProc)
        # Add actions
        action = QAction(self)
        action.setText("Grayscale")
        action.setCheckable(True)
        menu_imgProc.addAction(action)
        action = QAction(self)
        action.setText("Smooth")
        action.setCheckable(True)
        menu_imgProc.addAction(action)
        action = QAction(self)
        action.setText("Dilate")
        action.setCheckable(True)
        menu_imgProc.addAction(action)
        action = QAction(self)
        action.setText("Erode")
        action.setCheckable(True)
        menu_imgProc.addAction(action)
        action = QAction(self)
        action.setText("Flip")
        action.setCheckable(True)
        menu_imgProc.addAction(action)
        action = QAction(self)
        action.setText("Canny")
        action.setCheckable(True)
        menu_imgProc.addAction(action)
        menu_imgProc.addSeparator()
        action = QAction(self)
        action.setText("Pengaturan...")
        menu_imgProc.addAction(action)
