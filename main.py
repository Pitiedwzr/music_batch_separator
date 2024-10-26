import sys
from UI_mainWindow import Ui_MainWindow
from UI_settingsDialog import Ui_SettingsDialog
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QListWidgetItem
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
from settings import config
from file import InputFile
import api


class MainWindow(QMainWindow):
    """Inital the UI and functions"""
    def __init__(self):
        """Inital the UI and functions"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSlot()

    def initSlot(self):
        """Initial all slots"""
        self.ui.actionAbout_Qt.triggered.connect(self.showAboutQt)
        self.ui.actionPreferences.triggered.connect(self.jumpToSettings)
        self.ui.pushButtonProcess.clicked.connect(self.sendRequest)
        self.ui.listWidgetInput.setAcceptDrops(True)
        self.ui.listWidgetInput.dragEnterEvent = self.dragEnterEvent
        self.ui.listWidgetInput.dropEvent = self.dropEvent
        
    def showAboutQt(self):
        QApplication.aboutQt()
        
    def jumpToSettings(self):
        settings_dialog.show()
     
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                file_path = url.toLocalFile()
                item = QListWidgetItem(file_path)
                self.ui.listWidgetInput.addItem(item)
            event.accept()
        else:
            event.ignore()
            
    def sendRequest(self):
        audio_file_path = self.ui.listWidgetInput.currentItem().text()
        api.createRequest()

class SettingsDialog(QDialog):
    """Inital the UI and functions"""
    def __init__(self):
        """Inital the UI and functions"""
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.initSlot()
        
    def initSlot(self):
        """Initial all slots"""
        self.ui.pushButtonSave.clicked.connect(self.saveSettings)
        self.ui.pushButtonCancel.clicked.connect(self.exitSettings)
        self.ui.comboBoxOutputFormat.setCurrentIndex(config.common.output_format)
        self.ui.checkBoxIsDemo.setChecked(bool(config.common.is_demo))

    def saveSettings(self):
        config.common.output_format = self.ui.comboBoxOutputFormat.currentIndex()
        config.common.is_demo = int(self.ui.checkBoxIsDemo.isChecked())
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