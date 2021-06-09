# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        MainWindow.resize(1011, 684)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #07C25C, stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #717072;\n"
"	border-bottom: 1px solid #717072;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 30, 231, 131))
        font = QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 150, 451, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 210, 711, 71))
        self.label_3.setFont(font1)
        self.LoginFrame = QFrame(self.centralwidget)
        self.LoginFrame.setObjectName(u"LoginFrame")
        self.LoginFrame.setGeometry(QRect(390, 320, 251, 281))
        self.LoginFrame.setFocusPolicy(Qt.NoFocus)
        self.LoginFrame.setStyleSheet(u"QFrame {\n"
"	background: black;\n"
"	border-radius: 20px;\n"
"}")
        self.LoginFrame.setFrameShape(QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QFrame.Raised)
        self.LoginButton = QPushButton(self.LoginFrame)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(110, 190, 111, 31))
        font2 = QFont()
        font2.setFamily(u"Franklin Gothic Medium Cond")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.LoginButton.setFont(font2)
        self.LoginButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: #64AB25;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #64AB25;\n"
"	background: #333;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.Password = QLineEdit(self.LoginFrame)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(30, 140, 191, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.Password.setFont(font3)
        self.Password.setStyleSheet(u"QLineEdit {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #717072;\n"
"	border-bottom: 1px solid #717072;\n"
"}")
        self.Password.setEchoMode(QLineEdit.Password)
        self.Password.setDragEnabled(True)
        self.Password.setClearButtonEnabled(True)
        self.Username = QLineEdit(self.LoginFrame)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(30, 100, 191, 21))
        self.Username.setFont(font3)
        self.Username.setFocusPolicy(Qt.StrongFocus)
        self.Username.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Username.setStyleSheet(u"")
        self.Username.setEchoMode(QLineEdit.Normal)
        self.Username.setCursorPosition(8)
        self.Username.setDragEnabled(True)
        self.Username.setReadOnly(False)
        self.Username.setClearButtonEnabled(True)
        self.CreateAccountButton = QPushButton(self.LoginFrame)
        self.CreateAccountButton.setObjectName(u"CreateAccountButton")
        self.CreateAccountButton.setGeometry(QRect(110, 230, 111, 31))
        font4 = QFont()
        font4.setFamily(u"Franklin Gothic Medium Cond")
        font4.setPointSize(12)
        self.CreateAccountButton.setFont(font4)
        self.CreateAccountButton.setStyleSheet(u"QPushButton {\n"
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
        self.LoginLabel = QLabel(self.LoginFrame)
        self.LoginLabel.setObjectName(u"LoginLabel")
        self.LoginLabel.setGeometry(QRect(0, 30, 251, 31))
        font5 = QFont()
        font5.setFamily(u"Rockwell Condensed")
        font5.setPointSize(22)
        font5.setBold(False)
        self.LoginLabel.setFont(font5)
        self.LoginLabel.setStyleSheet(u"QLabel {\n"
"	color: white\n"
"}")
        self.LoginLabel.setAlignment(Qt.AlignCenter)
        self.LoginButton.raise_()
        self.Password.raise_()
        self.CreateAccountButton.raise_()
        self.LoginLabel.raise_()
        self.Username.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fresh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to Fresh! We only sell fresh stuff here. ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Please log in or register an account if you don't have one before start using.", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Password.setInputMask("")
        self.Password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
#if QT_CONFIG(whatsthis)
        self.Username.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Username.setPlaceholderText("")
        self.CreateAccountButton.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.LoginLabel.setText(QCoreApplication.translate("MainWindow", u"Account Login", None))
    # retranslateUi

