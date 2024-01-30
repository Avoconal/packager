# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browser.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_browser(object):
    def setupUi(self, browser):
        if not browser.objectName():
            browser.setObjectName(u"browser")
        browser.resize(800, 600)
        browser.setMinimumSize(QSize(400, 300))
        browser.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(browser)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.baidu = QRadioButton(self.centralwidget)
        self.baidu.setObjectName(u"baidu")
        self.baidu.setChecked(True)

        self.horizontalLayout.addWidget(self.baidu)

        self.youdao = QRadioButton(self.centralwidget)
        self.youdao.setObjectName(u"youdao")

        self.horizontalLayout.addWidget(self.youdao)

        self.bing = QRadioButton(self.centralwidget)
        self.bing.setObjectName(u"bing")

        self.horizontalLayout.addWidget(self.bing)

        self.google = QRadioButton(self.centralwidget)
        self.google.setObjectName(u"google")

        self.horizontalLayout.addWidget(self.google)

        self.ciba = QRadioButton(self.centralwidget)
        self.ciba.setObjectName(u"ciba")

        self.horizontalLayout.addWidget(self.ciba)

        self.oxford = QRadioButton(self.centralwidget)
        self.oxford.setObjectName(u"oxford")

        self.horizontalLayout.addWidget(self.oxford)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.tencent = QRadioButton(self.centralwidget)
        self.tencent.setObjectName(u"tencent")

        self.horizontalLayout.addWidget(self.tencent)

        self.auto_update = QCheckBox(self.centralwidget)
        self.auto_update.setObjectName(u"auto_update")
        self.auto_update.setChecked(True)

        self.horizontalLayout.addWidget(self.auto_update)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.web_layout = QVBoxLayout()
        self.web_layout.setObjectName(u"web_layout")

        self.verticalLayout.addLayout(self.web_layout)

        browser.setCentralWidget(self.centralwidget)

        self.retranslateUi(browser)

        QMetaObject.connectSlotsByName(browser)
    # setupUi

    def retranslateUi(self, browser):
        browser.setWindowTitle(QCoreApplication.translate("browser", u"\u795e\u9f99\u7ffb\u8bd1 - \u7f51\u9875", None))
        self.label.setText(QCoreApplication.translate("browser", u"\u7ffb\u8bd1\u5f15\u64ce\uff1a", None))
        self.baidu.setText(QCoreApplication.translate("browser", u"\u767e\u5ea6", None))
        self.youdao.setText(QCoreApplication.translate("browser", u"\u6709\u9053", None))
        self.bing.setText(QCoreApplication.translate("browser", u"\u5fc5\u5e94", None))
        self.google.setText(QCoreApplication.translate("browser", u"\u8c37\u6b4c", None))
        self.ciba.setText(QCoreApplication.translate("browser", u"\u8bcd\u9738", None))
        self.oxford.setText(QCoreApplication.translate("browser", u"\u725b\u6d25", None))
        self.tencent.setText(QCoreApplication.translate("browser", u"\u817e\u8baf", None))
        self.auto_update.setText(QCoreApplication.translate("browser", u"\u5b9e\u65f6\u66f4\u65b0", None))
    # retranslateUi

