# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copyright.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PrimaryPushButton, ToolButton)

class Ui_copyright(object):
    def setupUi(self, copyright):
        if not copyright.objectName():
            copyright.setObjectName(u"copyright")
        copyright.resize(300, 223)
        self.verticalLayout = QVBoxLayout(copyright)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_select_icon = PrimaryPushButton(copyright)
        self.btn_select_icon.setObjectName(u"btn_select_icon")
        self.btn_select_icon.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.btn_select_icon)

        self.label_icon_path = QLabel(copyright)
        self.label_icon_path.setObjectName(u"label_icon_path")
        self.label_icon_path.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_icon_path)

        self.label_icon_preview = QLabel(copyright)
        self.label_icon_preview.setObjectName(u"label_icon_preview")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icon_preview.sizePolicy().hasHeightForWidth())
        self.label_icon_preview.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_icon_preview)

        self.btn_clear_icon = ToolButton(copyright)
        self.btn_clear_icon.setObjectName(u"btn_clear_icon")

        self.horizontalLayout.addWidget(self.btn_clear_icon)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_company = QLabel(copyright)
        self.label_company.setObjectName(u"label_company")

        self.gridLayout.addWidget(self.label_company, 2, 0, 1, 1)

        self.lineedit_company = LineEdit(copyright)
        self.lineedit_company.setObjectName(u"lineedit_company")
        self.lineedit_company.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_company, 2, 1, 1, 1)

        self.label_copyright = QLabel(copyright)
        self.label_copyright.setObjectName(u"label_copyright")

        self.gridLayout.addWidget(self.label_copyright, 3, 0, 1, 1)

        self.lineedit_version = LineEdit(copyright)
        self.lineedit_version.setObjectName(u"lineedit_version")
        self.lineedit_version.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_version, 1, 1, 1, 1)

        self.lineedit_copyright = LineEdit(copyright)
        self.lineedit_copyright.setObjectName(u"lineedit_copyright")
        self.lineedit_copyright.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_copyright, 3, 1, 1, 1)

        self.lineedit_project = LineEdit(copyright)
        self.lineedit_project.setObjectName(u"lineedit_project")
        self.lineedit_project.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_project, 0, 1, 1, 1)

        self.lineedit_trademark = LineEdit(copyright)
        self.lineedit_trademark.setObjectName(u"lineedit_trademark")
        self.lineedit_trademark.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_trademark, 4, 1, 1, 1)

        self.label_version = QLabel(copyright)
        self.label_version.setObjectName(u"label_version")

        self.gridLayout.addWidget(self.label_version, 1, 0, 1, 1)

        self.label_project = QLabel(copyright)
        self.label_project.setObjectName(u"label_project")

        self.gridLayout.addWidget(self.label_project, 0, 0, 1, 1)

        self.label_trademark = QLabel(copyright)
        self.label_trademark.setObjectName(u"label_trademark")

        self.gridLayout.addWidget(self.label_trademark, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.btn_select_icon, self.btn_clear_icon)
        QWidget.setTabOrder(self.btn_clear_icon, self.lineedit_project)
        QWidget.setTabOrder(self.lineedit_project, self.lineedit_version)
        QWidget.setTabOrder(self.lineedit_version, self.lineedit_company)
        QWidget.setTabOrder(self.lineedit_company, self.lineedit_copyright)
        QWidget.setTabOrder(self.lineedit_copyright, self.lineedit_trademark)

        self.retranslateUi(copyright)

        QMetaObject.connectSlotsByName(copyright)
    # setupUi

    def retranslateUi(self, copyright):
        copyright.setWindowTitle(QCoreApplication.translate("copyright", u"Form", None))
        self.btn_select_icon.setText(QCoreApplication.translate("copyright", u"\u9009\u62e9\u56fe\u6807", None))
        self.label_icon_path.setText("")
        self.label_icon_preview.setText("")
        self.btn_clear_icon.setText(QCoreApplication.translate("copyright", u"\u6e05\u7a7a", None))
        self.label_company.setText(QCoreApplication.translate("copyright", u"\u4f01\u4e1a\u540d\uff1a", None))
        self.lineedit_company.setText(QCoreApplication.translate("copyright", u"Avoconal", None))
        self.label_copyright.setText(QCoreApplication.translate("copyright", u"\u7248\u6743\uff1a", None))
        self.lineedit_version.setPlaceholderText(QCoreApplication.translate("copyright", u"\u6700\u591a\u56db\u4f4d\u6570\u5b57\u7248\u672c\u53f7", None))
        self.lineedit_copyright.setText(QCoreApplication.translate("copyright", u"abcdesteve", None))
        self.label_version.setText(QCoreApplication.translate("copyright", u"\u7248\u672c\uff1a", None))
        self.label_project.setText(QCoreApplication.translate("copyright", u"\u9879\u76ee\u540d\uff1a", None))
        self.label_trademark.setText(QCoreApplication.translate("copyright", u"\u5546\u6807\uff1a", None))
    # retranslateUi

