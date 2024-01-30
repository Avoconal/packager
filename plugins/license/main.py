from PySide6.QtWidgets import *
from PySide6.QtCore import *

from .license_ui import Ui_license

import time

class License(QWidget,Ui_license):
    def __init__(self,parent:QWidget):
        super().__init__()
        self.setupUi(parent)

        self.checkbox_switch.setOnText('开启授权')
        self.checkbox_switch.setOffText('关闭授权')
        self.checkbox_dark_mode.setOnText('深色模式')
        self.checkbox_dark_mode.setOffText('浅色模式')
        self.dateedit.setDateFormat('yyyy 年 MM 月 dd 日')

        self.signal_connect()

    def signal_connect(self):
        self.checkbox_switch.checkedChanged.connect(
            self.update_encryption_status)

        date = [int(i) for i in time.strftime(r'%Y-%m-%d').split('-')]
        self.dateedit.setDate(QDate(date[0], date[1], date[2]))

    def update_encryption_status(self):
        temp = self.checkbox_switch.isChecked()
        self.checkbox_dark_mode.setEnabled(temp)
        self.lineedit_user.setEnabled(temp)
        self.dateedit.setEnabled(temp)
        self.lineedit_bios_sn.setEnabled(temp)
        self.lineedit_system_sn.setEnabled(temp)
        self.lineedit_disk_sn.setEnabled(temp)
        self.lineedit_link.setEnabled(temp)
