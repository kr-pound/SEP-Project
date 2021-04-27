from PyQt5 import QtCore, QtGui, QtWidgets
from _login_design import Ui_MainWindow as Ui_LoginWindow
from register import Ui_MainWindow as Ui_RegisterWindow
from search import Ui_MainWindow as Ui_SearchWindow

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class RegisterWindow(QtWidgets.QMainWindow, Ui_RegisterWindow):
    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)

class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    logged = QtCore.pyqtSignal()
    register = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> check user id
        self.pushButton.clicked.connect(self.authenticate)
        self.pushButton_3.clicked.connect(self.registerTransfer)

    @QtCore.pyqtSlot()
    def registerTransfer(self):
        self.register.emit()
        self.close()

    @QtCore.pyqtSlot()
    def authenticate(self):
        #login and close the previous window
        self.logged.emit()
        self.close()

        '''
        db_user = self.username_ldt.text()
        db_pass = self.password_ldt.text()
        if db_user == 'admin' and db_pass=='admin':
            self.logged.emit()
            self.close()
        '''
    

    

if __name__ == "__main__":
    import sys
    suppress_qt_warnings()

    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    search = SearchWindow()
    register = RegisterWindow()
    #connect login with the search page
    login.logged.connect(search.show)
    login.register.connect(register.show)
    #show login page
    login.show()
    sys.exit(app.exec_())
