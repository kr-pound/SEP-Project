# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
        MainWindow.resize(646, 413)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PageLabel = QLabel(self.centralwidget)
        self.PageLabel.setObjectName(u"PageLabel")
        self.PageLabel.setGeometry(QRect(30, 10, 231, 61))
        font = QFont()
        font.setPointSize(28)
        self.PageLabel.setFont(font)
        self.PageLabel.setStyleSheet(u"color: white;\n"
"background-color : \"rgb(0, 0, 0)\";\n"
"border-radius: 15px;\n"
"")
        self.ConfirmButton = QPushButton(self.centralwidget)
        self.ConfirmButton.setObjectName(u"ConfirmButton")
        self.ConfirmButton.setGeometry(QRect(270, 330, 75, 24))
        self.ConfirmButton.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background: #64AB25;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}")
        self.InfoLabel = QLabel(self.centralwidget)
        self.InfoLabel.setObjectName(u"InfoLabel")
        self.InfoLabel.setGeometry(QRect(40, 80, 271, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.InfoLabel.setFont(font1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 120, 591, 181))
        self.frame.setStyleSheet(u"background-color: rgb(116, 183, 46);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.UsernameLabel = QLabel(self.frame)
        self.UsernameLabel.setObjectName(u"UsernameLabel")
        self.UsernameLabel.setGeometry(QRect(20, 20, 81, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.UsernameLabel.setFont(font2)
        self.PasswordLabel = QLabel(self.frame)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setGeometry(QRect(20, 70, 101, 31))
        self.PasswordLabel.setFont(font2)
        self.RePasswordLabel = QLabel(self.frame)
        self.RePasswordLabel.setObjectName(u"RePasswordLabel")
        self.RePasswordLabel.setGeometry(QRect(20, 120, 141, 31))
        self.RePasswordLabel.setFont(font2)
        self.UsernameLineEdit = QLineEdit(self.frame)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")
        self.UsernameLineEdit.setGeometry(QRect(140, 20, 411, 31))
        self.UsernameLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.PasswordLineEdit = QLineEdit(self.frame)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setGeometry(QRect(140, 70, 411, 31))
        self.PasswordLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.RePasswordLineEdit = QLineEdit(self.frame)
        self.RePasswordLineEdit.setObjectName(u"RePasswordLineEdit")
        self.RePasswordLineEdit.setGeometry(QRect(140, 120, 411, 31))
        self.RePasswordLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 646, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PageLabel.setText(QCoreApplication.translate("MainWindow", u"Register page", None))
        self.ConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.InfoLabel.setText(QCoreApplication.translate("MainWindow", u"Please fill in below to register a new account.", None))
        self.UsernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.RePasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Re-Password:", None))
    # retranslateUi

