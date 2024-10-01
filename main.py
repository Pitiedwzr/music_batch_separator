import sys
from UI_mainWindow import Ui_MainWindow
from UI_settingsDialog import Ui_SettingsDialog
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
from settings import config


class MainWindow(QMainWindow):
    def __init__(self):
        """Inital the UI and functions"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSlot()

    def initSlot(self):
        self.ui.actionAbout_Qt.triggered.connect(self.showAboutQt)
        self.ui.actionPreferences.triggered.connect(self.jumpToSettings)
        
    def showAboutQt(self):
        QApplication.aboutQt()
        
    def jumpToSettings(self):
        settings_dialog.show()

class SettingsDialog(QDialog):
    def __init__(self):
        """Inital the UI and functions"""
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.initSlot()
        
    def initSlot(self):
        self.ui.pushButtonSave.clicked.connect(self.saveSettings)
        self.ui.pushButtonCancel.clicked.connect(self.exitSettings)
        self.ui.comboBoxOutputFormat.setCurrentIndex(config.common.output_format)
        self.ui.checkBoxIsDemo.setChecked(config.common.is_demo)

    def saveSettings(self):
        config.common.output_format = self.ui.comboBoxOutputFormat.currentIndex()
        config.common.is_demo = self.ui.checkBoxIsDemo.isChecked()
        config.save()
        
    def exitSettings(self):
        settings_dialog.hide()

# Main program running
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon("./Resource/images/icon.ico"))
    app.setStyle("fusion")

    # Inital all windows
    main_window = MainWindow()
    settings_dialog = SettingsDialog()
    
    main_window.show()
    
    sys.exit(app.exec())