from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .copyright_ui import Ui_copyright


class Copyright(QWidget, Ui_copyright):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.setupUi(parent)
        self.signal_connect()

    def signal_connect(self):
        self.btn_select_icon.clicked.connect(self.select_icon)
        self.btn_clear_icon.clicked.connect(self.clear_icon)

    def select_icon(self):
        path = QFileDialog.getOpenFileName(
            self, '请选择文件', filter='图标文件 (*.png *.ico);;图标文件 (*.png);;图标文件 (*.ico)')[0]
        if path:
            self.label_icon_path.setText(path)
            self.label_icon_preview.setPixmap(
                QPixmap(path).scaled(50, 50))
        else:
            QMessageBox.warning(self, '警告', '路径无效')

    def clear_icon(self):
        self.label_icon_path.setText('')
        self.label_icon_preview.setPixmap(QPixmap())
