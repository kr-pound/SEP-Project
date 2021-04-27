from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow

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
