from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QFont, QPalette)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QListWidget, QPushButton, QSizePolicy, QAbstractSpinBox, QDateEdit, QScrollArea,
    QStatusBar, QVBoxLayout, QWidget, QLayout, QSlider, QDialogButtonBox, QTabWidget, QListView, QLineEdit, QDateTimeEdit, QRadioButton, QSpacerItem)

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
        self.topLeftFrame.setAcceptDrops(False)
        self.topLeftFrame.setAutoFillBackground(False)
        self.topLeftFrame.setFrameShape(QFrame.Panel)
        self.topLeftFrame.setFrameShadow(QFrame.Sunken)
        self.topLeftFrame.setLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.topLeftFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.VideoWidget = QLabel(self.topLeftFrame)
        self.VideoWidget.setObjectName(u"VideoWidget")
        self.VideoWidget.setAutoFillBackground(False)
        self.VideoWidget.setStyleSheet(u"border: none;")
        self.VideoWidget.setFrameShape(QFrame.NoFrame)
        self.VideoWidget.setLineWidth(1)
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
        font1.setFamilies([u"Century Schoolbook"])
        font1.setPointSize(28)
        font1.setBold(True)
        self.LitterEyeTitle.setFont(font1)
        self.LitterEyeTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LitterEyeTitle)


        self.verticalLayout_2.addWidget(self.rightFirstFrame)

        self.rightSecondFrame = QFrame(self.rightFrame)
        self.rightSecondFrame.setObjectName(u"rightSecondFrame")
        self.rightSecondFrame.setAutoFillBackground(False)
        self.rightSecondFrame.setFrameShape(QFrame.Panel)
        self.rightSecondFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.rightSecondFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.totalObjectsDetectedTitle = QLabel(self.rightSecondFrame)
        self.totalObjectsDetectedTitle.setObjectName(u"totalObjectsDetectedTitle")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.totalObjectsDetectedTitle.setFont(font2)
        self.totalObjectsDetectedTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.totalObjectsDetectedTitle)

        self.totalObjectsDetectedNumber = QLabel(self.rightSecondFrame)
        self.totalObjectsDetectedNumber.setObjectName(u"totalObjectsDetectedNumber")
        font3 = QFont()
        font3.setPointSize(48)
        font3.setBold(False)
        self.totalObjectsDetectedNumber.setFont(font3)
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
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.detectedObjectsTitle.setFont(font4)
        self.detectedObjectsTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.detectedObjectsTitle)

        self.listWidget = QListWidget(self.rightThirdFrame)
        self.listWidget.setObjectName(u"listWidget")
        font5 = QFont()
        font5.setPointSize(12)
        self.listWidget.setFont(font5)

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
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.CameraSettingsLabel.setFont(font6)
        self.CameraSettingsLabel.setScaledContents(False)
        self.CameraSettingsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.CameraSettingsLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.CameraSourceLabel = QLabel(self.rightFourthFrame)
        self.CameraSourceLabel.setObjectName(u"CameraSourceLabel")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(False)
        self.CameraSourceLabel.setFont(font7)

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
        font8 = QFont()
        font8.setPointSize(26)
        font8.setBold(True)
        self.SummaryReportLabel.setFont(font8)

        self.verticalLayout_7.addWidget(self.SummaryReportLabel)

        self.topFrameLayout = QHBoxLayout()
        self.topFrameLayout.setObjectName(u"topFrameLayout")
        self.topFrameLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.topFrameLeftLayout_2 = QHBoxLayout()
        self.topFrameLeftLayout_2.setSpacing(5)
        self.topFrameLeftLayout_2.setObjectName(u"topFrameLeftLayout_2")
        self.topFrameLeftLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.topFrameLeftLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.dailyRadioButton = QRadioButton(self.topFrame)
        self.dailyRadioButton.setObjectName(u"dailyRadioButton")
        font9 = QFont()
        font9.setPointSize(11)
        self.dailyRadioButton.setFont(font9)
        self.dailyRadioButton.setChecked(True)

        self.topFrameLeftLayout_2.addWidget(self.dailyRadioButton)

        self.hourlyRadioButton = QRadioButton(self.topFrame)
        self.hourlyRadioButton.setObjectName(u"hourlyRadioButton")
        self.hourlyRadioButton.setFont(font9)

        self.topFrameLeftLayout_2.addWidget(self.hourlyRadioButton)

        self.fromDateEdit = QDateEdit(self.topFrame)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        sizePolicy.setHeightForWidth(self.fromDateEdit.sizePolicy().hasHeightForWidth())
        self.fromDateEdit.setSizePolicy(sizePolicy)
        self.fromDateEdit.setMinimumSize(QSize(0, 0))
        self.fromDateEdit.setFont(font9)
        self.fromDateEdit.setLayoutDirection(Qt.LeftToRight)
        self.fromDateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.fromDateEdit.setCurrentSection(QDateTimeEdit.MonthSection)
        self.fromDateEdit.setCalendarPopup(True)

        self.topFrameLeftLayout_2.addWidget(self.fromDateEdit)

        self.dateEditMinusLabel = QLabel(self.topFrame)
        self.dateEditMinusLabel.setObjectName(u"dateEditMinusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateEditMinusLabel.sizePolicy().hasHeightForWidth())
        self.dateEditMinusLabel.setSizePolicy(sizePolicy1)
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        self.dateEditMinusLabel.setFont(font10)
        self.dateEditMinusLabel.setAlignment(Qt.AlignCenter)

        self.topFrameLeftLayout_2.addWidget(self.dateEditMinusLabel)

        self.toDateEdit = QDateEdit(self.topFrame)
        self.toDateEdit.setObjectName(u"toDateEdit")
        sizePolicy.setHeightForWidth(self.toDateEdit.sizePolicy().hasHeightForWidth())
        self.toDateEdit.setSizePolicy(sizePolicy)
        self.toDateEdit.setFont(font9)
        self.toDateEdit.setCalendarPopup(True)

        self.topFrameLeftLayout_2.addWidget(self.toDateEdit)

        self.filterButton = QPushButton(self.topFrame)
        self.filterButton.setObjectName(u"filterButton")
        sizePolicy1.setHeightForWidth(self.filterButton.sizePolicy().hasHeightForWidth())
        self.filterButton.setSizePolicy(sizePolicy1)
        self.filterButton.setFont(font9)

        self.topFrameLeftLayout_2.addWidget(self.filterButton)

        self.topFrameLeftLayout_2.setStretch(0, 1)
        self.topFrameLeftLayout_2.setStretch(1, 1)
        self.topFrameLeftLayout_2.setStretch(2, 1)
        self.topFrameLeftLayout_2.setStretch(3, 1)
        self.topFrameLeftLayout_2.setStretch(4, 1)
        self.topFrameLeftLayout_2.setStretch(5, 1)

        self.topFrameLayout.addLayout(self.topFrameLeftLayout_2)

        self.topFrameRightLayout = QHBoxLayout()
        self.topFrameRightLayout.setObjectName(u"topFrameRightLayout")
        self.topFrameRightLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topFrameRightLayout.addItem(self.horizontalSpacer)

        self.downloadReportButton = QPushButton(self.topFrame)
        self.downloadReportButton.setObjectName(u"downloadReportButton")
        sizePolicy.setHeightForWidth(self.downloadReportButton.sizePolicy().hasHeightForWidth())
        self.downloadReportButton.setSizePolicy(sizePolicy)
        self.downloadReportButton.setLayoutDirection(Qt.LeftToRight)

        self.topFrameRightLayout.addWidget(self.downloadReportButton)


        self.topFrameLayout.addLayout(self.topFrameRightLayout)

        self.topFrameLayout.setStretch(0, 4)
        self.topFrameLayout.setStretch(1, 6)

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
        self.label.setFont(font10)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.label)

        self.totalDetectedLitterLabel = QLabel(self.centerLeftFrame)
        self.totalDetectedLitterLabel.setObjectName(u"totalDetectedLitterLabel")
        font11 = QFont()
        font11.setPointSize(18)
        font11.setBold(False)
        self.totalDetectedLitterLabel.setFont(font11)
        self.totalDetectedLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.totalDetectedLitterLabel)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.centerLeftFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font10)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)

        self.verticalLayout_9.addWidget(self.label_3)

        self.averageDailyDetectedLitterLabel = QLabel(self.centerLeftFrame)
        self.averageDailyDetectedLitterLabel.setObjectName(u"averageDailyDetectedLitterLabel")
        self.averageDailyDetectedLitterLabel.setFont(font11)
        self.averageDailyDetectedLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.averageDailyDetectedLitterLabel)

        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.centerLeftFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font10)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(False)

        self.verticalLayout_10.addWidget(self.label_4)

        self.totalRecyclableLitterLabel = QLabel(self.centerLeftFrame)
        self.totalRecyclableLitterLabel.setObjectName(u"totalRecyclableLitterLabel")
        self.totalRecyclableLitterLabel.setFont(font11)
        self.totalRecyclableLitterLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.totalRecyclableLitterLabel)

        self.verticalLayout_10.setStretch(0, 2)
        self.verticalLayout_10.setStretch(1, 8)

        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.centerLeftFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font10)
        self.label_6.setLineWidth(1)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(False)

        self.verticalLayout_11.addWidget(self.label_6)

        self.totalNonRecyclableLitterLabel = QLabel(self.centerLeftFrame)
        self.totalNonRecyclableLitterLabel.setObjectName(u"totalNonRecyclableLitterLabel")
        self.totalNonRecyclableLitterLabel.setFont(font11)
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
        self.label_9.setFont(font10)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9)

        self.recyclableLitterListWidget = QListWidget(self.centerCenterFrame)
        self.recyclableLitterListWidget.setObjectName(u"recyclableLitterListWidget")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI Light"])
        font12.setPointSize(12)
        self.recyclableLitterListWidget.setFont(font12)
        self.recyclableLitterListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recyclableLitterListWidget.setProperty("isWrapping", False)
        self.recyclableLitterListWidget.setLayoutMode(QListView.SinglePass)
        self.recyclableLitterListWidget.setModelColumn(0)
        self.recyclableLitterListWidget.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.recyclableLitterListWidget)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 9)

        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.centerCenterFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font10)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)

        self.nonRecyclableLitterListWidget = QListWidget(self.centerCenterFrame)
        self.nonRecyclableLitterListWidget.setObjectName(u"nonRecyclableLitterListWidget")
        self.nonRecyclableLitterListWidget.setFont(font12)
        self.nonRecyclableLitterListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.nonRecyclableLitterListWidget.setProperty("isWrapping", False)
        self.nonRecyclableLitterListWidget.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.nonRecyclableLitterListWidget)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 9)

        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.centerCenterFrame)

        self.lineChartFrame = QFrame(self.centerFrame)
        self.lineChartFrame.setObjectName(u"lineChartFrame")
        self.lineChartFrame.setFrameShape(QFrame.Panel)
        self.lineChartFrame.setFrameShadow(QFrame.Sunken)
        self.lineChartFrame.setLineWidth(1)
        self.lineChartGridLayout = QGridLayout(self.lineChartFrame)
        self.lineChartGridLayout.setObjectName(u"lineChartGridLayout")
        self.lineChartGridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.lineChartFrame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 6)

        self.verticalLayout_6.addWidget(self.centerFrame)

        self.bottomFrame = QFrame(self.reportTab)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.barChartFrame = QFrame(self.bottomFrame)
        self.barChartFrame.setObjectName(u"barChartFrame")
        self.barChartFrame.setFrameShape(QFrame.Panel)
        self.barChartFrame.setFrameShadow(QFrame.Sunken)
        self.barChartGridLayout = QGridLayout(self.barChartFrame)
        self.barChartGridLayout.setObjectName(u"barChartGridLayout")
        self.barChartGridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.barChartFrame)

        self.pieChartFrame = QFrame(self.bottomFrame)
        self.pieChartFrame.setObjectName(u"pieChartFrame")
        self.pieChartFrame.setFrameShape(QFrame.Panel)
        self.pieChartFrame.setFrameShadow(QFrame.Sunken)
        self.pieChartGridLayout = QGridLayout(self.pieChartFrame)
        self.pieChartGridLayout.setObjectName(u"pieChartGridLayout")
        self.pieChartGridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.pieChartFrame)


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
        self.LitterEyeTitle.setText(QCoreApplication.translate("MainWindow", u"LitterEye", None))
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
        self.dailyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Daily", None))
        self.hourlyRadioButton.setText(QCoreApplication.translate("MainWindow", u"Hourly", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportTab), QCoreApplication.translate("MainWindow", u"Report", None))
    # retranslateUi

class Ui_settingsDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Advanced Settings")
        Dialog.resize(250, 250)
        Dialog.setMinimumSize(QSize(250, 250))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AIModelLabel = QLabel(self.frame)
        self.AIModelLabel.setObjectName(u"AIModelLabel")
        font = QFont()
        font.setBold(True)
        self.AIModelLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.AIModelLabel)

        self.AIModelComboBox = QComboBox(self.frame)
        self.AIModelComboBox.setObjectName(u"AIModelComboBox")

        self.verticalLayout_2.addWidget(self.AIModelComboBox)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ConfidenceThresholdLabel = QLabel(self.frame_2)
        self.ConfidenceThresholdLabel.setObjectName(u"ConfidenceThresholdLabel")
        self.ConfidenceThresholdLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.ConfidenceThresholdLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ConfidenceThresholdHorizontalSlider = QSlider(self.frame_2)
        self.ConfidenceThresholdHorizontalSlider.setObjectName(u"ConfidenceThresholdHorizontalSlider")
        self.ConfidenceThresholdHorizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.ConfidenceThresholdHorizontalSlider)

        self.ConfidenceThresholdNumber = QLabel(self.frame_2)
        self.ConfidenceThresholdNumber.setObjectName(u"ConfidenceThresholdNumber")

        self.horizontalLayout.addWidget(self.ConfidenceThresholdNumber)

        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.IoUThresholdLabel = QLabel(self.frame_2)
        self.IoUThresholdLabel.setObjectName(u"IoUThresholdLabel")
        self.IoUThresholdLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.IoUThresholdLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.IoUThresholdHorizontalSlider = QSlider(self.frame_2)
        self.IoUThresholdHorizontalSlider.setObjectName(u"IoUThresholdHorizontalSlider")
        self.IoUThresholdHorizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.IoUThresholdHorizontalSlider)

        self.IoUThresholdNumber = QLabel(self.frame_2)
        self.IoUThresholdNumber.setObjectName(u"IoUThresholdNumber")
        self.IoUThresholdNumber.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.IoUThresholdNumber.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.IoUThresholdNumber)

        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 3)

        self.verticalLayout.addWidget(self.frame_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(170, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(212, 212, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(85, 85, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(113, 113, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(212, 212, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.buttonBox.setPalette(palette)
        self.buttonBox.setAcceptDrops(False)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Advanced Settings", u"Advanced Settings", None))
        self.AIModelLabel.setText(QCoreApplication.translate("Advanced Settings", u"AI Model", None))
        self.ConfidenceThresholdLabel.setText(QCoreApplication.translate("Advanced Settings", u"Confidence Threshold", None))
        self.ConfidenceThresholdNumber.setText(QCoreApplication.translate("Advanced Settings", u"0", None))
        self.IoUThresholdLabel.setText(QCoreApplication.translate("Advanced Settings", u"IoU Threshold", None))
        self.IoUThresholdNumber.setText(QCoreApplication.translate("Advanced Settings", u"0", None))
    
class Ui_setAlertDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Set Alert")
        Dialog.resize(250, 250)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.addButton = QPushButton(self.frame)
        self.addButton.setObjectName(u"addButton")
        font1 = QFont()
        font1.setBold(True)
        self.addButton.setFont(font1)

        self.gridLayout.addWidget(self.addButton, 1, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setColumnStretch(0, 8)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 228, 159))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)

        self.retranslateUi(Dialog)

        self.addButton.clicked.connect(self.add_row)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Class", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"Add", None))

    def add_row(self, item_name=None, amount=None):
        if item_name is None:
            item_name = self.comboBox.currentText()
        if amount is None:
            amount = self.lineEdit.text()     

        if item_name and amount:
            new_horizontal_layout = QHBoxLayout()
            new_horizontal_layout.setObjectName("horizontalLayout_" + item_name) 

            label_item = QLabel(self.scrollAreaWidgetContents)
            label_item.setObjectName("className_" + item_name) 
            label_item.setText(item_name)
            new_horizontal_layout.addWidget(label_item)

            label_amount = QLabel(self.scrollAreaWidgetContents)
            label_amount.setObjectName("alertAmount_" + item_name)
            label_amount.setText(str(amount))
            new_horizontal_layout.addWidget(label_amount)

            button_remove = QPushButton(self.scrollAreaWidgetContents)
            button_remove.setObjectName("removeButton_" + item_name) 
            button_remove.setText("Remove")
            button_remove.setFont(QFont('Arial', pointSize=9, weight=QFont.Bold))
            button_remove.clicked.connect(lambda: self.remove_row(new_horizontal_layout, item_name))
            new_horizontal_layout.addWidget(button_remove)

            new_horizontal_layout.setStretch(0, 8)
            new_horizontal_layout.setStretch(1, 1)
            new_horizontal_layout.setStretch(2, 1)

            print("UI.PY")
            self.save_to_database(item_name, amount)

            if item_name == self.comboBox.currentText(): # removes selected option in drop down list
                self.comboBox.removeItem(self.comboBox.findText(item_name))

            self.verticalLayout_2.addLayout(new_horizontal_layout)
            self.lineEdit.clear()

    def remove_row(self, layout, item_name):
        # Add the removed item back to the drop-down list
        self.comboBox.addItem(item_name)

        # Sort the items in the comboBox alphabetically
        self.comboBox.model().sort(0)

        self.remove_from_database(item_name)

        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            else:
                self.remove_row(item.layout(), item_name)
        self.verticalLayout_2.removeItem(layout)
        layout.deleteLater()