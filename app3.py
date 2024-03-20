# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QSize(1366, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.detectTab = QWidget()
        self.detectTab.setObjectName(u"detectTab")
        self.gridLayout_3 = QGridLayout(self.detectTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.wholeWindowLayout = QHBoxLayout()
        self.wholeWindowLayout.setObjectName(u"wholeWindowLayout")
        self.wholeWindowLayout.setContentsMargins(1, 1, 1, 1)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setObjectName(u"leftLayout")
        self.topLeftFrame = QFrame(self.detectTab)
        self.topLeftFrame.setObjectName(u"topLeftFrame")
        self.topLeftFrame.setFrameShape(QFrame.Panel)
        self.topLeftFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.topLeftFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.VideoWidget = QLabel(self.topLeftFrame)
        self.VideoWidget.setObjectName(u"VideoWidget")
        self.VideoWidget.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.VideoWidget, 0, 2, 1, 1)


        self.leftLayout.addWidget(self.topLeftFrame)


        self.wholeWindowLayout.addLayout(self.leftLayout)

        self.rightFrame = QFrame(self.detectTab)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.NoFrame)
        self.rightFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rightFirstFrame = QFrame(self.rightFrame)
        self.rightFirstFrame.setObjectName(u"rightFirstFrame")
        self.rightFirstFrame.setFrameShape(QFrame.Panel)
        self.rightFirstFrame.setFrameShadow(QFrame.Raised)
        self.rightFirstFrame.setLineWidth(3)
        self.verticalLayout = QVBoxLayout(self.rightFirstFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LitterEyeTitle = QLabel(self.rightFirstFrame)
        self.LitterEyeTitle.setObjectName(u"LitterEyeTitle")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.LitterEyeTitle.setFont(font1)
        self.LitterEyeTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LitterEyeTitle)


        self.verticalLayout_2.addWidget(self.rightFirstFrame)

        self.rightSecondFrame = QFrame(self.rightFrame)
        self.rightSecondFrame.setObjectName(u"rightSecondFrame")
        self.rightSecondFrame.setFrameShape(QFrame.Panel)
        self.rightSecondFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.rightSecondFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.totalObjectsDetectedTitle = QLabel(self.rightSecondFrame)
        self.totalObjectsDetectedTitle.setObjectName(u"totalObjectsDetectedTitle")
        self.totalObjectsDetectedTitle.setFont(font1)
        self.totalObjectsDetectedTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.totalObjectsDetectedTitle)

        self.totalObjectsDetectedNumber = QLabel(self.rightSecondFrame)
        self.totalObjectsDetectedNumber.setObjectName(u"totalObjectsDetectedNumber")
        font2 = QFont()
        font2.setPointSize(36)
        font2.setBold(False)
        self.totalObjectsDetectedNumber.setFont(font2)
        self.totalObjectsDetectedNumber.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.totalObjectsDetectedNumber)


        self.verticalLayout_2.addWidget(self.rightSecondFrame)

        self.rightThirdFrame = QFrame(self.rightFrame)
        self.rightThirdFrame.setObjectName(u"rightThirdFrame")
        self.rightThirdFrame.setFrameShape(QFrame.Panel)
        self.rightThirdFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.rightThirdFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.detectedObjectsTitle = QLabel(self.rightThirdFrame)
        self.detectedObjectsTitle.setObjectName(u"detectedObjectsTitle")
        self.detectedObjectsTitle.setFont(font1)
        self.detectedObjectsTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.detectedObjectsTitle)

        self.listWidget = QListWidget(self.rightThirdFrame)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_4.addWidget(self.listWidget)


        self.verticalLayout_2.addWidget(self.rightThirdFrame)

        self.rightFourthFrame = QFrame(self.rightFrame)
        self.rightFourthFrame.setObjectName(u"rightFourthFrame")
        self.rightFourthFrame.setFrameShape(QFrame.Panel)
        self.rightFourthFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_5 = QVBoxLayout(self.rightFourthFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CameraSettingsLabel = QLabel(self.rightFourthFrame)
        self.CameraSettingsLabel.setObjectName(u"CameraSettingsLabel")
        self.CameraSettingsLabel.setFont(font1)
        self.CameraSettingsLabel.setScaledContents(False)
        self.CameraSettingsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.CameraSettingsLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.CameraSourceLabel = QLabel(self.rightFourthFrame)
        self.CameraSourceLabel.setObjectName(u"CameraSourceLabel")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.CameraSourceLabel.setFont(font3)

        self.horizontalLayout_2.addWidget(self.CameraSourceLabel)

        self.CameraSourceComboBox = QComboBox(self.rightFourthFrame)
        self.CameraSourceComboBox.setObjectName(u"CameraSourceComboBox")

        self.horizontalLayout_2.addWidget(self.CameraSourceComboBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.StartRecordButton = QPushButton(self.rightFourthFrame)
        self.StartRecordButton.setObjectName(u"StartRecordButton")

        self.horizontalLayout_5.addWidget(self.StartRecordButton)

        self.SetAlertButton = QPushButton(self.rightFourthFrame)
        self.SetAlertButton.setObjectName(u"SetAlertButton")

        self.horizontalLayout_5.addWidget(self.SetAlertButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.advancedSettingsButton = QPushButton(self.rightFourthFrame)
        self.advancedSettingsButton.setObjectName(u"advancedSettingsButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedSettingsButton.sizePolicy().hasHeightForWidth())
        self.advancedSettingsButton.setSizePolicy(sizePolicy)
        self.advancedSettingsButton.setAutoFillBackground(False)
        self.advancedSettingsButton.setAutoDefault(False)
        self.advancedSettingsButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.advancedSettingsButton)


        self.verticalLayout_2.addWidget(self.rightFourthFrame)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 5)

        self.wholeWindowLayout.addWidget(self.rightFrame)

        self.wholeWindowLayout.setStretch(0, 9)
        self.wholeWindowLayout.setStretch(1, 1)

        self.gridLayout_3.addLayout(self.wholeWindowLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.detectTab, "")
        self.reportTab = QWidget()
        self.reportTab.setObjectName(u"reportTab")
        self.verticalLayout_6 = QVBoxLayout(self.reportTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.topFrame = QFrame(self.reportTab)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.Panel)
        self.topFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_7 = QVBoxLayout(self.topFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.SummaryReportLabel = QLabel(self.topFrame)
        self.SummaryReportLabel.setObjectName(u"SummaryReportLabel")
        font4 = QFont()
        font4.setPointSize(26)
        font4.setBold(True)
        self.SummaryReportLabel.setFont(font4)

        self.verticalLayout_7.addWidget(self.SummaryReportLabel)

        self.topFrameLayout = QHBoxLayout()
        self.topFrameLayout.setObjectName(u"topFrameLayout")
        self.topFrameLeftLayout_2 = QHBoxLayout()
        self.topFrameLeftLayout_2.setSpacing(5)
        self.topFrameLeftLayout_2.setObjectName(u"topFrameLeftLayout_2")
        self.topFrameLeftLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.topFrameLeftLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.fromDateEdit = QDateEdit(self.topFrame)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        sizePolicy.setHeightForWidth(self.fromDateEdit.sizePolicy().hasHeightForWidth())
        self.fromDateEdit.setSizePolicy(sizePolicy)
        self.fromDateEdit.setMinimumSize(QSize(0, 0))
        self.fromDateEdit.setLayoutDirection(Qt.LeftToRight)
        self.fromDateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.fromDateEdit.setCalendarPopup(True)

        self.topFrameLeftLayout_2.addWidget(self.fromDateEdit)

        self.dateEditMinusLabel = QLabel(self.topFrame)
        self.dateEditMinusLabel.setObjectName(u"dateEditMinusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateEditMinusLabel.sizePolicy().hasHeightForWidth())
        self.dateEditMinusLabel.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.dateEditMinusLabel.setFont(font5)
        self.dateEditMinusLabel.setAlignment(Qt.AlignCenter)

        self.topFrameLeftLayout_2.addWidget(self.dateEditMinusLabel)

        self.toDateEdit = QDateEdit(self.topFrame)
        self.toDateEdit.setObjectName(u"toDateEdit")
        sizePolicy.setHeightForWidth(self.toDateEdit.sizePolicy().hasHeightForWidth())
        self.toDateEdit.setSizePolicy(sizePolicy)
        self.toDateEdit.setCalendarPopup(True)

        self.topFrameLeftLayout_2.addWidget(self.toDateEdit)

        self.filterButton = QPushButton(self.topFrame)
        self.filterButton.setObjectName(u"filterButton")
        sizePolicy1.setHeightForWidth(self.filterButton.sizePolicy().hasHeightForWidth())
        self.filterButton.setSizePolicy(sizePolicy1)

        self.topFrameLeftLayout_2.addWidget(self.filterButton)

        self.topFrameLeftLayout_2.setStretch(0, 1)
        self.topFrameLeftLayout_2.setStretch(1, 1)
        self.topFrameLeftLayout_2.setStretch(2, 1)
        self.topFrameLeftLayout_2.setStretch(3, 1)

        self.topFrameLayout.addLayout(self.topFrameLeftLayout_2)

        self.topFrameRightLayout = QHBoxLayout()
        self.topFrameRightLayout.setObjectName(u"topFrameRightLayout")
        self.downloadReportButton = QPushButton(self.topFrame)
        self.downloadReportButton.setObjectName(u"downloadReportButton")

        self.topFrameRightLayout.addWidget(self.downloadReportButton, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.topFrameLayout.addLayout(self.topFrameRightLayout)

        self.topFrameLayout.setStretch(0, 3)
        self.topFrameLayout.setStretch(1, 7)

        self.verticalLayout_7.addLayout(self.topFrameLayout)

        self.verticalLayout_7.setStretch(0, 7)
        self.verticalLayout_7.setStretch(1, 3)

        self.verticalLayout_6.addWidget(self.topFrame)

        self.centerFrame = QFrame(self.reportTab)
        self.centerFrame.setObjectName(u"centerFrame")
        self.centerFrame.setFrameShape(QFrame.StyledPanel)
        self.centerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.centerFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.centerLeftFrame = QFrame(self.centerFrame)
        self.centerLeftFrame.setObjectName(u"centerLeftFrame")
        self.centerLeftFrame.setFrameShape(QFrame.Panel)
        self.centerLeftFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_12 = QVBoxLayout(self.centerLeftFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.centerLeftFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.totalDetectedLitterLabel = QLabel(self.centerLeftFrame)
        self.totalDetectedLitterLabel.setObjectName(u"totalDetectedLitterLabel")
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(False)
        self.totalDetectedLitterLabel.setFont(font6)
        self.totalDetectedLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.totalDetectedLitterLabel)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.centerLeftFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.averageDailyDetectedLitterLabel = QLabel(self.centerLeftFrame)
        self.averageDailyDetectedLitterLabel.setObjectName(u"averageDailyDetectedLitterLabel")
        self.averageDailyDetectedLitterLabel.setFont(font6)
        self.averageDailyDetectedLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.averageDailyDetectedLitterLabel)

        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.centerLeftFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_4)

        self.totalRecyclableLitterLabel = QLabel(self.centerLeftFrame)
        self.totalRecyclableLitterLabel.setObjectName(u"totalRecyclableLitterLabel")
        self.totalRecyclableLitterLabel.setFont(font6)
        self.totalRecyclableLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.totalRecyclableLitterLabel)

        self.verticalLayout_10.setStretch(0, 2)
        self.verticalLayout_10.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.centerLeftFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.totalNonRecyclableLitterLabel = QLabel(self.centerLeftFrame)
        self.totalNonRecyclableLitterLabel.setObjectName(u"totalNonRecyclableLitterLabel")
        self.totalNonRecyclableLitterLabel.setFont(font6)
        self.totalNonRecyclableLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.totalNonRecyclableLitterLabel)

        self.verticalLayout_11.setStretch(0, 2)
        self.verticalLayout_11.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_12.setStretch(0, 2)
        self.verticalLayout_12.setStretch(1, 2)
        self.verticalLayout_12.setStretch(2, 2)
        self.verticalLayout_12.setStretch(3, 2)

        self.horizontalLayout.addWidget(self.centerLeftFrame)

        self.centerCenterFrame = QFrame(self.centerFrame)
        self.centerCenterFrame.setObjectName(u"centerCenterFrame")
        self.centerCenterFrame.setFrameShape(QFrame.Panel)
        self.centerCenterFrame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_3 = QHBoxLayout(self.centerCenterFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.centerCenterFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9)

        self.recyclableLitterListWidget = QListWidget(self.centerCenterFrame)
        self.recyclableLitterListWidget.setObjectName(u"recyclableLitterListWidget")
        self.recyclableLitterListWidget.setLayoutMode(QListView.SinglePass)
        self.recyclableLitterListWidget.setModelColumn(0)

        self.verticalLayout_13.addWidget(self.recyclableLitterListWidget)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 9)

        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.centerCenterFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)

        self.nonRecyclableLitterListWidget = QListWidget(self.centerCenterFrame)
        self.nonRecyclableLitterListWidget.setObjectName(u"nonRecyclableLitterListWidget")

        self.verticalLayout_14.addWidget(self.nonRecyclableLitterListWidget)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 9)

        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.centerCenterFrame)

        self.centerRightFrame = QFrame(self.centerFrame)
        self.centerRightFrame.setObjectName(u"centerRightFrame")
        self.centerRightFrame.setFrameShape(QFrame.Panel)
        self.centerRightFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_4 = QGridLayout(self.centerRightFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineChart = QLabel(self.centerRightFrame)
        self.lineChart.setObjectName(u"lineChart")

        self.gridLayout_4.addWidget(self.lineChart, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.centerRightFrame)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 4)

        self.verticalLayout_6.addWidget(self.centerFrame)

        self.bottomFrame = QFrame(self.reportTab)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.bottomFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.barChart = QLabel(self.frame)
        self.barChart.setObjectName(u"barChart")

        self.gridLayout_5.addWidget(self.barChart, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.bottomFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pieChart = QLabel(self.frame_2)
        self.pieChart.setObjectName(u"pieChart")

        self.gridLayout_6.addWidget(self.pieChart, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.bottomFrame)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 4)
        self.verticalLayout_6.setStretch(2, 5)
        self.tabWidget.addTab(self.reportTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.advancedSettingsButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.VideoWidget.setText("")
        self.LitterEyeTitle.setText(QCoreApplication.translate("MainWindow", u"LitterEye v1", None))
        self.totalObjectsDetectedTitle.setText(QCoreApplication.translate("MainWindow", u"Total Objects Detected", None))
        self.totalObjectsDetectedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.detectedObjectsTitle.setText(QCoreApplication.translate("MainWindow", u"Detected Objects", None))
        self.CameraSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
        self.CameraSourceLabel.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.StartRecordButton.setText(QCoreApplication.translate("MainWindow", u"Start Record", None))
        self.SetAlertButton.setText(QCoreApplication.translate("MainWindow", u"Set Alert", None))
        self.advancedSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Advanced Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.detectTab), QCoreApplication.translate("MainWindow", u"Detect", None))
        self.SummaryReportLabel.setText(QCoreApplication.translate("MainWindow", u"Summary Report", None))
        self.dateEditMinusLabel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.downloadReportButton.setText(QCoreApplication.translate("MainWindow", u"Download Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Detected Litter", None))
        self.totalDetectedLitterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Average Daily Detected Litter", None))
        self.averageDailyDetectedLitterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Recyclable Litter (%)", None))
        self.totalRecyclableLitterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Non-Recyclable Litter (%)", None))
        self.totalNonRecyclableLitterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Recyclable Litter", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Non-Recyclable Litter", None))
        self.lineChart.setText(QCoreApplication.translate("MainWindow", u"Line Chart showing total detected litter per day on a span of a date", None))
        self.barChart.setText(QCoreApplication.translate("MainWindow", u"Amount of Total Detected Litter per class (Bar chart)", None))
        self.pieChart.setText(QCoreApplication.translate("MainWindow", u"Percentage Distribution of Total Detected Litter per class (Pie chart)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportTab), QCoreApplication.translate("MainWindow", u"Report", None))
    # retranslateUi

