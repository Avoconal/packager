# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'link_select.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_link_select(object):
    def setupUi(self, link_select):
        if not link_select.objectName():
            link_select.setObjectName(u"link_select")
        link_select.resize(300, 100)
        self.centralwidget = QWidget(link_select)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_select = QPushButton(self.centralwidget)
        self.btn_select.setObjectName(u"btn_select")

        self.gridLayout.addWidget(self.btn_select, 0, 0, 1, 1)

        self.radio_file = QRadioButton(self.centralwidget)
        self.radio_file.setObjectName(u"radio_file")
        self.radio_file.setChecked(True)

        self.gridLayout.addWidget(self.radio_file, 0, 2, 1, 1)

        self.label_from = QLabel(self.centralwidget)
        self.label_from.setObjectName(u"label_from")

        self.gridLayout.addWidget(self.label_from, 1, 0, 1, 1)

        self.lineedit_to = QLineEdit(self.centralwidget)
        self.lineedit_to.setObjectName(u"lineedit_to")

        self.gridLayout.addWidget(self.lineedit_to, 3, 2, 1, 2)

        self.label_to = QLabel(self.centralwidget)
        self.label_to.setObjectName(u"label_to")

        self.gridLayout.addWidget(self.label_to, 3, 0, 1, 1)

        self.radio_dir = QRadioButton(self.centralwidget)
        self.radio_dir.setObjectName(u"radio_dir")

        self.gridLayout.addWidget(self.radio_dir, 0, 3, 1, 1)

        self.lineedit_from = QLineEdit(self.centralwidget)
        self.lineedit_from.setObjectName(u"lineedit_from")

        self.gridLayout.addWidget(self.lineedit_from, 1, 2, 1, 2)

        link_select.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_select, self.radio_file)
        QWidget.setTabOrder(self.radio_file, self.radio_dir)
        QWidget.setTabOrder(self.radio_dir, self.lineedit_from)
        QWidget.setTabOrder(self.lineedit_from, self.lineedit_to)

        self.retranslateUi(link_select)

        QMetaObject.connectSlotsByName(link_select)
    # setupUi

    def retranslateUi(self, link_select):
        link_select.setWindowTitle(QCoreApplication.translate("link_select", u"\u6587\u4ef6\u94fe\u63a5", None))
        self.btn_select.setText(QCoreApplication.translate("link_select", u"\u9009\u62e9\u6587\u4ef6/\u76ee\u5f55", None))
        self.radio_file.setText(QCoreApplication.translate("link_select", u"\u6587\u4ef6", None))
        self.label_from.setText(QCoreApplication.translate("link_select", u"\u6e90\u6587\u4ef6/\u76ee\u5f55\uff1a", None))
        self.label_to.setText(QCoreApplication.translate("link_select", u"\u76ee\u6807\u8def\u5f84\uff1a", None))
        self.radio_dir.setText(QCoreApplication.translate("link_select", u"\u76ee\u5f55", None))
    # retranslateUi

