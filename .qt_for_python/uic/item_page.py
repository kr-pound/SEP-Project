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
        MainWindow.resize(725, 706)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(520, 560, 171, 81))
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium Cond")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: #64AB25;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #64AB25;\n"
"	background: #333;\n"
"	border-radius: 15px;\n"
"}")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 531, 61))
        font1 = QFont()
        font1.setFamily(u"Franklin Gothic Medium Cond")
        font1.setPointSize(48)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: white;\n"
"background-color : \"rgb(0, 0, 0)\";\n"
"border-radius: 15px;\n"
"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 110, 671, 421))
        self.frame.setStyleSheet(u"background-color: rgb(116, 183, 46);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 141, 61))
        font2 = QFont()
        font2.setFamily(u"Franklin Gothic Medium Cond")
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 151, 51))
        self.label_3.setFont(font2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 61, 61))
        self.label_2.setFont(font2)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 260, 141, 31))
        self.label_6.setFont(font2)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 200, 151, 41))
        self.label_4.setFont(font2)
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(210, 30, 411, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(210, 90, 411, 31))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(210, 150, 411, 31))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(210, 210, 411, 31))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_9 = QLineEdit(self.frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(210, 270, 411, 121))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 725, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"POST", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sell your product here:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name of item:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Product amount:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Detail:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Catagory:", None))
    # retranslateUi

