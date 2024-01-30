import rsa
import sys
import os
import wmi
import math
import pyperclip
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui_core import Ui_core
product = 'slfy'


class Notification(QMainWindow, Ui_core):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.session_paste.clicked.connect(self.paste_to_session)
        self.identify_copy.clicked.connect(self.copy_from_identify)
        self.activate_paste.clicked.connect(self.paste_to_activate)
        self.session.textChanged.connect(self.status_update)
        if os.path.isfile(f'%appdata%/ShenLong/{product}.pem'):
            # 使用客户端生成的私钥解密
            license, pem = open(f'%appdata%/ShenLong/{product}.license'), rsa.PrivateKey.load_pkcs1(
                open(f'%appdata%/ShenLong/{product}.pem'))
            license = str(rsa.decrypt(license, pem)).split('\n')

        else:
            print('invalid license, generating key set')
            self.pu, self.pr = rsa.newkeys(1024)
            temp = wmi.WMI()
            # bios system cpu disk
            self.info = '~~~'.join([temp.Win32_BIOS()[0].SerialNumber,
                           temp.Win32_OperatingSystem()[0].SerialNumber,
                           temp.Win32_Processor()[0].ProcessorId,
                           temp.Win32_DiskDrive()[0].SerialNumber])
            self.show()

    def paste_to_session(self):
        self.session.setText(pyperclip.paste())

    def copy_from_identify(self):
        pyperclip.copy(self.identify.text())

    def paste_to_activate(self):
        self.activate.setText(pyperclip.paste())

    def status_update(self):
        self.identify.setEnabled(bool(self.session.text()))
        self.identify_copy.setEnabled(bool(self.session.text()))
        self.activate.setEnabled(bool(self.session.text()))
        self.activate_paste.setEnabled(bool(self.session.text()))
        if len(self.session.text())==309:
            print('generating identification')
            message,key=f'{self.info}~~~{self.pu.n}',rsa.PublicKey(int(self.session.text()),65537)
            # print(rsa.encrypt(message[:50].encode('utf-8'),key))
            # message=[rsa.encrypt(message[i:i+50].encode('utf-8'),key) for i in range(math.ceil(len(message)/50))]
            print()
            # self.identify.setText(message)
            print(message)
        

         


app = QApplication(sys.argv)
notification = Notification()
sys.exit(app.exec())
