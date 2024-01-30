import sys
import os
import wmi
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import app.main as Main
name = 'Wv'
product = 'slfy'
version = '1.8'
bios_sn = 'KCN0CV03T592490'
os_sn = '00342-35640-38855-AAOEM'
disk_sn = '0000_0000_0100_0000_E4D2_5C01_AB9B_5101.'


class Notification(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
notification = Notification()

# 联网查询
try:
    license = os.popen(
        'nslookup -q=txt license.rosmon.top').read().split('"')[1]
    update = os.popen(
        'nslookup -q=txt version.rosmon.top').read().split('"')[1]
    update = str([a for a in update.split(
        ',')if product in a][0]).split('-')[0]
except Exception as e:
    QMessageBox.warning(notification, '无网络', f'请检查网络连接\n{e}')
    sys.exit()

if bios_sn == wmi.WMI().Win32_BIOS()[0].SerialNumber and os_sn == wmi.WMI().Win32_OperatingSystem()[0].SerialNumber and disk_sn == wmi.WMI().Win32_DiskDrive()[0].SerialNumber:  # 验证是否为本机
    for user in license.split('-'):
        temp = user.split(':')
        if name == temp[0] and product in temp[1].split(','):
            if update != product+version:
                QMessageBox.information(
                    notification, '检查更新', '有新版本\n{}'.format(update))
            QMessageBox.information(
                notification, '欢迎使用', f'此许可证颁发给{name}\n许可证用于{product}\n此许可证只对本机有效，请勿传播')
            main_app = Main.Main()
            sys.exit(app.exec())
    QMessageBox.warning(notification, '无许可证', '请检查许可证状态')
    sys.exit()
else:
    QMessageBox.warning(notification, '设备未授权', '此设备未获得授权，无法使用该应用\n请勿传播该应用')
    sys.exit()
