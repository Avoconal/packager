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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

from qfluentwidgets import (CheckBox, DateEdit, LineEdit)

class Ui_license(object):
    def setupUi(self, license):
        if not license.objectName():
            license.setObjectName(u"license")
        license.resize(300, 216)
        self.gridLayout = QGridLayout(license)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkbox_switch = CheckBox(license)
        self.checkbox_switch.setObjectName(u"checkbox_switch")

        self.gridLayout.addWidget(self.checkbox_switch, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(117, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.checkbox_dark_mode = CheckBox(license)
        self.checkbox_dark_mode.setObjectName(u"checkbox_dark_mode")
        self.checkbox_dark_mode.setEnabled(False)
        self.checkbox_dark_mode.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_dark_mode, 0, 2, 1, 1)

        self.label_user = QLabel(license)
        self.label_user.setObjectName(u"label_user")

        self.gridLayout.addWidget(self.label_user, 1, 0, 1, 1)

        self.label_date = QLabel(license)
        self.label_date.setObjectName(u"label_date")

        self.gridLayout.addWidget(self.label_date, 2, 0, 1, 1)

        self.dateedit = DateEdit(license)
        self.dateedit.setObjectName(u"dateedit")
        self.dateedit.setEnabled(False)
        self.dateedit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateedit, 2, 1, 1, 2)

        self.label_bios_sn = QLabel(license)
        self.label_bios_sn.setObjectName(u"label_bios_sn")

        self.gridLayout.addWidget(self.label_bios_sn, 3, 0, 1, 1)

        self.label_system_sn = QLabel(license)
        self.label_system_sn.setObjectName(u"label_system_sn")

        self.gridLayout.addWidget(self.label_system_sn, 4, 0, 1, 1)

        self.label_disk_sn = QLabel(license)
        self.label_disk_sn.setObjectName(u"label_disk_sn")

        self.gridLayout.addWidget(self.label_disk_sn, 5, 0, 1, 1)

        self.label_link = QLabel(license)
        self.label_link.setObjectName(u"label_link")

        self.gridLayout.addWidget(self.label_link, 6, 0, 1, 1)

        self.lineedit_user = LineEdit(license)
        self.lineedit_user.setObjectName(u"lineedit_user")
        self.lineedit_user.setEnabled(False)
        self.lineedit_user.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_user, 1, 1, 1, 2)

        self.lineedit_bios_sn = LineEdit(license)
        self.lineedit_bios_sn.setObjectName(u"lineedit_bios_sn")
        self.lineedit_bios_sn.setEnabled(False)
        self.lineedit_bios_sn.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_bios_sn, 3, 1, 1, 2)

        self.lineedit_system_sn = LineEdit(license)
        self.lineedit_system_sn.setObjectName(u"lineedit_system_sn")
        self.lineedit_system_sn.setEnabled(False)
        self.lineedit_system_sn.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_system_sn, 4, 1, 1, 2)

        self.lineedit_disk_sn = LineEdit(license)
        self.lineedit_disk_sn.setObjectName(u"lineedit_disk_sn")
        self.lineedit_disk_sn.setEnabled(False)
        self.lineedit_disk_sn.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_disk_sn, 5, 1, 1, 2)

        self.lineedit_link = LineEdit(license)
        self.lineedit_link.setObjectName(u"lineedit_link")
        self.lineedit_link.setEnabled(False)
        self.lineedit_link.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineedit_link, 6, 1, 1, 2)

        QWidget.setTabOrder(self.checkbox_switch, self.checkbox_dark_mode)
        QWidget.setTabOrder(self.checkbox_dark_mode, self.lineedit_user)
        QWidget.setTabOrder(self.lineedit_user, self.dateedit)
        QWidget.setTabOrder(self.dateedit, self.lineedit_bios_sn)
        QWidget.setTabOrder(self.lineedit_bios_sn, self.lineedit_system_sn)
        QWidget.setTabOrder(self.lineedit_system_sn, self.lineedit_disk_sn)
        QWidget.setTabOrder(self.lineedit_disk_sn, self.lineedit_link)

        self.retranslateUi(license)

        QMetaObject.connectSlotsByName(license)
    # setupUi

    def retranslateUi(self, license):
        license.setWindowTitle(QCoreApplication.translate("license", u"Form", None))
        self.checkbox_switch.setText(QCoreApplication.translate("license", u"\u5f00\u542f\u6388\u6743", None))
        self.checkbox_dark_mode.setText(QCoreApplication.translate("license", u"\u6df1\u8272\u6a21\u5f0f", None))
        self.label_user.setText(QCoreApplication.translate("license", u"\u7528\u6237\u540d\uff1a", None))
        self.label_date.setText(QCoreApplication.translate("license", u"\u6388\u6743\u65f6\u95f4\uff1a", None))
        self.dateedit.setDisplayFormat(QCoreApplication.translate("license", u"yyyy \u5e74 MM \u6708 dd \u65e5", None))
        self.label_bios_sn.setText(QCoreApplication.translate("license", u"BIOS\u5e8f\u5217\u53f7\uff1a", None))
        self.label_system_sn.setText(QCoreApplication.translate("license", u"\u7cfb\u7edf\u5e8f\u5217\u53f7\uff1a", None))
        self.label_disk_sn.setText(QCoreApplication.translate("license", u"\u786c\u76d8\u5e8f\u5217\u53f7\uff1a", None))
        self.label_link.setText(QCoreApplication.translate("license", u"\u5728\u7ebf\u94fe\u63a5\uff1a", None))
    # retranslateUi

