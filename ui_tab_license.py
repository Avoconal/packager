# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_license.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QGridLayout,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_license(object):
    def setupUi(self, license):
        if not license.objectName():
            license.setObjectName(u"license")
        license.resize(300, 200)
        self.gridLayout = QGridLayout(license)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkbox_switch = QCheckBox(license)
        self.checkbox_switch.setObjectName(u"checkbox_switch")

        self.gridLayout.addWidget(self.checkbox_switch, 0, 0, 1, 1)

        self.label_user = QLabel(license)
        self.label_user.setObjectName(u"label_user")

        self.gridLayout.addWidget(self.label_user, 1, 0, 1, 1)

        self.lineedit_user = QLineEdit(license)
        self.lineedit_user.setObjectName(u"lineedit_user")
        self.lineedit_user.setEnabled(False)

        self.gridLayout.addWidget(self.lineedit_user, 1, 1, 1, 1)

        self.label_date = QLabel(license)
        self.label_date.setObjectName(u"label_date")

        self.gridLayout.addWidget(self.label_date, 2, 0, 1, 1)

        self.dateedit = QDateEdit(license)
        self.dateedit.setObjectName(u"dateedit")
        self.dateedit.setEnabled(False)
        self.dateedit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateedit, 2, 1, 1, 1)

        self.label_bios_sn = QLabel(license)
        self.label_bios_sn.setObjectName(u"label_bios_sn")

        self.gridLayout.addWidget(self.label_bios_sn, 3, 0, 1, 1)

        self.lineedit_bios_sn = QLineEdit(license)
        self.lineedit_bios_sn.setObjectName(u"lineedit_bios_sn")
        self.lineedit_bios_sn.setEnabled(False)

        self.gridLayout.addWidget(self.lineedit_bios_sn, 3, 1, 1, 1)

        self.label_system_sn = QLabel(license)
        self.label_system_sn.setObjectName(u"label_system_sn")

        self.gridLayout.addWidget(self.label_system_sn, 4, 0, 1, 1)

        self.lineedit_system_sn = QLineEdit(license)
        self.lineedit_system_sn.setObjectName(u"lineedit_system_sn")
        self.lineedit_system_sn.setEnabled(False)

        self.gridLayout.addWidget(self.lineedit_system_sn, 4, 1, 1, 1)

        self.label_disk_sn = QLabel(license)
        self.label_disk_sn.setObjectName(u"label_disk_sn")

        self.gridLayout.addWidget(self.label_disk_sn, 5, 0, 1, 1)

        self.lineedit_disk_sn = QLineEdit(license)
        self.lineedit_disk_sn.setObjectName(u"lineedit_disk_sn")
        self.lineedit_disk_sn.setEnabled(False)

        self.gridLayout.addWidget(self.lineedit_disk_sn, 5, 1, 1, 1)


        self.retranslateUi(license)

        QMetaObject.connectSlotsByName(license)
    # setupUi

    def retranslateUi(self, license):
        license.setWindowTitle(QCoreApplication.translate("license", u"Form", None))
        self.checkbox_switch.setText(QCoreApplication.translate("license", u"\u5f00\u542f\u6388\u6743", None))
        self.label_user.setText(QCoreApplication.translate("license", u"\u7528\u6237\u540d\uff1a", None))
        self.label_date.setText(QCoreApplication.translate("license", u"\u6388\u6743\u65f6\u95f4\uff1a", None))
        self.dateedit.setDisplayFormat(QCoreApplication.translate("license", u"yyyy \u5e74 MM \u6708 dd \u65e5", None))
        self.label_bios_sn.setText(QCoreApplication.translate("license", u"BIOS\u5e8f\u5217\u53f7\uff1a", None))
        self.label_system_sn.setText(QCoreApplication.translate("license", u"\u7cfb\u7edf\u5e8f\u5217\u53f7\uff1a", None))
        self.label_disk_sn.setText(QCoreApplication.translate("license", u"\u786c\u76d8\u5e8f\u5217\u53f7\uff1a", None))
    # retranslateUi

