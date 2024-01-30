# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(400, 200)
        gui.setMinimumSize(QSize(400, 200))
        gui.setMaximumSize(QSize(400, 200))
        self.centralwidget = QWidget(gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_path = QLabel(self.centralwidget)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(90, 5, 301, 31))
        font = QFont()
        font.setPointSize(8)
        self.label_path.setFont(font)
        self.label_path.setScaledContents(True)
        self.label_path.setWordWrap(True)
        self.button_select = QPushButton(self.centralwidget)
        self.button_select.setObjectName(u"button_select")
        self.button_select.setGeometry(QRect(5, 5, 81, 29))
        self.scroll_plugin = QScrollArea(self.centralwidget)
        self.scroll_plugin.setObjectName(u"scroll_plugin")
        self.scroll_plugin.setGeometry(QRect(5, 40, 241, 151))
        self.scroll_plugin.setWidgetResizable(True)
        self.plugin_list = QWidget()
        self.plugin_list.setObjectName(u"plugin_list")
        self.plugin_list.setGeometry(QRect(0, 0, 222, 345))
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
        self.checkbox_one_file = QCheckBox(self.centralwidget)
        self.checkbox_one_file.setObjectName(u"checkbox_one_file")
        self.checkbox_one_file.setGeometry(QRect(260, 40, 71, 26))
        self.checkbox_one_file.setChecked(True)
        self.checkbox_disable_console = QCheckBox(self.centralwidget)
        self.checkbox_disable_console.setObjectName(u"checkbox_disable_console")
        self.checkbox_disable_console.setGeometry(QRect(260, 70, 101, 26))
        self.checkbox_disable_console.setChecked(True)
        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setEnabled(False)
        self.button_start.setGeometry(QRect(260, 160, 121, 29))
        self.checkbox_require_admin = QCheckBox(self.centralwidget)
        self.checkbox_require_admin.setObjectName(u"checkbox_require_admin")
        self.checkbox_require_admin.setGeometry(QRect(260, 100, 131, 26))
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(10, 200, 81, 20))
        self.edit_name = QLineEdit(self.centralwidget)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setGeometry(QRect(100, 200, 291, 25))
        self.edit_version = QLineEdit(self.centralwidget)
        self.edit_version.setObjectName(u"edit_version")
        self.edit_version.setEnabled(False)
        self.edit_version.setGeometry(QRect(100, 230, 291, 25))
        self.label_version = QLabel(self.centralwidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(10, 230, 81, 20))
        self.edit_customer = QLineEdit(self.centralwidget)
        self.edit_customer.setObjectName(u"edit_customer")
        self.edit_customer.setEnabled(False)
        self.edit_customer.setGeometry(QRect(100, 260, 291, 25))
        self.edit_customer.setInputMethodHints(Qt.ImhUrlCharactersOnly)
        self.label_customer = QLabel(self.centralwidget)
        self.label_customer.setObjectName(u"label_customer")
        self.label_customer.setGeometry(QRect(10, 260, 81, 20))
        self.edit_os_sn = QLineEdit(self.centralwidget)
        self.edit_os_sn.setObjectName(u"edit_os_sn")
        self.edit_os_sn.setEnabled(False)
        self.edit_os_sn.setGeometry(QRect(100, 290, 291, 25))
        self.edit_os_sn.setInputMethodHints(Qt.ImhNone)
        self.label_os_sn = QLabel(self.centralwidget)
        self.label_os_sn.setObjectName(u"label_os_sn")
        self.label_os_sn.setGeometry(QRect(10, 290, 81, 20))
        self.label_disk_sn = QLabel(self.centralwidget)
        self.label_disk_sn.setObjectName(u"label_disk_sn")
        self.label_disk_sn.setGeometry(QRect(10, 320, 81, 20))
        self.edit_disk_sn = QLineEdit(self.centralwidget)
        self.edit_disk_sn.setObjectName(u"edit_disk_sn")
        self.edit_disk_sn.setEnabled(False)
        self.edit_disk_sn.setGeometry(QRect(100, 320, 291, 25))
        self.edit_disk_sn.setInputMethodHints(Qt.ImhUrlCharactersOnly)
        gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(gui)

        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"\u795e\u9f99\u5206\u53d1\u5668", None))
        self.label_path.setText("")
        self.button_select.setText(QCoreApplication.translate("gui", u"\u9009\u62e9\u6587\u4ef6", None))
        self.matplotlib.setText(QCoreApplication.translate("gui", u"matplotlib", None))
        self.multiprocessing.setText(QCoreApplication.translate("gui", u"multiprocessing", None))
        self.numpy.setText(QCoreApplication.translate("gui", u"numpy", None))
        self.pyqt5.setText(QCoreApplication.translate("gui", u"pyqt5", None))
        self.pyqt6.setText(QCoreApplication.translate("gui", u"pyqt6", None))
        self.pyside2.setText(QCoreApplication.translate("gui", u"pyside2", None))
        self.pyside6.setText(QCoreApplication.translate("gui", u"pyside6", None))
        self.tensorflow.setText(QCoreApplication.translate("gui", u"tensorflow", None))
        self.tk_inter.setText(QCoreApplication.translate("gui", u"tk-inter", None))
        self.torch.setText(QCoreApplication.translate("gui", u"torch", None))
        self.checkbox_one_file.setText(QCoreApplication.translate("gui", u"\u5355\u6587\u4ef6", None))
        self.checkbox_disable_console.setText(QCoreApplication.translate("gui", u"\u7981\u7528\u547d\u4ee4\u884c", None))
        self.button_start.setText(QCoreApplication.translate("gui", u"\u6253\u5305", None))
        self.checkbox_require_admin.setText(QCoreApplication.translate("gui", u"\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650", None))
        self.label_name.setText(QCoreApplication.translate("gui", u"\u5e94\u7528\u540d\u79f0\uff1a", None))
        self.edit_name.setPlaceholderText(QCoreApplication.translate("gui", u"\uff08\u53ef\u9009\uff09\u4e0d\u586b\u5219\u4e0d\u52a0\u5bc6", None))
        self.label_version.setText(QCoreApplication.translate("gui", u"\u5e94\u7528\u7248\u672c\uff1a", None))
        self.edit_customer.setText("")
        self.label_customer.setText(QCoreApplication.translate("gui", u"\u6388\u6743\u7ed9\uff1a", None))
        self.edit_os_sn.setText("")
        self.label_os_sn.setText(QCoreApplication.translate("gui", u"\u8bbe\u5907\u5e8f\u5217\u53f7\uff1a", None))
        self.label_disk_sn.setText(QCoreApplication.translate("gui", u"\u78c1\u76d8\u5e8f\u5217\u53f7\uff1a", None))
        self.edit_disk_sn.setText("")
    # retranslateUi

