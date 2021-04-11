# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SEP_Login.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(389, 340)
        LoginForm.setAutoFillBackground(False)
        LoginForm.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #07C25C, stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #717072;\n"
"	border-bottom: 1px solid #717072;\n"
"}")
        self.LoginFrame = QFrame(LoginForm)
        self.LoginFrame.setObjectName(u"LoginFrame")
        self.LoginFrame.setGeometry(QRect(70, 30, 251, 281))
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
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.LoginButton.setFont(font)
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
        font1 = QFont()
        font1.setPointSize(10)
        self.Password.setFont(font1)
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
        self.Username.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Franklin Gothic Medium Cond")
        font2.setPointSize(12)
        self.CreateAccountButton.setFont(font2)
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
        font3 = QFont()
        font3.setFamily(u"Rockwell Condensed")
        font3.setPointSize(22)
        font3.setBold(False)
        self.LoginLabel.setFont(font3)
        self.LoginLabel.setStyleSheet(u"QLabel {\n"
"	color: white\n"
"}")
        self.LoginLabel.setAlignment(Qt.AlignCenter)
        self.LoginButton.raise_()
        self.Password.raise_()
        self.CreateAccountButton.raise_()
        self.LoginLabel.raise_()
        self.Username.raise_()

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Login", None))
        self.LoginButton.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.Password.setInputMask("")
        self.Password.setText(QCoreApplication.translate("LoginForm", u"Password", None))
#if QT_CONFIG(whatsthis)
        self.Username.setWhatsThis(QCoreApplication.translate("LoginForm", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Username.setText(QCoreApplication.translate("LoginForm", u"Username", None))
        self.Username.setPlaceholderText("")
        self.CreateAccountButton.setText(QCoreApplication.translate("LoginForm", u"Create Account", None))
        self.LoginLabel.setText(QCoreApplication.translate("LoginForm", u"Account Login", None))
    # retranslateUi

