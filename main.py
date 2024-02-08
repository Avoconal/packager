import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from qfluentwidgets.common import FluentIcon

import theme_control

from gui_ui import Ui_gui

from plugins.basic.main import Basic
from plugins.link.main import Link
from plugins.license.main import License
from plugins.copyright.main import Copyright
from plugins.about.main import About


class Main(QMainWindow, Ui_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # tab init
        self.tab_basic = Basic(self.tab_1, self)
        self.tab_link = Link(self.tab_2, self)
        self.tab_license = License(self.tab_3)
        self.tab_copyright = Copyright(self.tab_4)
        self.tab_about = About(self.tab_5)

        self.pivot.addItem('basic', '基本', lambda: self.update_current_tab(0))
        self.pivot.addItem('link', '映射', lambda: self.update_current_tab(1))
        self.pivot.addItem('license', '授权信息',
                           lambda: self.update_current_tab(2))
        self.pivot.addItem('copyright', '版权信息',
                           lambda: self.update_current_tab(3))
        self.pivot.addItem('about', '关于', lambda: self.update_current_tab(4))
        self.pivot.setCurrentItem('basic')

        self.drag_file = ''

        app.setWindowIcon(
            QIcon(os.path.join(os.path.dirname(__file__), 'icon', 'license.svg')))
        self.tab_link.btn_add.setIcon(FluentIcon.ADD)
        self.tab_link.btn_del.setIcon(FluentIcon.DELETE)
        self.show()
        self.signal_connect()

    def signal_connect(self):
        # window size update
        self.tabWidget.currentChanged.connect(self.window_size_update)
        self.window_size_update()

    def update_current_tab(self, index: int):
        self.tabWidget.setCurrentIndex(index)

    def window_size_update(self):
        self.animation = QPropertyAnimation(self, b'size')
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutBack)
        match self.tabWidget.currentIndex():
            case 0:
                self.animation.setEndValue(QSize(500, 300))
            case 1:
                self.animation.setEndValue(QSize(700, 300))
            case 2:
                self.animation.setEndValue(QSize(400, 200))
            case 3:
                self.animation.setEndValue(QSize(500, 200))
            case 4:
                self.animation.setEndValue(QSize(500, 200))
        self.animation.start()
        self.tab_link.link_table_update_size()

    def dragEnterEvent(self, event: QDragEnterEvent):
        drag_path = os.path.realpath(event.mimeData().urls()[0].toLocalFile())
        ext = os.path.splitext(drag_path)[1]

        if self.tabWidget.currentIndex() == 0 and ext in ['.exe', '.py']:
            event.accept()
            self.drag_file = drag_path

        elif self.tabWidget.currentIndex() == 1:
            event.accept()
            self.drag_file = drag_path

        elif self.tabWidget.currentIndex() == 3 and ext in ['.png', '.ico', '.svg']:
            event.accept()
            self.drag_file = drag_path

        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if self.drag_file:
            if self.tabWidget.currentIndex() == 0:
                if os.path.split(self.drag_file)[1] == 'python.exe':
                    if self.tab_basic.combobox_executor.findText(self.drag_file) == -1:
                        self.tab_basic.combobox_executor.addItem(
                            self.drag_file)
                    self.tab_basic.combobox_executor.setCurrentText(
                        self.drag_file)
                    self.tab_basic.test_executor()
                elif os.path.splitext(self.drag_file)[1] == '.py':
                    self.tab_basic.label_path_file.setText(self.drag_file)
                    self.tab_basic.btn_start.setEnabled(True)

            elif self.tabWidget.currentIndex() == 1:
                if os.path.isfile(self.drag_file):
                    self.tab_link.subwin_link_select.radio_file.setChecked(
                        True)
                    self.tab_link.subwin_link_select.btn_select.setIcon(
                        FluentIcon.DOCUMENT)
                else:
                    self.tab_link.subwin_link_select.radio_dir.setChecked(True)
                    self.tab_link.subwin_link_select.btn_select.setIcon(
                        FluentIcon.FOLDER)

                self.tab_link.subwin_link_select.lineedit_from.setText(
                    self.drag_file)
                self.tab_link.subwin_link_select.lineedit_to.setText(
                    os.path.split(self.drag_file)[1])
                self.tab_link.subwin_link_select.show()

            elif self.tabWidget.currentIndex() == 3:
                self.tab_copyright.label_icon_path.setText(self.drag_file)
                self.tab_copyright.label_icon_preview.setPixmap(
                    QPixmap(self.drag_file).scaled(50, 50))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main()

    theme_control.apply_theme(app, 'dark')
    sys.exit(app.exec())
