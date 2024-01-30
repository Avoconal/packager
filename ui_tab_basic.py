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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_basic(object):
    def setupUi(self, basic):
        if not basic.objectName():
            basic.setObjectName(u"basic")
        basic.resize(300, 200)
        self.gridLayout = QGridLayout(basic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_select = QPushButton(basic)
        self.btn_select.setObjectName(u"btn_select")

        self.gridLayout.addWidget(self.btn_select, 0, 0, 1, 1)

        self.scroll_plugin = QScrollArea(basic)
        self.scroll_plugin.setObjectName(u"scroll_plugin")
        self.scroll_plugin.setWidgetResizable(True)
        self.plugin_list = QWidget()
        self.plugin_list.setObjectName(u"plugin_list")
        self.plugin_list.setGeometry(QRect(0, 0, 150, 272))
        self.verticalLayout = QVBoxLayout(self.plugin_list)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.matplotlib = QCheckBox(self.plugin_list)
        self.matplotlib.setObjectName(u"matplotlib")

        self.verticalLayout.addWidget(self.matplotlib)

        self.multiprocessing = QCheckBox(self.plugin_list)
        self.multiprocessing.setObjectName(u"multiprocessing")

        self.verticalLayout.addWidget(self.multiprocessing)

        self.numpy = QCheckBox(self.plugin_list)
        self.numpy.setObjectName(u"numpy")

        self.verticalLayout.addWidget(self.numpy)

        self.pyqt5 = QCheckBox(self.plugin_list)
        self.pyqt5.setObjectName(u"pyqt5")

        self.verticalLayout.addWidget(self.pyqt5)

        self.pyqt6 = QCheckBox(self.plugin_list)
        self.pyqt6.setObjectName(u"pyqt6")

        self.verticalLayout.addWidget(self.pyqt6)

        self.pyside2 = QCheckBox(self.plugin_list)
        self.pyside2.setObjectName(u"pyside2")

        self.verticalLayout.addWidget(self.pyside2)

        self.pyside6 = QCheckBox(self.plugin_list)
        self.pyside6.setObjectName(u"pyside6")

        self.verticalLayout.addWidget(self.pyside6)

        self.tensorflow = QCheckBox(self.plugin_list)
        self.tensorflow.setObjectName(u"tensorflow")

        self.verticalLayout.addWidget(self.tensorflow)

        self.tk_inter = QCheckBox(self.plugin_list)
        self.tk_inter.setObjectName(u"tk_inter")

        self.verticalLayout.addWidget(self.tk_inter)

        self.torch = QCheckBox(self.plugin_list)
        self.torch.setObjectName(u"torch")

        self.verticalLayout.addWidget(self.torch)

        self.scroll_plugin.setWidget(self.plugin_list)

        self.gridLayout.addWidget(self.scroll_plugin, 1, 0, 5, 2)

        self.checkbox_onefile = QCheckBox(basic)
        self.checkbox_onefile.setObjectName(u"checkbox_onefile")
        self.checkbox_onefile.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_onefile, 1, 2, 1, 1)

        self.checkbox_disable_console = QCheckBox(basic)
        self.checkbox_disable_console.setObjectName(u"checkbox_disable_console")
        self.checkbox_disable_console.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_disable_console, 2, 2, 1, 1)

        self.checkbox_standalone = QCheckBox(basic)
        self.checkbox_standalone.setObjectName(u"checkbox_standalone")
        self.checkbox_standalone.setChecked(True)

        self.gridLayout.addWidget(self.checkbox_standalone, 3, 2, 1, 1)

        self.checkbox_require_admin = QCheckBox(basic)
        self.checkbox_require_admin.setObjectName(u"checkbox_require_admin")

        self.gridLayout.addWidget(self.checkbox_require_admin, 4, 2, 1, 1)

        self.btn_start = QPushButton(basic)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(False)

        self.gridLayout.addWidget(self.btn_start, 5, 2, 1, 1)

        self.label_path = QLabel(basic)
        self.label_path.setObjectName(u"label_path")
        font = QFont()
        font.setPointSize(8)
        self.label_path.setFont(font)
        self.label_path.setScaledContents(True)
        self.label_path.setWordWrap(True)

        self.gridLayout.addWidget(self.label_path, 0, 1, 1, 2)


        self.retranslateUi(basic)

        QMetaObject.connectSlotsByName(basic)
    # setupUi

    def retranslateUi(self, basic):
        basic.setWindowTitle(QCoreApplication.translate("basic", u"Form", None))
        self.btn_select.setText(QCoreApplication.translate("basic", u"\u9009\u62e9\u6587\u4ef6", None))
        self.matplotlib.setText(QCoreApplication.translate("basic", u"matplotlib", None))
        self.multiprocessing.setText(QCoreApplication.translate("basic", u"multiprocessing", None))
        self.numpy.setText(QCoreApplication.translate("basic", u"numpy", None))
        self.pyqt5.setText(QCoreApplication.translate("basic", u"pyqt5", None))
        self.pyqt6.setText(QCoreApplication.translate("basic", u"pyqt6", None))
        self.pyside2.setText(QCoreApplication.translate("basic", u"pyside2", None))
        self.pyside6.setText(QCoreApplication.translate("basic", u"pyside6", None))
        self.tensorflow.setText(QCoreApplication.translate("basic", u"tensorflow", None))
        self.tk_inter.setText(QCoreApplication.translate("basic", u"tk-inter", None))
        self.torch.setText(QCoreApplication.translate("basic", u"torch", None))
        self.checkbox_onefile.setText(QCoreApplication.translate("basic", u"\u5355\u6587\u4ef6", None))
        self.checkbox_disable_console.setText(QCoreApplication.translate("basic", u"\u7981\u7528\u547d\u4ee4\u884c", None))
        self.checkbox_standalone.setText(QCoreApplication.translate("basic", u"\u5305\u542b\u8fd0\u884c\u73af\u5883", None))
        self.checkbox_require_admin.setText(QCoreApplication.translate("basic", u"\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650", None))
        self.btn_start.setText(QCoreApplication.translate("basic", u"\u6253\u5305", None))
        self.label_path.setText("")
    # retranslateUi

