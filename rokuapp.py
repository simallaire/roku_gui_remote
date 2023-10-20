import requests

from PyQt6.QtWidgets import QDialog, QMainWindow, QPushButton
from remote import Ui_Dialog

class RokuApp():
    def __init__(self, ip):
        self.Dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        self.baseAddr = "http://" + ip
        self.ui.pushButtonOff.clicked.connect(self.btnOff_clicked)
        self.ui.pushButtonOn.clicked.connect(self.btnOn_clicked)
        self.ui.pushButtonUp.clicked.connect(self.btnUp_clicked)
        self.ui.pushButtonDown.clicked.connect(self.btnDown_clicked)
        self.ui.pushButtonLeft.clicked.connect(self.btnLeft_clicked)
        self.ui.pushButtonRight.clicked.connect(self.btnRight_clicked)
        self.ui.pushButtonHome.clicked.connect(self.btnHome_clicked)
        self.ui.pushButtonOk.clicked.connect(self.btnOk_clicker)
        self.ui.pushButtonBack.clicked.connect(self.btnBack_clicked)
        self.ui.pushButtonVolUp.clicked.connect(self.btnVolUp_clicked)
        self.ui.pushButtonVolDown.clicked.connect(self.btnVolDown_clicked)
        self.ui.pushButtonPause.clicked.connect(self.btnPause_clicked)
        self.ui.pushButtonPlay.clicked.connect(self.btnPlay_clicked)
        print(requests.get(f"{self.baseAddr}/query/device-info").text)
        
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
    
    def btnOk_clicker(self):
        requests.post(f"{self.baseAddr}/keypress/select", "")
        
    def btnVolUp_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/VolumeUp", "")
        
    def btnVolDown_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/VolumeDown", "")
    
    def btnBack_clicked(self):
        requests.post(f"{self.baseAddr}/keypress/back", "")
    