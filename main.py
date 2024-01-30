import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui_gui import Ui_gui
from ui_cmd import Ui_cmd

class Cmd(QMainWindow,Ui_cmd):
    def __init__(self,popen):
        super().__init__()
        self.setupUi(self)
        self.timer=QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.update_print)
        self.timer.timeout.connect(self.update_log)
        self.popen=popen
    def update_print(self):
        self.txt=self.popen.readline()
        if self.txt:
            print(self.txt)
    def update_log(self):
        if self.txt!=self.textEdit.toPlainText().split('\n')[-1]:
            self.textEdit.append(self.txt)
            self.textEdit.moveCursor(QTextCursor.End)

class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.edit_name.textChanged.connect(self.update_encryption_status)
        self.edit_version.textChanged.connect(self.update_encryption_status)
        self.edit_customer.textChanged.connect(self.update_encryption_status)
        self.edit_os_sn.textChanged.connect(self.update_encryption_status)
        self.edit_disk_sn.textChanged.connect(self.update_encryption_status)
        self.button_select.clicked.connect(self.select_file)
        self.button_start.clicked.connect(self.process)

        self.cmd=QMainWindow()

        self.show()

    def update_encryption_status(self):
        if self.edit_name.text():
            self.edit_version.setEnabled(True)
            self.edit_customer.setEnabled(True)
            self.edit_os_sn.setEnabled(True)
            self.edit_disk_sn.setEnabled(True)
            if self.edit_version.text() and self.edit_customer.text() and self.edit_os_sn.text() and self.edit_disk_sn.text():
                self.button_start.setEnabled(True)
            else:
                self.button_start.setEnabled(False)
        else:
            self.edit_version.setEnabled(False)
            self.edit_customer.setEnabled(False)
            self.edit_os_sn.setEnabled(False)
            self.edit_disk_sn.setEnabled(False)
            self.button_start.setEnabled(True)
        if not self.label_path.text():
            self.button_start.setEnabled(False)

    def select_file(self):
        path = QFileDialog.getOpenFileName(self, '打开文件', filter='*.py')[0]
        if path:
            self.label_path.setText(path)
            self.update_encryption_status()
        else:
            QMessageBox.warning(self, '警告', '文件路径有误，请重新选择')

    def process(self):
        lis=self.scroll_plugin.findChildren(QCheckBox)
        argv=''.join([' --enable-plugin='+i.text() for i in lis if i.isChecked()])
        if self.checkbox_one_file.isChecked():
            argv+=' --onefile '
        if self.checkbox_disable_console.isChecked():
            argv+=' --windows-disable-console '
        if self.checkbox_require_admin.isChecked():
            argv+=' --windows-uac-admin '
        print(r'nuitka --standalone --output-dir="D:\Users\abcdesteve\Desktop\神龙\神龙授权器\output" {} "{}"'.format(argv,self.label_path.text()))
        os.chdir(r'D:\Users\abcdesteve\Desktop\神龙\神龙授权器\神龙授权器v1.1\core')
        self.cmd=Cmd(os.popen(r'nuitka --standalone --output-dir="D:\Users\abcdesteve\Desktop\神龙\神龙授权器\output" {} "{}"'.format(argv,self.label_path.text())))
        self.cmd.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())
