from PyQt5 import QtCore, QtGui, QtWidgets
from _sell_product_design import Ui_MainWindow as Ui_SellProductWindow
from __product import CartProductClass
from __database import database

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class SellProductWindow(QtWidgets.QMainWindow, Ui_SellProductWindow):
    search = QtCore.pyqtSignal()

    name = None
    price = 0
    detail = None
    category = None
    amount = 0

    #db = database

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SellProductWindow, self).__init__(parent)
        self.setupUi(self)

        #Transfer to Search page
        self.ConfirmButton.clicked.connect(self.receiveData)

    @QtCore.pyqtSlot()
    def searchTransfer(self):
        self.search.emit()
        self.close()

    def receiveData(self):
        self.name = self.NameLineEdit.text()
        self.price = self.PriceLineEdit.text()
        self.detail = self.DetailTextEdit.toPlainText()
        self.category = self.CategoryLineEdit.text()
        self.amount = self.AmountLineEdit.text()

        self.clear_lineEdit()

        if (self.price == '') or (self.amount == ''):
            print("Wrong Input")
        else:
            self.price = int(self.price)
            self.amount = int(self.amount)

            self.submitData()
            self.searchTransfer()

    #clear line edit after push button
    def clear_lineEdit(self):
        cleared_text = ""

        self.NameLineEdit.setText(cleared_text)
        self.PriceLineEdit.setText(cleared_text)
        self.DetailTextEdit.setPlainText(cleared_text)
        self.CategoryLineEdit.setText(cleared_text)
        self.AmountLineEdit.setText(cleared_text)

    #send data to __database.py
    def submitData(self):
        database.product_name = self.name
        database.product_price = self.price
        database.product_detail = self.detail
        database.product_category = self.category
        database.product_amount = self.amount

        database.push_product(database)
        

        
