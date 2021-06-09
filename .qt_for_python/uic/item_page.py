# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_page.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 890)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(210, 10, 611, 291))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 320, 941, 61))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 410, 61, 61))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 500, 61, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 510, 151, 41))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 420, 101, 41))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 590, 141, 31))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 590, 191, 31))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 660, 411, 161))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 710, 201, 91))
        font2 = QFont()
        font2.setPointSize(20)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(780, 710, 181, 91))
        self.pushButton_2.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name of item", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stock:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"number of stock", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Date of pickup: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"more information about product/ ad", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add to cart", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
    # retranslateUi

