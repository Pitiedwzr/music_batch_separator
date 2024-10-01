# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.NewZealand))
        self.actionAbout_Music_Batch_Separator = QAction(MainWindow)
        self.actionAbout_Music_Batch_Separator.setObjectName(u"actionAbout_Music_Batch_Separator")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionMusic_Batch_Separator_Help = QAction(MainWindow)
        self.actionMusic_Batch_Separator_Help.setObjectName(u"actionMusic_Batch_Separator_Help")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))

        self.verticalLayout_2.addWidget(self.label)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 3, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 67, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 67, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))

        self.verticalLayout_3.addWidget(self.label_2)

        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_3.addWidget(self.listWidget_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 4, 3, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelSepType = QLabel(self.centralwidget)
        self.labelSepType.setObjectName(u"labelSepType")
        self.labelSepType.setMinimumSize(QSize(254, 20))

        self.verticalLayout.addWidget(self.labelSepType)

        self.comboBoxSepType = QComboBox(self.centralwidget)
        self.comboBoxSepType.setObjectName(u"comboBoxSepType")
        self.comboBoxSepType.setMinimumSize(QSize(0, 22))

        self.verticalLayout.addWidget(self.comboBoxSepType)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.labelOpt1 = QLabel(self.centralwidget)
        self.labelOpt1.setObjectName(u"labelOpt1")
        self.labelOpt1.setMinimumSize(QSize(0, 20))

        self.verticalLayout.addWidget(self.labelOpt1)

        self.comboBoxOpt1 = QComboBox(self.centralwidget)
        self.comboBoxOpt1.setObjectName(u"comboBoxOpt1")
        self.comboBoxOpt1.setMinimumSize(QSize(0, 22))

        self.verticalLayout.addWidget(self.comboBoxOpt1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))

        self.verticalLayout.addWidget(self.label_5)

        self.comboBoxOpt2 = QComboBox(self.centralwidget)
        self.comboBoxOpt2.setObjectName(u"comboBoxOpt2")
        self.comboBoxOpt2.setMinimumSize(QSize(0, 22))

        self.verticalLayout.addWidget(self.comboBoxOpt2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 26))

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionMusic_Batch_Separator_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Music_Batch_Separator)
        self.menuHelp.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Batch Separator", None))
        self.actionAbout_Music_Batch_Separator.setText(QCoreApplication.translate("MainWindow", u"About Music Batch Separator", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionMusic_Batch_Separator_Help.setText(QCoreApplication.translate("MainWindow", u"Music Batch Separator Help", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input Files", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.labelSepType.setText(QCoreApplication.translate("MainWindow", u"Separation type", None))
        self.labelOpt1.setText(QCoreApplication.translate("MainWindow", u"opt_1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"opt_2", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

