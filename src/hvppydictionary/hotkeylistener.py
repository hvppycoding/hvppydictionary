from typing import Union
from functools import partial
from PySide6.QtCore import QObject, QThread, Signal, Slot
import keyboard

class HotkeyListenerWorker(QObject):
    pressed = Signal(str)
    
    def __init__(self, hotkeys: list[str], parent=None):
        super().__init__(parent)
        self.hotkeys = hotkeys

    def run(self):
        def on_pressed(hotkey: str):
            print(hotkey)
            self.pressed.emit(hotkey)
        
        for hotkey in self.hotkeys:
            print(hotkey)
            keyboard.add_hotkey(hotkey, partial(on_pressed, hotkey=hotkey))
        keyboard.wait()


class HotkeyListener(QObject):
    pressed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hotkeys: list[str] = []
        self.is_running = False
        self.work_thread = None
        self.worker = None
        
    def is_running(self) -> bool:
        return self.is_running
    
    def quit_listening(self) -> None:
        if self.work_thread:
            self.work_thread.kill()
            self.work_thread.wait()
        self.is_running = False
        self.work_thread = None
        self.worker = None
        
    def add_hotkey(self, hotkey: str) -> None:
        self.hotkeys.append(hotkey)
    
    def listen(self, hotkeys: Union[list[str], str, None] = None) -> None:
        if self.is_running:
            print("HotkeyListener is already started.")
            return
        if hotkeys:
            if isinstance(hotkeys, str):
                hotkeys = [hotkeys]
            self.hotkeys += hotkeys
        self.is_running = True
        self.work_thread = QThread()
        self.worker = HotkeyListenerWorker(self.hotkeys)
        self.worker.moveToThread(self.work_thread)
        self.worker.pressed.connect(self.on_pressed)
        self.work_thread.started.connect(self.worker.run)
        self.work_thread.start()
    
    @Slot(str)
    def on_pressed(self, hotkey: str):
        self.pressed.emit(hotkey)
