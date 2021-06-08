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
        MainWindow.resize(843, 318)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 261, 61))
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium Cond")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"background-color : \"rgb(0, 0, 0)\";\n"
"border-radius: 15px;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 541, 31))
        font1 = QFont()
        font1.setFamily(u"Franklin Gothic Medium Cond")
        font1.setPointSize(12)
        self.label_7.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(630, 140, 181, 91))
        font2 = QFont()
        font2.setFamily(u"Franklin Gothic Medium Cond")
        font2.setPointSize(36)
        self.pushButton.setFont(font2)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 140, 551, 81))
        self.frame.setStyleSheet(u"background-color: rgb(116, 183, 46);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 71, 41))
        font3 = QFont()
        font3.setFamily(u"Franklin Gothic Medium Cond")
        font3.setPointSize(16)
        self.label_5.setFont(font3)
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(90, 20, 411, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 843, 22))
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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Banking information/ after tranfer the money send proof to seller.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
    # retranslateUi

