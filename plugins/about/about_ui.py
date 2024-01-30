# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

from qfluentwidgets import (PrimaryPushButton, PushButton, TextEdit)

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(400, 300)
        self.gridLayout = QGridLayout(about)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = TextEdit(about)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 3)

        self.btn_github = PrimaryPushButton(about)
        self.btn_github.setObjectName(u"btn_github")

        self.gridLayout.addWidget(self.btn_github, 1, 0, 1, 1)

        self.btn_bilibili = PushButton(about)
        self.btn_bilibili.setObjectName(u"btn_bilibili")

        self.gridLayout.addWidget(self.btn_bilibili, 1, 1, 1, 1)

        self.btn_tour = PushButton(about)
        self.btn_tour.setObjectName(u"btn_tour")

        self.gridLayout.addWidget(self.btn_tour, 1, 2, 1, 1)


        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"Form", None))
        self.btn_github.setText(QCoreApplication.translate("about", u"GitHub\u4ed3\u5e93", None))
        self.btn_bilibili.setText(QCoreApplication.translate("about", u"B\u7ad9\u4e3b\u9875", None))
        self.btn_tour.setText(QCoreApplication.translate("about", u"\u89c6\u9891\u4ecb\u7ecd", None))
    # retranslateUi

