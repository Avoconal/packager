from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .basic_ui import Ui_basic
from .cmd_ui import Ui_cmd

import os


class Basic(QWidget, Ui_basic):
    def __init__(self, parent: QWidget, mainwindow: QMainWindow):
        super().__init__()
        self.setupUi(parent)
        self.mainwindow = mainwindow
        self.signal_connect()

        # find executor
        self.combobox_executor.addItems(set(
            self.scan_file('C:\\', 'python.exe', 2) +
            self.scan_file('C:\Program Files', 'python.exe', 3) +
            self.scan_file('C:\Program Files (x86)', 'python.exe', 3) +
            self.scan_file('D:\\', 'python.exe', 4)+
            self.scan_file('E:\\','python.exe',4)
        ))
        if self.combobox_executor.count():
            self.combobox_executor.setCurrentIndex(0)
            self.test_executor()

    def signal_connect(self):
        self.checkbox_nuitka.clicked.connect(self.checkbox_nuitka.toggle)
        self.btn_select_file.clicked.connect(self.select_file)
        self.btn_select_executor.clicked.connect(
            self.select_executor)
        self.btn_select_file.clicked.connect(self.update_allow_start)
        self.btn_select_executor.clicked.connect(
            self.update_allow_start)
        self.btn_start.clicked.connect(self.process)
        self.combobox_executor.currentIndexChanged.connect(self.test_executor)

    def select_file(self):
        path = QFileDialog.getOpenFileName(
            self, '请选择文件', filter='代码文件 (*.py)')[0]
        if path:
            self.label_path_file.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def select_executor(self):
        path = QFileDialog.getOpenFileName(
            self, '请选择Python编译器', filter='Python编译器 (python.exe)')[0]
        if path:
            self.combobox_executor.addItem(path)
            self.test_executor()

        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def test_executor(self):
        status = os.popen(
            f'{self.combobox_executor.currentText()} -m pip show nuitka').read()
        if 'Name: Nuitka' in status: #last
            self.checkbox_nuitka.setChecked(True)
        else:
            QMessageBox.warning(self, '警告', f'Nuitka未安装\n{status}')
            self.checkbox_nuitka.setChecked(False)

    def scan_file(self, dir: str, goal: str, depth: int) -> list[str]:
        '''
        Find the goal in the given dir.
        Return mutiple results if found.

        argvs:
            dir: The location to scan.
            goal: The file to be found.
            depth: Decide how many folders to be scan.  1 means no child folder is scaned

        e.g. scan_file('c:/','python.exe',5)
        >>> ["c:/user/abcdesteve/python/python.exe","c:/python/python.exe"]
        '''
        results = []
        if os.path.isdir(dir) and depth > 0:
            try:
                lis = os.listdir(dir)
                if goal in lis:
                    results.append(os.path.join(dir, goal))
                temp = [results.extend(self.scan_file(os.path.join(
                    dir, i), goal, depth-1)) for i in lis if os.path.isdir(os.path.join(dir, i))]
                # print(f'temp:{temp}')
                return results
            except PermissionError:
                print(f'Not enough permission when trying to scan dir: {dir}')
                return []
        else:
            return []

    def update_allow_start(self):
        self.btn_start.setEnabled(bool(
            self.checkbox_nuitka.isChecked() and
            self.combobox_executor.currentText() and
            self.label_path_file.text()))

    def process(self):
        self.btn_select_file.setEnabled(False)
        self.btn_start.setEnabled(False)

        dir, source_code_name = os.path.split(
            self.label_path_file.text())

        # license init
        if self.mainwindow.tab_license.checkbox_switch.isChecked():
            with open('id.py', 'w', encoding='utf-8')as file:
                file.write("""user='{}'\neol={}\nbios_sn='{}'\nos_sn='{}'\ndisk_sn='{}'\nlink='{}'\ndark_mode={}\nsource_code='{}'""".format(self.mainwindow.tab_license.lineedit_user.text(), self.mainwindow.tab_license.dateedit.date(
                ).toString('yyyyMMdd'), self.mainwindow.tab_license.lineedit_bios_sn.text(), self.mainwindow.tab_license.lineedit_system_sn.text(), self.mainwindow.tab_license.lineedit_disk_sn.text(), self.mainwindow.tab_license.lineedit_link.text(), self.mainwindow.tab_license.checkbox_dark_mode.isChecked(), source_code_name))

        # plugin init
        # plugin = self.basic.scroll_plugin.findChildren(QCheckBox)
        plugin = ' '.join(['--enable-plugin='+self.plugin_list.item(i).text()
                           for i in range(self.plugin_list.count()) if self.plugin_list.item(i).checkState() == Qt.Checked])

        argv = [
            '--onefile' if self.checkbox_onefile.isChecked() else '',
            '--windows-disable-console' if self.checkbox_disable_console.isChecked() else '',
            '--standalone' if self.checkbox_standalone.isChecked() else '',
            '--windows-uac-admin' if self.checkbox_require_admin.isChecked() else ''
        ]

        link_file = [f'--include-data-files="{self.mainwindow.tab_link.column_file.item(i,0).text()}"="{self.mainwindow.tab_link.column_file.item(i,1).text()}"' for i in range(
            self.mainwindow.tab_link.column_file.rowCount())]
        link_dir = [f'--include-data-dir="{self.mainwindow.tab_link.column_dir.item(i,0).text()}"="{self.mainwindow.tab_link.column_dir.item(i,1).text()}"' for i in range(
            self.mainwindow.tab_link.column_dir.rowCount())]

        copyright = [
            f'--windows-icon-from-ico="{self.mainwindow.tab_copyright.label_icon_path.text()}"' if self.mainwindow.tab_copyright.label_icon_path.text() else '',
            f'--product-name="{self.mainwindow.tab_copyright.lineedit_project.text()}"'if self.mainwindow.tab_copyright.lineedit_project.text() else '',
            f'--product-version="{self.mainwindow.tab_copyright.lineedit_version.text()}"'if self.mainwindow.tab_copyright.lineedit_version.text() else '',
            f'--company-name="{self.mainwindow.tab_copyright.lineedit_company.text()}"'if self.mainwindow.tab_copyright.lineedit_company.text() else '',
            f'--copyright="{self.mainwindow.tab_copyright.lineedit_copyright.text()}"'if self.mainwindow.tab_copyright.lineedit_copyright.text() else '',
            f'--trademarks="{self.mainwindow.tab_copyright.lineedit_trademark.text()}"'if self.mainwindow.tab_copyright.lineedit_trademark.text() else ''
        ]

        # popen=os.popen(f'python -m nuitka --output-dir="{os.path.split(__file__)[0]}/output" {" ".join(argv)} {plugin}')

        if self.mainwindow.tab_license.checkbox_switch.isChecked():
            os.system(
                f'''copy "{os.path.realpath('id.py')}" "{dir}/id.py" /V /Y''')
            os.system(
                f'''copy "{os.path.realpath('sl_app_encrypt.py')}" "{dir}/sl_app_encrypt.py" /V /Y''')
            compile_file = os.path.join(dir, 'sl_app_encrypt.py')
        else:
            compile_file = self.label_path_file.text()

        os.chdir(dir)
        print(
            f'''{self.combobox_executor.currentText()} -m nuitka --output-dir="{os.path.join(os.path.dirname(__file__),'output')}" {" ".join(argv)} {plugin} {" ".join(link_file)} {" ".join(link_dir)} {" ".join(copyright)} {self.lineedit_addition.text()} {compile_file}''')
        popen = os.popen(
            f'''{self.combobox_executor.currentText()} -m nuitka --output-dir="{os.path.join(os.path.dirname(__file__),'output')}" {" ".join(argv)} {plugin} {" ".join(link_file)} {" ".join(link_dir)} {" ".join(copyright)} {self.lineedit_addition.text()} {compile_file}''')
        self.cmd = Cmd(popen,self.mainwindow)


class Cmd(QMainWindow, Ui_cmd):
    def __init__(self, popen, mainwindow:QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.txt = ''
        self.popen = popen
        self.mainwindow=mainwindow

        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.update_print)
        self.timer.timeout.connect(self.update_log)

        self.show()

    def update_print(self):
        self.txt = self.popen.readline()
        if self.txt:
            print(self.txt)

    def update_log(self):
        if self.txt != self.textEdit.toPlainText().split('\n')[-1]:
            self.textEdit.append(self.txt)
            self.textEdit.moveCursor(QTextCursor.End)

    def closeEvent(self, event):
        self.mainwindow.tab_basic.btn_select_file.setEnabled(True)
        self.mainwindow.tab_basic.btn_start.setEnabled(True)
        os.system(
            f"explorer {os.path.join(os.path.dirname(__file__),'output')}")
