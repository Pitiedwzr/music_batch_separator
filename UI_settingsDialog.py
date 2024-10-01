# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 315)
        self.groupBoxCommon = QGroupBox(Dialog)
        self.groupBoxCommon.setObjectName(u"groupBoxCommon")
        self.groupBoxCommon.setGeometry(QRect(10, 10, 400, 130))
        self.labelOutputformat = QLabel(self.groupBoxCommon)
        self.labelOutputformat.setObjectName(u"labelOutputformat")
        self.labelOutputformat.setGeometry(QRect(10, 20, 141, 22))
        self.comboBoxOutputFormat = QComboBox(self.groupBoxCommon)
        self.comboBoxOutputFormat.addItem("")
        self.comboBoxOutputFormat.addItem("")
        self.comboBoxOutputFormat.addItem("")
        self.comboBoxOutputFormat.addItem("")
        self.comboBoxOutputFormat.setObjectName(u"comboBoxOutputFormat")
        self.comboBoxOutputFormat.setGeometry(QRect(149, 20, 241, 22))
        self.checkBoxIsDemo = QCheckBox(self.groupBoxCommon)
        self.checkBoxIsDemo.setObjectName(u"checkBoxIsDemo")
        self.checkBoxIsDemo.setGeometry(QRect(150, 50, 111, 21))
        self.labelIsDemo = QLabel(self.groupBoxCommon)
        self.labelIsDemo.setObjectName(u"labelIsDemo")
        self.labelIsDemo.setGeometry(QRect(10, 50, 141, 22))
        self.groupBoxSecert = QGroupBox(Dialog)
        self.groupBoxSecert.setObjectName(u"groupBoxSecert")
        self.groupBoxSecert.setGeometry(QRect(10, 140, 400, 110))
        self.labelAPI = QLabel(self.groupBoxSecert)
        self.labelAPI.setObjectName(u"labelAPI")
        self.labelAPI.setGeometry(QRect(10, 20, 91, 22))
        self.lineEditAPI = QLineEdit(self.groupBoxSecert)
        self.lineEditAPI.setObjectName(u"lineEditAPI")
        self.lineEditAPI.setGeometry(QRect(150, 20, 241, 22))
        self.pushButtonSave = QPushButton(Dialog)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(90, 270, 91, 24))
        self.pushButtonCancel = QPushButton(Dialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setGeometry(QRect(240, 270, 91, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.groupBoxCommon.setTitle(QCoreApplication.translate("Dialog", u"Common", None))
        self.labelOutputformat.setText(QCoreApplication.translate("Dialog", u"Output format", None))
        self.comboBoxOutputFormat.setItemText(0, QCoreApplication.translate("Dialog", u"mp3 (320 kbps)", None))
        self.comboBoxOutputFormat.setItemText(1, QCoreApplication.translate("Dialog", u"wav (uncompressed)", None))
        self.comboBoxOutputFormat.setItemText(2, QCoreApplication.translate("Dialog", u"flac (lossless)", None))
        self.comboBoxOutputFormat.setItemText(3, QCoreApplication.translate("Dialog", u"m4a (lossy)", None))

        self.checkBoxIsDemo.setText("")
        self.labelIsDemo.setText(QCoreApplication.translate("Dialog", u"Put on demo page", None))
        self.groupBoxSecert.setTitle(QCoreApplication.translate("Dialog", u"Secert", None))
        self.labelAPI.setText(QCoreApplication.translate("Dialog", u"API token", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

