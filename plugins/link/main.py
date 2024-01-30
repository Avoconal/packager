from PySide6.QtWidgets import *
from PySide6.QtCore import *

from qfluentwidgets.common import FluentIcon

from .link_ui import Ui_link
from .link_select_ui import Ui_link_select

import os

class Link(QWidget,Ui_link):
    def __init__(self,parent:QWidget,mainwindow:QMainWindow):
        super().__init__()
        self.setupUi(parent)
        self.subwin_link_select=Link_select(mainwindow)

        self.signal_connect()

    def signal_connect(self):
        self.btn_add.clicked.connect(self.subwin_link_select.show)
        self.btn_del.clicked.connect(self.link_del)
        self.column_file.cellClicked.connect(self.update_link_pos)
        self.column_dir.cellClicked.connect(self.update_link_pos)
        self.link_pos = [0, 0]

    def link_table_update_size(self):
        self.column_file.setColumnWidth(
            0, self.column_file.width()*0.6)
        self.column_file.setColumnWidth(
            1, self.column_file.width()*0.3)
        self.column_dir.setColumnWidth(
            0, self.column_dir.width()*0.6)
        self.column_dir.setColumnWidth(
            1, self.column_dir.width()*0.3)

    def update_link_pos(self, y):
        self.link_pos = [self.column_file.hasFocus(), y]

    def link_del(self):
        temp = self.column_file if self.link_pos[0] else self.column_dir
        temp.removeRow(self.link_pos[1])

class Link_select(QMainWindow, Ui_link_select):
    def __init__(self,mainwindow:QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.mainwindow=mainwindow

        self.radio_file.clicked.connect(lambda:self.btn_select.setIcon(FluentIcon.DOCUMENT))
        self.radio_dir.clicked.connect(lambda:self.btn_select.setIcon(FluentIcon.FOLDER))
        self.btn_select.setIcon(FluentIcon.DOCUMENT)
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
        if self.lineedit_from.text():
            if self.radio_file.isChecked():
                temp = self.mainwindow.tab_link.column_file
            else:
                temp = self.mainwindow.tab_link.column_dir
            temp.setRowCount(temp.rowCount()+1)
            temp.setItem(temp.rowCount()-1, 0,
                         QTableWidgetItem(self.lineedit_from.text()))
            temp.setItem(temp.rowCount()-1, 1,
                         QTableWidgetItem(self.lineedit_to.text()))
            self.mainwindow.tab_link.link_table_update_size()

