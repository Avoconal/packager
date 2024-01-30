# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_copyright.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_copyright(object):
    def setupUi(self, copyright):
        if not copyright.objectName():
            copyright.setObjectName(u"copyright")
        copyright.resize(300, 200)
        self.verticalLayout = QVBoxLayout(copyright)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_icon = QPushButton(copyright)
        self.btn_icon.setObjectName(u"btn_icon")
        self.btn_icon.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btn_icon)

        self.label_icon = QLabel(copyright)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_icon)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_project = QLabel(copyright)
        self.label_project.setObjectName(u"label_project")

        self.gridLayout.addWidget(self.label_project, 0, 0, 1, 1)

        self.lineedit_project = QLineEdit(copyright)
        self.lineedit_project.setObjectName(u"lineedit_project")

        self.gridLayout.addWidget(self.lineedit_project, 0, 1, 1, 1)

        self.label_version = QLabel(copyright)
        self.label_version.setObjectName(u"label_version")

        self.gridLayout.addWidget(self.label_version, 1, 0, 1, 1)

        self.lineedit_version = QLineEdit(copyright)
        self.lineedit_version.setObjectName(u"lineedit_version")

        self.gridLayout.addWidget(self.lineedit_version, 1, 1, 1, 1)

        self.label_company = QLabel(copyright)
        self.label_company.setObjectName(u"label_company")

        self.gridLayout.addWidget(self.label_company, 2, 0, 1, 1)

        self.lineedit_company = QLineEdit(copyright)
        self.lineedit_company.setObjectName(u"lineedit_company")

        self.gridLayout.addWidget(self.lineedit_company, 2, 1, 1, 1)

        self.label_copyright = QLabel(copyright)
        self.label_copyright.setObjectName(u"label_copyright")

        self.gridLayout.addWidget(self.label_copyright, 3, 0, 1, 1)

        self.lineedit_copyright = QLineEdit(copyright)
        self.lineedit_copyright.setObjectName(u"lineedit_copyright")

        self.gridLayout.addWidget(self.lineedit_copyright, 3, 1, 1, 1)

        self.label_trademark = QLabel(copyright)
        self.label_trademark.setObjectName(u"label_trademark")

        self.gridLayout.addWidget(self.label_trademark, 4, 0, 1, 1)

        self.lineedit_trademark = QLineEdit(copyright)
        self.lineedit_trademark.setObjectName(u"lineedit_trademark")

        self.gridLayout.addWidget(self.lineedit_trademark, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(copyright)

        QMetaObject.connectSlotsByName(copyright)
    # setupUi

    def retranslateUi(self, copyright):
        copyright.setWindowTitle(QCoreApplication.translate("copyright", u"Form", None))
        self.btn_icon.setText(QCoreApplication.translate("copyright", u"\u9009\u62e9\u56fe\u6807", None))
        self.label_icon.setText("")
        self.label_project.setText(QCoreApplication.translate("copyright", u"\u9879\u76ee\u540d\uff1a", None))
        self.label_version.setText(QCoreApplication.translate("copyright", u"\u7248\u672c\uff1a", None))
        self.lineedit_version.setPlaceholderText(QCoreApplication.translate("copyright", u"\u6700\u591a\u56db\u4f4d\u6570\u5b57\u7248\u672c\u53f7", None))
        self.label_company.setText(QCoreApplication.translate("copyright", u"\u4f01\u4e1a\u540d\uff1a", None))
        self.label_copyright.setText(QCoreApplication.translate("copyright", u"\u7248\u6743\uff1a", None))
        self.label_trademark.setText(QCoreApplication.translate("copyright", u"\u5546\u6807\uff1a", None))
    # retranslateUi

