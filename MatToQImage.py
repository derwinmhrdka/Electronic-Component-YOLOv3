from PyQt5.QtCore import qDebug
from PyQt5.QtGui import QImage
import numpy as np


def matToQImage(data):
    if data.dtype == np.uint8:
        channels = 1 if len(data.shape) == 2 else data.shape[2]
        if channels == 3:
            img = QImage(data, data.shape[1], data.shape[0], data.strides[0], QImage.Format_RGB888)
            return img.rgbSwapped()
        elif channels == 1:
            img = QImage(data, data.shape[1], data.shape[0], data.strides[0], QImage.Format_Indexed8)
            return img

    qDebug("ERROR: numpy.ndarray tidak bisa dikonversi ke QImage. Channels = %d" % data.shape[2])
    return QImage()
