from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .about_ui import Ui_about

from qfluentwidgets.common import FluentIcon

import webbrowser,os

class About(QWidget,Ui_about):
    '''About page'''
    def __init__(self,parent:QWidget):
        super().__init__()
        self.setupUi(parent)
        self.btn_github.setIcon(FluentIcon.GITHUB)
        # self.btn_bilibili.setIcon(FluentIcon.HOME)
        self.btn_bilibili.setIcon(QIcon(os.path.join(os.path.dirname(__name__),'icon/bilibili.svg')))
        self.btn_tour.setIcon(FluentIcon.MOVIE)
        self.signal_connect()

    def signal_connect(self):
        self.btn_github.clicked.connect(lambda:webbrowser.open('https://www.github.com/abcdesteve'))
        self.btn_bilibili.clicked.connect(lambda:webbrowser.open('https://space.bilibili.com/520340464'))
        self.btn_tour.clicked.connect(lambda:webbrowser.open('https://space.bilibili.com/1247794668'))