from PyQt5 import QtCore, QtGui, QtWidgets
from _register_design import Ui_MainWindow as Ui_RegisterWindow
from login import Ui_LoginWindow

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)

class RegisterWindow(QtWidgets.QMainWindow, Ui_RegisterWindow):
    login = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> go back
        self.pushButton.clicked.connect(self.loginTransfer)

    @QtCore.pyqtSlot()
    def loginTransfer(self):
        self.login.emit()
        self.close()


if __name__ == "__main__":
    import sys
    suppress_qt_warnings()

    app = QtWidgets.QApplication(sys.argv)
    register = RegisterWindow()
    login = LoginWindow()
    #connect login with the search page
    register.login.connect(login.show)
    #show login page
    register.show()
    sys.exit(app.exec_())