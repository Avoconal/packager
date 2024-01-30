# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_basic.ui'
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
    QListWidgetItem, QSizePolicy, QWidget)

from qfluentwidgets import (CheckBox, LineEdit, ListWidget, PrimaryPushButton,
    PushButton)

class Ui_basic(object):
    def setupUi(self, basic):
        if not basic.objectName():
            basic.setObjectName(u"basic")
        basic.resize(509, 301)
        self.gridLayout = QGridLayout(basic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_select_executor = PushButton(basic)
        self.btn_select_executor.setObjectName(u"btn_select_executor")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_executor.sizePolicy().hasHeightForWidth())
        self.btn_select_executor.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_select_executor)

        self.combobox_executor = QLabel(basic)
        self.combobox_executor.setObjectName(u"combobox_executor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combobox_executor.sizePolicy().hasHeightForWidth())
        self.combobox_executor.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(8)
        self.combobox_executor.setFont(font)
        self.combobox_executor.setScaledContents(True)
        self.combobox_executor.setWordWrap(True)

        self.horizontalLayout.addWidget(self.combobox_executor)

        self.chackbox_nuitka = CheckBox(basic)
        self.chackbox_nuitka.setObjectName(u"chackbox_nuitka")
        self.chackbox_nuitka.setEnabled(False)
        sizePolicy.setHeightForWidth(self.chackbox_nuitka.sizePolicy().hasHeightForWidth())
        self.chackbox_nuitka.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.chackbox_nuitka)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.plugin_list = ListWidget(basic)
        __qlistwidgetitem = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1 = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3 = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4 = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5 = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6 = QListWidgetItem(self.plugin_list)
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        self.plugin_list.setObjectName(u"plugin_list")
        self.plugin_list.setTabKeyNavigation(True)
        self.plugin_list.setAlternatingRowColors(True)
        self.plugin_list.setSpacing(1)

        self.gridLayout.addWidget(self.plugin_list, 2, 0, 5, 1)

        self.btn_start = PrimaryPushButton(basic)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(False)

        self.gridLayout.addWidget(self.btn_start, 6, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_addition = QLabel(basic)
        self.label_addition.setObjectName(u"label_addition")

        self.horizontalLayout_2.addWidget(self.label_addition)

        self.lineedit_addition = LineEdit(basic)
        self.lineedit_addition.setObjectName(u"lineedit_addition")

        self.horizontalLayout_2.addWidget(self.lineedit_addition)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 2)

        self.checkbox_onefile = CheckBox(basic)
        self.checkbox_onefile.setObjectName(u"checkbox_onefile")
        self.checkbox_onefile.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_onefile, 2, 1, 1, 1)

        self.checkbox_disable_console = CheckBox(basic)
        self.checkbox_disable_console.setObjectName(u"checkbox_disable_console")
        self.checkbox_disable_console.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_disable_console, 3, 1, 1, 1)

        self.checkbox_standalone = CheckBox(basic)
        self.checkbox_standalone.setObjectName(u"checkbox_standalone")
        self.checkbox_standalone.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_standalone, 4, 1, 1, 1)

        self.checkbox_require_admin = CheckBox(basic)
        self.checkbox_require_admin.setObjectName(u"checkbox_require_admin")

        self.gridLayout.addWidget(self.checkbox_require_admin, 5, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_select_file = PushButton(basic)
        self.btn_select_file.setObjectName(u"btn_select_file")
        sizePolicy.setHeightForWidth(self.btn_select_file.sizePolicy().hasHeightForWidth())
        self.btn_select_file.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btn_select_file)

        self.label_path_file = QLabel(basic)
        self.label_path_file.setObjectName(u"label_path_file")
        sizePolicy1.setHeightForWidth(self.label_path_file.sizePolicy().hasHeightForWidth())
        self.label_path_file.setSizePolicy(sizePolicy1)
        self.label_path_file.setFont(font)
        self.label_path_file.setScaledContents(True)
        self.label_path_file.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_path_file)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        QWidget.setTabOrder(self.btn_select_file, self.plugin_list)
        QWidget.setTabOrder(self.plugin_list, self.checkbox_onefile)
        QWidget.setTabOrder(self.checkbox_onefile, self.checkbox_disable_console)
        QWidget.setTabOrder(self.checkbox_disable_console, self.checkbox_standalone)
        QWidget.setTabOrder(self.checkbox_standalone, self.checkbox_require_admin)
        QWidget.setTabOrder(self.checkbox_require_admin, self.btn_start)
        QWidget.setTabOrder(self.btn_start, self.lineedit_addition)

        self.retranslateUi(basic)

        QMetaObject.connectSlotsByName(basic)
    # setupUi

    def retranslateUi(self, basic):
        basic.setWindowTitle(QCoreApplication.translate("basic", u"Form", None))
        self.btn_select_executor.setText(QCoreApplication.translate("basic", u"\u9009\u62e9\u89e3\u91ca\u5668", None))
        self.combobox_executor.setText("")
        self.chackbox_nuitka.setText(QCoreApplication.translate("basic", u"Nuitka", None))

        __sortingEnabled = self.plugin_list.isSortingEnabled()
        self.plugin_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.plugin_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("basic", u"matplotlib", None));
        ___qlistwidgetitem1 = self.plugin_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("basic", u"multiprocessing", None));
        ___qlistwidgetitem2 = self.plugin_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("basic", u"pyqt5", None));
        ___qlistwidgetitem3 = self.plugin_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("basic", u"pyqt6", None));
        ___qlistwidgetitem4 = self.plugin_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("basic", u"pyside2", None));
        ___qlistwidgetitem5 = self.plugin_list.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("basic", u"pyside6", None));
        ___qlistwidgetitem6 = self.plugin_list.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("basic", u"tk-inter", None));
        self.plugin_list.setSortingEnabled(__sortingEnabled)

        self.btn_start.setText(QCoreApplication.translate("basic", u"\u6253\u5305", None))
        self.label_addition.setText(QCoreApplication.translate("basic", u"\u989d\u5916\u53c2\u6570\uff1a", None))
        self.checkbox_onefile.setText(QCoreApplication.translate("basic", u"\u5355\u6587\u4ef6", None))
        self.checkbox_disable_console.setText(QCoreApplication.translate("basic", u"\u7981\u7528\u547d\u4ee4\u884c", None))
        self.checkbox_standalone.setText(QCoreApplication.translate("basic", u"\u5305\u542b\u8fd0\u884c\u73af\u5883", None))
        self.checkbox_require_admin.setText(QCoreApplication.translate("basic", u"\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650", None))
        self.btn_select_file.setText(QCoreApplication.translate("basic", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_path_file.setText("")
    # retranslateUi

