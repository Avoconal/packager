import os
import sys
import time

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qdarkstyle
# from qt_material import apply_stylesheet

from ui_gui import Ui_gui
from ui_cmd import Ui_cmd
from ui_link_select import Ui_link_select

from ui_tab_basic import Ui_basic
from ui_tab_link import Ui_link
from ui_tab_license import Ui_license
from ui_tab_copyright import Ui_copyright


class Cmd(QMainWindow, Ui_cmd):

    def __init__(self, popen):
        super().__init__()
        self.setupUi(self)
        self.txt = ''
        self.popen = popen
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
        global window
        window.basic.btn_select.setEnabled(True)
        window.basic.btn_start.setEnabled(True)
        os.system('explorer .')


class Link_select(QMainWindow, Ui_link_select):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.btn_select.clicked.connect(self.select)

    def select(self):
        if self.radio_file.isChecked():
            path = QFileDialog.getOpenFileName(self, '请选择文件')[0]
        else:
            path = QFileDialog.getExistingDirectory(self, '请选择目录')
        if path:
            self.lineedit_from.setText(path)
            self.lineedit_to.setText(os.path.split(path)[1])
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def closeEvent(self, event):
        global window
        if self.radio_file.isChecked():
            temp = window.link.column_file
        else:
            temp = window.link.column_dir
        temp.setRowCount(temp.rowCount()+1)
        temp.setItem(temp.rowCount()-1, 0,
                     QTableWidgetItem(self.lineedit_from.text()))
        temp.setItem(temp.rowCount()-1, 1,
                     QTableWidgetItem(self.lineedit_to.text()))
        window.link_table_update_size()
        # temp.addItem(f'{self.lineedit_from.text()} -> {self.lineedit_to.text()}')


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # tab init
        self.basic = Ui_basic()
        self.link = Ui_link()
        self.license = Ui_license()
        self.copyright = Ui_copyright()
        self.basic.setupUi(self.tab_1)
        self.link.setupUi(self.tab_2)
        self.license.setupUi(self.tab_3)
        self.copyright.setupUi(self.tab_4)

        # subwin init
        self.subwin_link_select = Link_select()

        # # tab2 init
        # self.link.column_file.setColumnCount(2)
        # self.link.column_file.setHorizontalHeaderLabels(['原路径', '目标路径'])
        # self.link.column_dir.setColumnCount(2)
        # self.link.column_dir.setHorizontalHeaderLabels(['原路径', '目标路径'])

        # tab3 init
        self.license.checkbox_switch.clicked.connect(
            self.update_encryption_status)

        date = [int(i) for i in time.strftime(r'%Y-%m-%d').split('-')]
        self.license.dateedit.setDate(QDate(date[0], date[1], date[2]))

        self.basic.btn_select.clicked.connect(self.select_file)
        self.basic.btn_start.clicked.connect(self.process)
        self.link.btn_add.clicked.connect(self.subwin_link_select.show)
        self.link.btn_del.clicked.connect(self.link_del)
        self.link.column_file.cellClicked.connect(self.update_link_pos)
        self.link.column_dir.cellClicked.connect(self.update_link_pos)
        self.link_pos = [0, 0]

        # tab4 init
        self.copyright.btn_select_icon.clicked.connect(self.select_icon)
        self.copyright.btn_clear_icon.clicked.connect(self.clear_icon)

        # window size update
        self.tabWidget.currentChanged.connect(self.window_size_update)
        self.window_size_update()

        self.show()

    def window_size_update(self):
        self.animation = QPropertyAnimation(self, b'size')
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutBack)
        match self.tabWidget.currentIndex():
            case 0:
                self.animation.setEndValue(QSize(350, 250))
                # self.resize(350, 250)
            case 1:
                self.animation.setEndValue(QSize(700, 300))
                # self.resize(500, 300)
            case 2:
                self.animation.setEndValue(QSize(350, 200))
                # self.resize(350, 200)
            case 3:
                self.animation.setEndValue(QSize(400, 200))
                # self.resize(300, 200)
        self.animation.start()
        self.link_table_update_size()

    # tab1

    def select_file(self):
        path = QFileDialog.getOpenFileName(
            self, '请选择文件', filter='代码文件 (*.py)')[0]
        if path:
            self.basic.btn_start.setEnabled(True)
            self.basic.label_path.setText(path)
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def process(self):
        self.basic.btn_select.setEnabled(False)
        self.basic.btn_start.setEnabled(False)

        dir, source_code_name = os.path.split(self.basic.label_path.text())

        # license init
        if self.license.checkbox_switch.isChecked():
            with open('id.py', 'w', encoding='utf-8')as file:
                file.write("""user='{}'\neol={}\nbios_sn='{}'\nos_sn='{}'\ndisk_sn='{}'\nlink='{}'\ndark_mode={}\nsource_code='{}'""".format(self.license.lineedit_user.text(), self.license.dateedit.date(
                ).toString('yyyyMMdd'), self.license.lineedit_bios_sn.text(), self.license.lineedit_system_sn.text(), self.license.lineedit_disk_sn.text(), self.license.lineedit_link.text(), self.license.checkbox_dark_mode.isChecked(), source_code_name))

        # plugin init
        # plugin = self.basic.scroll_plugin.findChildren(QCheckBox)
        plugin = ' '.join(['--enable-plugin='+self.basic.plugin_list.item(i).text()
                          for i in range(self.basic.plugin_list.count()) if self.basic.plugin_list.item(i).checkState() == Qt.Checked])

        argv = [
            '--onefile' if self.basic.checkbox_onefile.isChecked() else '',
            '--windows-disable-console' if self.basic.checkbox_disable_console.isChecked() else '',
            '--standalone' if self.basic.checkbox_standalone.isChecked() else '',
            '--windows-uac-admin' if self.basic.checkbox_require_admin.isChecked() else ''
        ]

        link_file = [f'--include-data-files="{self.link.column_file.item(i,0).text()}"="{self.link.column_file.item(i,1).text()}"' for i in range(
            self.link.column_file.rowCount())]
        link_dir = [f'--include-data-dir="{self.link.column_dir.item(i,0).text()}"="{self.link.column_dir.item(i,1).text()}"' for i in range(
            self.link.column_dir.rowCount())]

        copyright = [
            f'--windows-icon-from-ico="{self.copyright.label_icon_path.text()}"' if self.copyright.label_icon_path.text() else '',
            f'--product-name="{self.copyright.lineedit_project.text()}"'if self.copyright.lineedit_project.text() else '',
            f'--product-version="{self.copyright.lineedit_version.text()}"'if self.copyright.lineedit_version.text() else '',
            f'--company-name="{self.copyright.lineedit_company.text()}"'if self.copyright.lineedit_company.text() else '',
            f'--copyright="{self.copyright.lineedit_copyright.text()}"'if self.copyright.lineedit_copyright.text() else '',
            f'--trademarks="{self.copyright.lineedit_trademark.text()}"'if self.copyright.lineedit_trademark.text() else ''
        ]

        # popen=os.popen(f'python -m nuitka --output-dir="{os.path.split(__file__)[0]}/output" {" ".join(argv)} {plugin}')

        if self.license.checkbox_switch.isChecked():
            os.system(
                f'''copy "{os.path.realpath('id.py')}" "{dir}/id.py" /V /Y''')
            os.system(
                f'''copy "{os.path.realpath('sl_app_encrypt.py')}" "{dir}/sl_app_encrypt.py" /V /Y''')
            compile_file = os.path.join(dir, 'sl_app_encrypt.py')
        else:
            compile_file = self.basic.label_path.text()

        os.chdir(dir)
        print(
            f'python -m nuitka --output-dir="{os.path.split(__file__)[0]}/output" {" ".join(argv)} {plugin} {" ".join(link_file)} {" ".join(link_dir)} {" ".join(copyright)} {self.basic.lineedit_addition.text()} {compile_file}')
        popen = os.popen(
            f'python -m nuitka --output-dir="{os.path.split(__file__)[0]}/output" {" ".join(argv)} {plugin} {" ".join(link_file)} {" ".join(link_dir)} {" ".join(copyright)} {self.basic.lineedit_addition.text()} {compile_file}')
        self.cmd = Cmd(popen)

    # tab2
    def link_table_update_size(self):
        self.link.column_file.setColumnWidth(
            0, self.link.column_file.width()*0.6)
        self.link.column_file.setColumnWidth(
            1, self.link.column_file.width()*0.3)
        self.link.column_dir.setColumnWidth(
            0, self.link.column_dir.width()*0.6)
        self.link.column_dir.setColumnWidth(
            1, self.link.column_dir.width()*0.3)

    def update_link_pos(self, y):
        self.link_pos = [self.link.column_file.hasFocus(), y]

    def link_del(self):
        temp = self.link.column_file if self.link_pos[0] else self.link.column_dir
        temp.removeRow(self.link_pos[1])

    # tab3
    def update_encryption_status(self):
        temp = self.license.checkbox_switch.isChecked()
        self.license.checkbox_dark_mode.setEnabled(temp)
        self.license.lineedit_user.setEnabled(temp)
        self.license.dateedit.setEnabled(temp)
        self.license.lineedit_bios_sn.setEnabled(temp)
        self.license.lineedit_system_sn.setEnabled(temp)
        self.license.lineedit_disk_sn.setEnabled(temp)
        self.license.lineedit_link.setEnabled(temp)

    # tab4
    def select_icon(self):
        path = QFileDialog.getOpenFileName(
            self, '请选择文件', filter='图标文件 (*.png *.ico);;图标文件 (*.png);;图标文件 (*.ico)')[0]
        if path:
            self.copyright.label_icon_path.setText(path)
            self.copyright.label_icon_preview.setPixmap(
                QPixmap(path).scaled(50, 50))
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def clear_icon(self):
        self.copyright.label_icon_path.setText('')
        self.copyright.label_icon_preview.setPixmap(QPixmap())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    # color=['dark_amber.xml', 'dark_blue.xml', 'dark_cyan.xml', 'dark_lightgreen.xml', 'dark_pink.xml','dark_purple.xml', 'dark_red.xml','dark_teal.xml','dark_yellow.xml', 'light_amber.xml','light_blue.xml', 'light_cyan.xml','light_cyan_500.xml','light_lightgreen.xml','light_pink.xml','light_purple.xml','light_red.xml','light_teal.xml','light_yellow.xml']
    # apply_stylesheet(app,color[3])
    window = Main()
    sys.exit(app.exec())
