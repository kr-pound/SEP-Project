from PyQt5 import QtCore, QtGui, QtWidgets
from _login_design import Ui_MainWindow as Ui_LoginWindow
from search import Ui_MainWindow as Ui_SearchWindow

import pyrebase

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    logged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> check user id
        self.pushButton.clicked.connect(self.authenticate)

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
    #connect login with the search page
    login.logged.connect(search.show)
    #show login page
    login.show()
    sys.exit(app.exec_())


    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''