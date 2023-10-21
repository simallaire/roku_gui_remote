import requests

from pynput import keyboard
from PyQt6.QtWidgets import QDialog, QMainWindow, QPushButton, QWidget
from remote import Ui_Form

class RokuApp():
    def __init__(self, host, kb_listener):
        self.Form = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.baseAddr = "http://" + host
        self.ui.pushButtonOff.clicked.connect(self.btnOff_clicked)
        self.ui.pushButtonOn.clicked.connect(self.btnOn_clicked)
        self.ui.pushButtonUp.clicked.connect(self.btnUp_clicked)
        self.ui.pushButtonDown.clicked.connect(self.btnDown_clicked)
        self.ui.pushButtonLeft.clicked.connect(self.btnLeft_clicked)
        self.ui.pushButtonRight.clicked.connect(self.btnRight_clicked)
        self.ui.pushButtonHome.clicked.connect(self.btnHome_clicked)
        self.ui.pushButtonOk.clicked.connect(self.btnOk_clicked)
        self.ui.pushButtonBack.clicked.connect(self.btnBack_clicked)
        self.ui.pushButtonVolUp.clicked.connect(self.btnVolUp_clicked)
        self.ui.pushButtonVolDown.clicked.connect(self.btnVolDown_clicked)
        self.ui.pushButtonPause.clicked.connect(self.btnPause_clicked)
        self.ui.pushButtonPlay.clicked.connect(self.btnPlay_clicked)
        print(requests.get(f"{self.baseAddr}/query/device-info").content)
        if kb_listener:
            self.listener = keyboard.Listener(on_press=self.onKeyPress)
            self.listener.start()
  
    def onKeyPress(self, key):
        if self.Form.isActiveWindow():
            if key == keyboard.Key.up:
                self.btnUp_clicked()
            elif key == keyboard.Key.down:
                self.btnDown_clicked()  
            elif key == keyboard.Key.left:
                self.btnLeft_clicked()
            elif key == keyboard.Key.right:
                self.btnRight_clicked()
            elif key == keyboard.Key.enter:
                self.btnOk_clicked()
            elif key == keyboard.Key.backspace:
                self.btnBack_clicked()
            elif key == keyboard.Key.space:
                self.btnPlay_clicked()
            else:
                try:
                    self.send_char(key.char)
                except AttributeError:
                    print("Cant resolve key")
                
                
    def send_char(self, char):
        requests.post(f"{self.baseAddr}/keypress/Lit_{char}", "")
        
    def btnPause_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/pause", "")
        
    def btnPlay_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/play", "")
        
    def btnOff_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/powerOff", "")
        
    def btnOn_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/powerOn", "")

    def btnUp_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/up", "")
        
    def btnDown_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/down", "")
        
    def btnLeft_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/left", "")
        
    def btnRight_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/right", "")
        
    def btnHome_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/home", "")
    
    def btnOk_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/select", "")
        
    def btnVolUp_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/VolumeUp", "")
        
    def btnVolDown_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/VolumeDown", "")
    
    def btnBack_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/back", "")
    