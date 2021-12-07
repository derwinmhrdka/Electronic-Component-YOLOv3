import sys
from PyQt5.QtWidgets import QApplication
import qdarkstyle

from MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

