# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SEP_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from os import environ

#to get rid of QT_DEICE_PIXEL_RATIO warnings.
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(389, 340)
        LoginForm.setAutoFillBackground(False)
        LoginForm.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #07C25C, stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.LoginFrame = QtWidgets.QFrame(LoginForm)
        self.LoginFrame.setGeometry(QtCore.QRect(70, 30, 251, 281))
        self.LoginFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LoginFrame.setStyleSheet("QFrame {\n"
"    background: black;\n"
"    border-radius: 20px;\n"
"}")
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginFrame.setObjectName("LoginFrame")
        self.LoginButton = QtWidgets.QPushButton(self.LoginFrame)
        self.LoginButton.setGeometry(QtCore.QRect(110, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #64AB25;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.LoginButton.setObjectName("LoginButton")
        self.Password = QtWidgets.QLineEdit(self.LoginFrame)
        self.Password.setGeometry(QtCore.QRect(30, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px solid #717072;\n"
"}")
        self.Password.setInputMask("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setDragEnabled(True)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        self.Username = QtWidgets.QLineEdit(self.LoginFrame)
        self.Username.setGeometry(QtCore.QRect(30, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Username.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Username.setStyleSheet("")
        self.Username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Username.setCursorPosition(8)
        self.Username.setDragEnabled(True)
        self.Username.setReadOnly(False)
        self.Username.setPlaceholderText("")
        self.Username.setClearButtonEnabled(True)
        self.Username.setObjectName("Username")
        self.CreateAccountButton = QtWidgets.QPushButton(self.LoginFrame)
        self.CreateAccountButton.setGeometry(QtCore.QRect(110, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.CreateAccountButton.setFont(font)
        self.CreateAccountButton.setStyleSheet("QPushButton {\n"
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
        self.CreateAccountButton.setObjectName("CreateAccountButton")
        self.LoginLabel = QtWidgets.QLabel(self.LoginFrame)
        self.LoginLabel.setGeometry(QtCore.QRect(0, 30, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        font.setBold(False)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("QLabel {\n"
"    color: white\n"
"}")
        self.LoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginLabel.setObjectName("LoginLabel")
        self.LoginButton.raise_()
        self.Password.raise_()
        self.CreateAccountButton.raise_()
        self.LoginLabel.raise_()
        self.Username.raise_()

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.LoginButton.setText(_translate("LoginForm", "Login"))
        self.Password.setText(_translate("LoginForm", "Password"))
        self.Username.setWhatsThis(_translate("LoginForm", "<html><head/><body><p><br/></p></body></html>"))
        self.Username.setText(_translate("LoginForm", "Username"))
        self.CreateAccountButton.setText(_translate("LoginForm", "Create Account"))
        self.LoginLabel.setText(_translate("LoginForm", "Account Login"))


if __name__ == "__main__":
        #to get rid of QT_DEICE_PIXEL_RATIO warnings.
        suppress_qt_warnings()

        import sys

        app = QtWidgets.QApplication(sys.argv)
        LoginForm = QtWidgets.QWidget()
        ui = Ui_LoginForm()
        ui.setupUi(LoginForm)
        LoginForm.show()
        sys.exit(app.exec_())
