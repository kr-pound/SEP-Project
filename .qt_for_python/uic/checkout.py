# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkout.ui'
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
        MainWindow.resize(1010, 736)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 241, 61))
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 120, 171, 131))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 130, 541, 71))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 240, 91, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 240, 151, 41))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 340, 71, 41))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 340, 101, 31))
        self.label_6.setFont(font2)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 400, 541, 201))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(810, 580, 181, 91))
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton.setFont(font3)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(650, 50, 401, 261))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Check out:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name of product", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Quantity:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"num", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"num total", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Banking information/ after tranfer the money send proof to seller.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Test", None))
    # retranslateUi

