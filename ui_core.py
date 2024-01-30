# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'core.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_core(object):
    def setupUi(self, core):
        if not core.objectName():
            core.setObjectName(u"core")
        core.resize(400, 150)
        core.setMinimumSize(QSize(400, 150))
        core.setMaximumSize(QSize(400, 150))
        self.centralwidget = QWidget(core)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.session_label = QLabel(self.centralwidget)
        self.session_label.setObjectName(u"session_label")

        self.gridLayout.addWidget(self.session_label, 0, 0, 1, 1)

        self.session = QLineEdit(self.centralwidget)
        self.session.setObjectName(u"session")
        self.session.setReadOnly(False)
        self.session.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.session, 0, 1, 1, 1)

        self.session_paste = QPushButton(self.centralwidget)
        self.session_paste.setObjectName(u"session_paste")
        self.session_paste.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.session_paste, 0, 2, 1, 1)

        self.identify_label = QLabel(self.centralwidget)
        self.identify_label.setObjectName(u"identify_label")

        self.gridLayout.addWidget(self.identify_label, 1, 0, 1, 1)

        self.identify = QLineEdit(self.centralwidget)
        self.identify.setObjectName(u"identify")
        self.identify.setEnabled(False)
        self.identify.setReadOnly(True)

        self.gridLayout.addWidget(self.identify, 1, 1, 1, 1)

        self.identify_copy = QPushButton(self.centralwidget)
        self.identify_copy.setObjectName(u"identify_copy")
        self.identify_copy.setEnabled(False)
        self.identify_copy.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.identify_copy, 1, 2, 1, 1)

        self.activate_label = QLabel(self.centralwidget)
        self.activate_label.setObjectName(u"activate_label")

        self.gridLayout.addWidget(self.activate_label, 2, 0, 1, 1)

        self.activate = QLineEdit(self.centralwidget)
        self.activate.setObjectName(u"activate")
        self.activate.setEnabled(False)
        self.activate.setReadOnly(False)
        self.activate.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.activate, 2, 1, 1, 1)

        self.activate_paste = QPushButton(self.centralwidget)
        self.activate_paste.setObjectName(u"activate_paste")
        self.activate_paste.setEnabled(False)
        self.activate_paste.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.activate_paste, 2, 2, 1, 1)

        core.setCentralWidget(self.centralwidget)

        self.retranslateUi(core)

        QMetaObject.connectSlotsByName(core)
    # setupUi

    def retranslateUi(self, core):
        core.setWindowTitle(QCoreApplication.translate("core", u"\u6fc0\u6d3b", None))
        self.session_label.setText(QCoreApplication.translate("core", u"\u4f1a\u8bdd\u7801\uff1a", None))
        self.session.setText("")
        self.session.setPlaceholderText(QCoreApplication.translate("core", u"\u8bf7\u5411\u5f00\u53d1\u8005\u83b7\u53d6\u4f1a\u8bdd\u7801", None))
        self.session_paste.setText(QCoreApplication.translate("core", u"\u7c98\u8d34", None))
        self.identify_label.setText(QCoreApplication.translate("core", u"\u8bc6\u522b\u7801\uff1a", None))
        self.identify.setText("")
        self.identify.setPlaceholderText(QCoreApplication.translate("core", u"\u83b7\u53d6\u4f1a\u8bdd\u7801\u540e\u5c06\u8bc6\u522b\u7801\u53d1\u7ed9\u5f00\u53d1\u8005", None))
        self.identify_copy.setText(QCoreApplication.translate("core", u"\u590d\u5236", None))
        self.activate_label.setText(QCoreApplication.translate("core", u"\u6fc0\u6d3b\u7801\uff1a", None))
        self.activate.setText("")
        self.activate.setPlaceholderText(QCoreApplication.translate("core", u"\u8bf7\u5411\u5f00\u53d1\u8005\u83b7\u53d6\u6fc0\u6d3b\u7801", None))
        self.activate_paste.setText(QCoreApplication.translate("core", u"\u7c98\u8d34", None))
    # retranslateUi

