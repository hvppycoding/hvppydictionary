from typing import Optional
import keyboard

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from hvppydictionary.hotkeylistener import HotkeyListener


class MainWindow(QMainWindow):
    """Main window of the application."""
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.keyboard_listener = HotkeyListener(self)
        self.keyboard_listener.pressed.connect(self.on_pressed)
        self.keyboard_listener.listen("ctrl+shift+D")
        
    def closeEvent(self, event: QCloseEvent) -> None:
        question = QMessageBox.question(self, "Exit", "Run Background?", QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            event.ignore()
            self.hide()
        else:
            # Quit program...
            exit(0)
        
    def on_pressed(self, hotkey: str):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time + " -> " + hotkey)
        self.show()
        self.raise_()
        self.activateWindow()