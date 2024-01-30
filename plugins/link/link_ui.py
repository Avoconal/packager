# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'link.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QSizePolicy, QTableWidgetItem, QWidget)

from qfluentwidgets import (PrimaryPushButton, TableWidget)

class Ui_link(object):
    def setupUi(self, link):
        if not link.objectName():
            link.setObjectName(u"link")
        link.resize(500, 300)
        self.gridLayout = QGridLayout(link)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_file = QLabel(link)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setMaximumSize(QSize(16777215, 15))
        self.label_file.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_file, 0, 0, 1, 1)

        self.label_dir = QLabel(link)
        self.label_dir.setObjectName(u"label_dir")
        self.label_dir.setMaximumSize(QSize(16777215, 15))
        self.label_dir.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_dir, 0, 1, 1, 1)

        self.column_file = TableWidget(link)
        if (self.column_file.columnCount() < 2):
            self.column_file.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.column_file.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.column_file.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.column_file.setObjectName(u"column_file")
        self.column_file.setSortingEnabled(True)
        self.column_file.horizontalHeader().setProperty("showSortIndicator", True)
        self.column_file.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.column_file, 1, 0, 1, 1)

        self.column_dir = TableWidget(link)
        if (self.column_dir.columnCount() < 2):
            self.column_dir.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.column_dir.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.column_dir.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.column_dir.setObjectName(u"column_dir")
        self.column_dir.setSortingEnabled(True)
        self.column_dir.horizontalHeader().setProperty("showSortIndicator", True)
        self.column_dir.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.column_dir, 1, 1, 1, 1)

        self.btn_add = PrimaryPushButton(link)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout.addWidget(self.btn_add, 2, 0, 1, 1)

        self.btn_del = PrimaryPushButton(link)
        self.btn_del.setObjectName(u"btn_del")

        self.gridLayout.addWidget(self.btn_del, 2, 1, 1, 1)


        self.retranslateUi(link)

        QMetaObject.connectSlotsByName(link)
    # setupUi

    def retranslateUi(self, link):
        link.setWindowTitle(QCoreApplication.translate("link", u"Form", None))
        self.label_file.setText(QCoreApplication.translate("link", u"\u6587\u4ef6\u6620\u5c04", None))
        self.label_dir.setText(QCoreApplication.translate("link", u"\u76ee\u5f55\u6620\u5c04", None))
        ___qtablewidgetitem = self.column_file.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("link", u"\u6e90\u8def\u5f84", None));
        ___qtablewidgetitem1 = self.column_file.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("link", u"\u76ee\u6807\u8def\u5f84", None));
        ___qtablewidgetitem2 = self.column_dir.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("link", u"\u6e90\u8def\u5f84", None));
        ___qtablewidgetitem3 = self.column_dir.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("link", u"\u76ee\u6807\u8def\u5f84", None));
        self.btn_add.setText(QCoreApplication.translate("link", u"\u6dfb\u52a0", None))
        self.btn_del.setText(QCoreApplication.translate("link", u"\u5220\u9664", None))
    # retranslateUi

