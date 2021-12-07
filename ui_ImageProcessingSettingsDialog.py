from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageProcessingSettingsDialog(object):
    def setupUi(self, ImageProcessingSettingsDialog):
        ImageProcessingSettingsDialog.setObjectName("ImageProcessingSettingsDialog")
        ImageProcessingSettingsDialog.resize(440, 380)
        self.layoutWidget1 = QtWidgets.QWidget(ImageProcessingSettingsDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 421, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget1)
        self.tabWidget.setObjectName("tabWidget")
        self.smoothTab_5 = QtWidgets.QWidget()
        self.smoothTab_5.setObjectName("smoothTab_5")
        self.layoutWidget2_5 = QtWidgets.QWidget(self.smoothTab_5)
        self.layoutWidget2_5.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.layoutWidget2_5.setObjectName("layoutWidget2_5")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.layoutWidget2_5)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_68 = QtWidgets.QLabel(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy)
        self.label_68.setMinimumSize(QtCore.QSize(0, 27))
        self.label_68.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_42.addWidget(self.label_68)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.smoothBlurButton = QtWidgets.QRadioButton(self.layoutWidget2_5)
        self.smoothBlurButton.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothBlurButton.setFont(font)
        self.smoothBlurButton.setObjectName("smoothBlurButton")
        self.smoothTypeGroup = QtWidgets.QButtonGroup(ImageProcessingSettingsDialog)
        self.smoothTypeGroup.setObjectName("smoothTypeGroup")
        self.smoothTypeGroup.addButton(self.smoothBlurButton)
        self.verticalLayout_43.addWidget(self.smoothBlurButton)
        self.smoothGaussianButton = QtWidgets.QRadioButton(self.layoutWidget2_5)
        self.smoothGaussianButton.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothGaussianButton.setFont(font)
        self.smoothGaussianButton.setObjectName("smoothGaussianButton")
        self.smoothTypeGroup.addButton(self.smoothGaussianButton)
        self.verticalLayout_43.addWidget(self.smoothGaussianButton)
        self.smoothMedianButton = QtWidgets.QRadioButton(self.layoutWidget2_5)
        self.smoothMedianButton.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothMedianButton.setFont(font)
        self.smoothMedianButton.setObjectName("smoothMedianButton")
        self.smoothTypeGroup.addButton(self.smoothMedianButton)
        self.verticalLayout_43.addWidget(self.smoothMedianButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_43.addItem(spacerItem)
        self.verticalLayout_42.addLayout(self.verticalLayout_43)
        self.horizontalLayout_48.addLayout(self.verticalLayout_42)
        self.verticalLayout_44 = QtWidgets.QVBoxLayout()
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_69 = QtWidgets.QLabel(self.layoutWidget2_5)
        self.label_69.setMinimumSize(QtCore.QSize(0, 27))
        self.label_69.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.verticalLayout_44.addWidget(self.label_69)
        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.label_70 = QtWidgets.QLabel(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMinimumSize(QtCore.QSize(15, 0))
        self.label_70.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_49.addWidget(self.label_70)
        self.smoothParam1Edit = QtWidgets.QLineEdit(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smoothParam1Edit.sizePolicy().hasHeightForWidth())
        self.smoothParam1Edit.setSizePolicy(sizePolicy)
        self.smoothParam1Edit.setMinimumSize(QtCore.QSize(45, 0))
        self.smoothParam1Edit.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam1Edit.setFont(font)
        self.smoothParam1Edit.setObjectName("smoothParam1Edit")
        self.horizontalLayout_49.addWidget(self.smoothParam1Edit)
        self.smoothParam1RangeLabel = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.smoothParam1RangeLabel.setFont(font)
        self.smoothParam1RangeLabel.setText("")
        self.smoothParam1RangeLabel.setObjectName("smoothParam1RangeLabel")
        self.horizontalLayout_49.addWidget(self.smoothParam1RangeLabel)
        self.smoothParam1Label = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam1Label.setFont(font)
        self.smoothParam1Label.setText("")
        self.smoothParam1Label.setObjectName("smoothParam1Label")
        self.horizontalLayout_49.addWidget(self.smoothParam1Label)
        self.verticalLayout_45.addLayout(self.horizontalLayout_49)
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_71 = QtWidgets.QLabel(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QtCore.QSize(15, 0))
        self.label_71.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_50.addWidget(self.label_71)
        self.smoothParam2Edit = QtWidgets.QLineEdit(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smoothParam2Edit.sizePolicy().hasHeightForWidth())
        self.smoothParam2Edit.setSizePolicy(sizePolicy)
        self.smoothParam2Edit.setMinimumSize(QtCore.QSize(45, 0))
        self.smoothParam2Edit.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam2Edit.setFont(font)
        self.smoothParam2Edit.setObjectName("smoothParam2Edit")
        self.horizontalLayout_50.addWidget(self.smoothParam2Edit)
        self.smoothParam2RangeLabel = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.smoothParam2RangeLabel.setFont(font)
        self.smoothParam2RangeLabel.setText("")
        self.smoothParam2RangeLabel.setObjectName("smoothParam2RangeLabel")
        self.horizontalLayout_50.addWidget(self.smoothParam2RangeLabel)
        self.smoothParam2Label = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam2Label.setFont(font)
        self.smoothParam2Label.setText("")
        self.smoothParam2Label.setObjectName("smoothParam2Label")
        self.horizontalLayout_50.addWidget(self.smoothParam2Label)
        self.verticalLayout_45.addLayout(self.horizontalLayout_50)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.label_72 = QtWidgets.QLabel(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMinimumSize(QtCore.QSize(15, 0))
        self.label_72.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_51.addWidget(self.label_72)
        self.smoothParam3Edit = QtWidgets.QLineEdit(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smoothParam3Edit.sizePolicy().hasHeightForWidth())
        self.smoothParam3Edit.setSizePolicy(sizePolicy)
        self.smoothParam3Edit.setMinimumSize(QtCore.QSize(45, 0))
        self.smoothParam3Edit.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam3Edit.setFont(font)
        self.smoothParam3Edit.setObjectName("smoothParam3Edit")
        self.horizontalLayout_51.addWidget(self.smoothParam3Edit)
        self.smoothParam3RangeLabel = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.smoothParam3RangeLabel.setFont(font)
        self.smoothParam3RangeLabel.setText("")
        self.smoothParam3RangeLabel.setObjectName("smoothParam3RangeLabel")
        self.horizontalLayout_51.addWidget(self.smoothParam3RangeLabel)
        self.smoothParam3Label = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam3Label.setFont(font)
        self.smoothParam3Label.setText("")
        self.smoothParam3Label.setObjectName("smoothParam3Label")
        self.horizontalLayout_51.addWidget(self.smoothParam3Label)
        self.verticalLayout_45.addLayout(self.horizontalLayout_51)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_73 = QtWidgets.QLabel(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QtCore.QSize(15, 0))
        self.label_73.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_52.addWidget(self.label_73)
        self.smoothParam4Edit = QtWidgets.QLineEdit(self.layoutWidget2_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smoothParam4Edit.sizePolicy().hasHeightForWidth())
        self.smoothParam4Edit.setSizePolicy(sizePolicy)
        self.smoothParam4Edit.setMinimumSize(QtCore.QSize(45, 0))
        self.smoothParam4Edit.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam4Edit.setFont(font)
        self.smoothParam4Edit.setObjectName("smoothParam4Edit")
        self.horizontalLayout_52.addWidget(self.smoothParam4Edit)
        self.smoothParam4RangeLabel = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.smoothParam4RangeLabel.setFont(font)
        self.smoothParam4RangeLabel.setText("")
        self.smoothParam4RangeLabel.setObjectName("smoothParam4RangeLabel")
        self.horizontalLayout_52.addWidget(self.smoothParam4RangeLabel)
        self.smoothParam4Label = QtWidgets.QLabel(self.layoutWidget2_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.smoothParam4Label.setFont(font)
        self.smoothParam4Label.setText("")
        self.smoothParam4Label.setObjectName("smoothParam4Label")
        self.horizontalLayout_52.addWidget(self.smoothParam4Label)
        self.verticalLayout_45.addLayout(self.horizontalLayout_52)
        self.verticalLayout_44.addLayout(self.verticalLayout_45)
        self.horizontalLayout_48.addLayout(self.verticalLayout_44)
        self.verticalLayout_41.addLayout(self.horizontalLayout_48)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_41.addItem(spacerItem1)
        self.resetSmoothToDefaultsButton = QtWidgets.QPushButton(self.layoutWidget2_5)
        self.resetSmoothToDefaultsButton.setObjectName("resetSmoothToDefaultsButton")
        self.verticalLayout_41.addWidget(self.resetSmoothToDefaultsButton)
        self.tabWidget.addTab(self.smoothTab_5, "")
        self.dilateTab_5 = QtWidgets.QWidget()
        self.dilateTab_5.setObjectName("dilateTab_5")
        self.layoutWidget3_5 = QtWidgets.QWidget(self.dilateTab_5)
        self.layoutWidget3_5.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.layoutWidget3_5.setObjectName("layoutWidget3_5")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.layoutWidget3_5)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_74 = QtWidgets.QLabel(self.layoutWidget3_5)
        self.label_74.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_53.addWidget(self.label_74)
        self.dilateIterationsEdit = QtWidgets.QLineEdit(self.layoutWidget3_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dilateIterationsEdit.sizePolicy().hasHeightForWidth())
        self.dilateIterationsEdit.setSizePolicy(sizePolicy)
        self.dilateIterationsEdit.setMinimumSize(QtCore.QSize(50, 27))
        self.dilateIterationsEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dilateIterationsEdit.setFont(font)
        self.dilateIterationsEdit.setObjectName("dilateIterationsEdit")
        self.horizontalLayout_53.addWidget(self.dilateIterationsEdit)
        self.label_75 = QtWidgets.QLabel(self.layoutWidget3_5)
        self.label_75.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.horizontalLayout_53.addWidget(self.label_75)
        self.verticalLayout_46.addLayout(self.horizontalLayout_53)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_46.addItem(spacerItem2)
        self.resetDilateToDefaultsButton = QtWidgets.QPushButton(self.layoutWidget3_5)
        self.resetDilateToDefaultsButton.setObjectName("resetDilateToDefaultsButton")
        self.verticalLayout_46.addWidget(self.resetDilateToDefaultsButton)
        self.tabWidget.addTab(self.dilateTab_5, "")
        self.erodeTab_5 = QtWidgets.QWidget()
        self.erodeTab_5.setObjectName("erodeTab_5")
        self.layoutWidget4_5 = QtWidgets.QWidget(self.erodeTab_5)
        self.layoutWidget4_5.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.layoutWidget4_5.setObjectName("layoutWidget4_5")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.layoutWidget4_5)
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_76 = QtWidgets.QLabel(self.layoutWidget4_5)
        self.label_76.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.horizontalLayout_54.addWidget(self.label_76)
        self.erodeIterationsEdit = QtWidgets.QLineEdit(self.layoutWidget4_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.erodeIterationsEdit.sizePolicy().hasHeightForWidth())
        self.erodeIterationsEdit.setSizePolicy(sizePolicy)
        self.erodeIterationsEdit.setMinimumSize(QtCore.QSize(50, 27))
        self.erodeIterationsEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.erodeIterationsEdit.setFont(font)
        self.erodeIterationsEdit.setObjectName("erodeIterationsEdit")
        self.horizontalLayout_54.addWidget(self.erodeIterationsEdit)
        self.label_77 = QtWidgets.QLabel(self.layoutWidget4_5)
        self.label_77.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.horizontalLayout_54.addWidget(self.label_77)
        self.verticalLayout_47.addLayout(self.horizontalLayout_54)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_47.addItem(spacerItem3)
        self.resetErodeToDefaultsButton = QtWidgets.QPushButton(self.layoutWidget4_5)
        self.resetErodeToDefaultsButton.setObjectName("resetErodeToDefaultsButton")
        self.verticalLayout_47.addWidget(self.resetErodeToDefaultsButton)
        self.tabWidget.addTab(self.erodeTab_5, "")
        self.flipTab_5 = QtWidgets.QWidget()
        self.flipTab_5.setObjectName("flipTab_5")
        self.layoutWidget5_5 = QtWidgets.QWidget(self.flipTab_5)
        self.layoutWidget5_5.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.layoutWidget5_5.setObjectName("layoutWidget5_5")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.layoutWidget5_5)
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_78 = QtWidgets.QLabel(self.layoutWidget5_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setMinimumSize(QtCore.QSize(0, 27))
        self.label_78.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.horizontalLayout_55.addWidget(self.label_78)
        self.flipXAxisButton = QtWidgets.QRadioButton(self.layoutWidget5_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.flipXAxisButton.setFont(font)
        self.flipXAxisButton.setObjectName("flipXAxisButton")
        self.flipCodeGroup = QtWidgets.QButtonGroup(ImageProcessingSettingsDialog)
        self.flipCodeGroup.setObjectName("flipCodeGroup")
        self.flipCodeGroup.addButton(self.flipXAxisButton)
        self.horizontalLayout_55.addWidget(self.flipXAxisButton)
        self.flipYAxisButton = QtWidgets.QRadioButton(self.layoutWidget5_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.flipYAxisButton.setFont(font)
        self.flipYAxisButton.setObjectName("flipYAxisButton")
        self.flipCodeGroup.addButton(self.flipYAxisButton)
        self.horizontalLayout_55.addWidget(self.flipYAxisButton)
        self.flipBothAxesButton = QtWidgets.QRadioButton(self.layoutWidget5_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.flipBothAxesButton.setFont(font)
        self.flipBothAxesButton.setObjectName("flipBothAxesButton")
        self.flipCodeGroup.addButton(self.flipBothAxesButton)
        self.horizontalLayout_55.addWidget(self.flipBothAxesButton)
        self.verticalLayout_48.addLayout(self.horizontalLayout_55)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_48.addItem(spacerItem4)
        self.resetFlipToDefaultsButton = QtWidgets.QPushButton(self.layoutWidget5_5)
        self.resetFlipToDefaultsButton.setObjectName("resetFlipToDefaultsButton")
        self.verticalLayout_48.addWidget(self.resetFlipToDefaultsButton)
        self.tabWidget.addTab(self.flipTab_5, "")
        self.cannyTab_5 = QtWidgets.QWidget()
        self.cannyTab_5.setObjectName("cannyTab_5")
        self.layoutWidget6_5 = QtWidgets.QWidget(self.cannyTab_5)
        self.layoutWidget6_5.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.layoutWidget6_5.setObjectName("layoutWidget6_5")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.layoutWidget6_5)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_79 = QtWidgets.QLabel(self.layoutWidget6_5)
        self.label_79.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.horizontalLayout_56.addWidget(self.label_79)
        self.cannyThresh1Edit = QtWidgets.QLineEdit(self.layoutWidget6_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cannyThresh1Edit.sizePolicy().hasHeightForWidth())
        self.cannyThresh1Edit.setSizePolicy(sizePolicy)
        self.cannyThresh1Edit.setMinimumSize(QtCore.QSize(50, 27))
        self.cannyThresh1Edit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cannyThresh1Edit.setFont(font)
        self.cannyThresh1Edit.setObjectName("cannyThresh1Edit")
        self.horizontalLayout_56.addWidget(self.cannyThresh1Edit)
        self.label_80 = QtWidgets.QLabel(self.layoutWidget6_5)
        self.label_80.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.horizontalLayout_56.addWidget(self.label_80)
        self.verticalLayout_49.addLayout(self.horizontalLayout_56)
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.label_81 = QtWidgets.QLabel(self.layoutWidget6_5)
        self.label_81.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.horizontalLayout_57.addWidget(self.label_81)
        self.cannyThresh2Edit = QtWidgets.QLineEdit(self.layoutWidget6_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cannyThresh2Edit.sizePolicy().hasHeightForWidth())
        self.cannyThresh2Edit.setSizePolicy(sizePolicy)
        self.cannyThresh2Edit.setMinimumSize(QtCore.QSize(50, 27))
        self.cannyThresh2Edit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cannyThresh2Edit.setFont(font)
        self.cannyThresh2Edit.setObjectName("cannyThresh2Edit")
        self.horizontalLayout_57.addWidget(self.cannyThresh2Edit)
        self.label_82 = QtWidgets.QLabel(self.layoutWidget6_5)
        self.label_82.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.horizontalLayout_57.addWidget(self.label_82)
        self.verticalLayout_49.addLayout(self.horizontalLayout_57)
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.label_83 = QtWidgets.QLabel(self.layoutWidget6_5)
        self.label_83.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.horizontalLayout_58.addWidget(self.label_83)
        self.cannyApertureSizeEdit = QtWidgets.QLineEdit(self.layoutWidget6_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cannyApertureSizeEdit.sizePolicy().hasHeightForWidth())
        self.cannyApertureSizeEdit.setSizePolicy(sizePolicy)
        self.cannyApertureSizeEdit.setMinimumSize(QtCore.QSize(50, 27))
        self.cannyApertureSizeEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cannyApertureSizeEdit.setFont(font)
        self.cannyApertureSizeEdit.setObjectName("cannyApertureSizeEdit")
        self.horizontalLayout_58.addWidget(self.cannyApertureSizeEdit)
        self.label_84 = QtWidgets.QLabel(self.layoutWidget6_5)
        self.label_84.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.horizontalLayout_58.addWidget(self.label_84)
        self.verticalLayout_49.addLayout(self.horizontalLayout_58)
        self.cannyL2NormCheckBox = QtWidgets.QCheckBox(self.layoutWidget6_5)
        self.cannyL2NormCheckBox.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.cannyL2NormCheckBox.setFont(font)
        self.cannyL2NormCheckBox.setObjectName("cannyL2NormCheckBox")
        self.verticalLayout_49.addWidget(self.cannyL2NormCheckBox)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_49.addItem(spacerItem5)
        self.resetCannyToDefaultsButton = QtWidgets.QPushButton(self.layoutWidget6_5)
        self.resetCannyToDefaultsButton.setObjectName("resetCannyToDefaultsButton")
        self.verticalLayout_49.addWidget(self.resetCannyToDefaultsButton)
        self.tabWidget.addTab(self.cannyTab_5, "")
        self.verticalLayout_40.addWidget(self.tabWidget)
        self.line_9 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_40.addWidget(self.line_9)
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.applyButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_59.addWidget(self.applyButton)
        self.resetAllToDefaultsButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.resetAllToDefaultsButton.setObjectName("resetAllToDefaultsButton")
        self.horizontalLayout_59.addWidget(self.resetAllToDefaultsButton)
        self.verticalLayout_40.addLayout(self.horizontalLayout_59)
        self.line_10 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_40.addWidget(self.line_10)
        self.okCancelBox = QtWidgets.QDialogButtonBox(self.layoutWidget1)
        self.okCancelBox.setOrientation(QtCore.Qt.Horizontal)
        self.okCancelBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.okCancelBox.setObjectName("okCancelBox")
        self.verticalLayout_40.addWidget(self.okCancelBox)

        self.retranslateUi(ImageProcessingSettingsDialog)
        self.tabWidget.setCurrentIndex(4)
        self.okCancelBox.accepted.connect(ImageProcessingSettingsDialog.accept)
        self.okCancelBox.rejected.connect(ImageProcessingSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImageProcessingSettingsDialog)
        ImageProcessingSettingsDialog.setTabOrder(self.tabWidget, self.applyButton)
        ImageProcessingSettingsDialog.setTabOrder(self.applyButton, self.resetAllToDefaultsButton)
        ImageProcessingSettingsDialog.setTabOrder(self.resetAllToDefaultsButton, self.okCancelBox)
        ImageProcessingSettingsDialog.setTabOrder(self.okCancelBox, self.smoothBlurButton)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothBlurButton, self.smoothGaussianButton)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothGaussianButton, self.smoothMedianButton)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothMedianButton, self.smoothParam1Edit)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothParam1Edit, self.smoothParam2Edit)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothParam2Edit, self.smoothParam3Edit)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothParam3Edit, self.smoothParam4Edit)
        ImageProcessingSettingsDialog.setTabOrder(self.smoothParam4Edit, self.resetSmoothToDefaultsButton)
        ImageProcessingSettingsDialog.setTabOrder(self.resetSmoothToDefaultsButton, self.dilateIterationsEdit)
        ImageProcessingSettingsDialog.setTabOrder(self.dilateIterationsEdit, self.resetDilateToDefaultsButton)
        ImageProcessingSettingsDialog.setTabOrder(self.resetDilateToDefaultsButton, self.erodeIterationsEdit)
        ImageProcessingSettingsDialog.setTabOrder(self.erodeIterationsEdit, self.resetErodeToDefaultsButton)
        ImageProcessingSettingsDialog.setTabOrder(self.resetErodeToDefaultsButton, self.flipXAxisButton)
        ImageProcessingSettingsDialog.setTabOrder(self.flipXAxisButton, self.flipYAxisButton)
        ImageProcessingSettingsDialog.setTabOrder(self.flipYAxisButton, self.flipBothAxesButton)
        ImageProcessingSettingsDialog.setTabOrder(self.flipBothAxesButton, self.resetFlipToDefaultsButton)
        ImageProcessingSettingsDialog.setTabOrder(self.resetFlipToDefaultsButton, self.cannyThresh1Edit)
        ImageProcessingSettingsDialog.setTabOrder(self.cannyThresh1Edit, self.cannyThresh2Edit)
        ImageProcessingSettingsDialog.setTabOrder(self.cannyThresh2Edit, self.cannyApertureSizeEdit)
        ImageProcessingSettingsDialog.setTabOrder(self.cannyApertureSizeEdit, self.cannyL2NormCheckBox)
        ImageProcessingSettingsDialog.setTabOrder(self.cannyL2NormCheckBox, self.resetCannyToDefaultsButton)

    def retranslateUi(self, ImageProcessingSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageProcessingSettingsDialog.setWindowTitle(_translate("ImageProcessingSettingsDialog", "Pengaturan Image Processing"))
        self.label_68.setText(_translate("ImageProcessingSettingsDialog", "Tipe:"))
        self.smoothBlurButton.setText(_translate("ImageProcessingSettingsDialog", "Blur"))
        self.smoothGaussianButton.setText(_translate("ImageProcessingSettingsDialog", "Gaussian"))
        self.smoothMedianButton.setText(_translate("ImageProcessingSettingsDialog", "Median"))
        self.label_69.setText(_translate("ImageProcessingSettingsDialog", "Parameters:"))
        self.label_70.setText(_translate("ImageProcessingSettingsDialog", "1:"))
        self.label_71.setText(_translate("ImageProcessingSettingsDialog", "2:"))
        self.label_72.setText(_translate("ImageProcessingSettingsDialog", "3:"))
        self.label_73.setText(_translate("ImageProcessingSettingsDialog", "4:"))
        self.resetSmoothToDefaultsButton.setText(_translate("ImageProcessingSettingsDialog", "Reset ke Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.smoothTab_5), _translate("ImageProcessingSettingsDialog", "Smooth"))
        self.label_74.setText(_translate("ImageProcessingSettingsDialog", "Jumlah iterasi:"))
        self.label_75.setText(_translate("ImageProcessingSettingsDialog", "[1-999]"))
        self.resetDilateToDefaultsButton.setText(_translate("ImageProcessingSettingsDialog", "Reset ke Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dilateTab_5), _translate("ImageProcessingSettingsDialog", "Dilate"))
        self.label_76.setText(_translate("ImageProcessingSettingsDialog", "Jumlah iterasi:"))
        self.label_77.setText(_translate("ImageProcessingSettingsDialog", "[1-999]"))
        self.resetErodeToDefaultsButton.setText(_translate("ImageProcessingSettingsDialog", "Reset ke Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.erodeTab_5), _translate("ImageProcessingSettingsDialog", "Erode"))
        self.label_78.setText(_translate("ImageProcessingSettingsDialog", "Mode:"))
        self.flipXAxisButton.setText(_translate("ImageProcessingSettingsDialog", "X-axis"))
        self.flipYAxisButton.setText(_translate("ImageProcessingSettingsDialog", "Y-axis"))
        self.flipBothAxesButton.setText(_translate("ImageProcessingSettingsDialog", "Kedua axis"))
        self.resetFlipToDefaultsButton.setText(_translate("ImageProcessingSettingsDialog", "Reset ke Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flipTab_5), _translate("ImageProcessingSettingsDialog", "Flip"))
        self.label_79.setText(_translate("ImageProcessingSettingsDialog", "Threshold 1:"))
        self.label_80.setText(_translate("ImageProcessingSettingsDialog", "[0-999]"))
        self.label_81.setText(_translate("ImageProcessingSettingsDialog", "Threshold 2:"))
        self.label_82.setText(_translate("ImageProcessingSettingsDialog", "[0-999]"))
        self.label_83.setText(_translate("ImageProcessingSettingsDialog", "Aperture:"))
        self.label_84.setText(_translate("ImageProcessingSettingsDialog", "[3/5/7]"))
        self.cannyL2NormCheckBox.setText(_translate("ImageProcessingSettingsDialog", "Gunakan L2-norm"))
        self.resetCannyToDefaultsButton.setText(_translate("ImageProcessingSettingsDialog", "Reset ke Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cannyTab_5), _translate("ImageProcessingSettingsDialog", "Canny"))
        self.applyButton.setText(_translate("ImageProcessingSettingsDialog", "Terapkan"))
        self.resetAllToDefaultsButton.setText(_translate("ImageProcessingSettingsDialog", "Reset Semua ke Default"))

