# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(480, 270)
        gui.setMinimumSize(QSize(480, 270))
        gui.setMaximumSize(QSize(480, 270))
        self.centralwidget = QWidget(gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(170, 50, 150, 25))
        self.name_label.setMinimumSize(QSize(150, 25))
        font = QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setAutoFillBackground(True)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(40, 10, 400, 41))
        self.title_label.setMinimumSize(QSize(400, 0))
        self.title_label.setBaseSize(QSize(100, 0))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.title_label.setAutoFillBackground(True)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(10, 170, 461, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.input.setFont(font2)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setClearButtonEnabled(True)
        self.topmost = QCheckBox(self.centralwidget)
        self.topmost.setObjectName(u"topmost")
        self.topmost.setGeometry(QRect(250, 80, 101, 31))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.topmost.setFont(font3)
        self.topmost.setChecked(True)
        self.file_select = QPushButton(self.centralwidget)
        self.file_select.setObjectName(u"file_select")
        self.file_select.setGeometry(QRect(130, 120, 101, 31))
        self.file_select.setFont(font3)
        self.output = QLineEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 220, 461, 41))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.output.setFont(font4)
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setClearButtonEnabled(True)
        self.hide_char = QCheckBox(self.centralwidget)
        self.hide_char.setObjectName(u"hide_char")
        self.hide_char.setGeometry(QRect(250, 120, 101, 31))
        self.hide_char.setFont(font3)
        self.hide_char.setChecked(True)
        self.web = QPushButton(self.centralwidget)
        self.web.setObjectName(u"web")
        self.web.setGeometry(QRect(130, 80, 101, 31))
        self.web.setFont(font3)
        gui.setCentralWidget(self.centralwidget)
        self.name_label.raise_()
        self.title_label.raise_()
        self.output.raise_()
        self.input.raise_()
        self.hide_char.raise_()
        self.file_select.raise_()
        self.topmost.raise_()
        self.web.raise_()

        self.retranslateUi(gui)

        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"\u795e\u9f99\u7ffb\u8bd1 v1.8", None))
        self.name_label.setText(QCoreApplication.translate("gui", u"by abcdesteve", None))
        self.title_label.setText(QCoreApplication.translate("gui", u"\u795e\u9f99\u7ffb\u8bd1 v1.8", None))
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("gui", u"\u8f93\u5165\u8981\u7ffb\u8bd1\u7684\u5185\u5bb9", None))
#endif // QT_CONFIG(tooltip)
        self.topmost.setText(QCoreApplication.translate("gui", u"\u7a97\u53e3\u7f6e\u9876", None))
        self.file_select.setText(QCoreApplication.translate("gui", u"\u6587\u4ef6\u7ffb\u8bd1", None))
#if QT_CONFIG(tooltip)
        self.output.setToolTip(QCoreApplication.translate("gui", u"\u7ffb\u8bd1\u7ed3\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.hide_char.setText(QCoreApplication.translate("gui", u"\u5ffd\u7565\u6807\u70b9", None))
        self.web.setText(QCoreApplication.translate("gui", u"\u6253\u5f00\u7f51\u9875", None))
    # retranslateUi

