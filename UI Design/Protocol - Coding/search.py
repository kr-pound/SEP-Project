from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow
from __product import ProductClass

from os import environ
from __database import database

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    cart = QtCore.pyqtSignal()

    product = [None] * 5

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> view cart
        self.CartButton.clicked.connect(self.cartTransfer)

        db = database()

        #receive product dictionary from database
        product_list = db.get_product('/product')
        #create list of each product object in page
        while(len(self.product) < len(product_list)):
            self.product += [None] * 5
        
        #store product objects in the list
        id_count = 0
        for product in product_list:
            #get any data from dictionary
            id = self.product[id_count] = product["id"]
            name = self.product[id_count] = product["name"]
            price = self.product[id_count] = product["price"]
            detail = self.product[id_count] = product["detail"]

            #store the object within a list
            self.product[id_count] = ProductClass(id, name, price, detail)
            id_count += 1

        #product label color
        self.ProductLabel1.setStyleSheet("color: darkgreen;")
        self.ProductLabel2.setStyleSheet("color: darkgreen;")
        self.ProductLabel3.setStyleSheet("color: darkgreen;")

        #insert product info
        self.label_product_detail(1, 5)

        self.ProductIncrease1.clicked.connect(self.increment)

    @QtCore.pyqtSlot()
    def cartTransfer(self):
        self.cart.emit()
        self.close()


    #label product information
    def label_product_detail(self, current_page, amount_per_page):
        page_index = current_page - 1

        if (self.product[0 + (amount_per_page * page_index)] != None):
            self.ProductLabel1.setText(self.product[0 + (amount_per_page * page_index)].name)
            self.BuyingButton1.setText(str(self.product[0 + (amount_per_page * page_index)].price) + " Baht")
            self.ProductDescription1.setText("   " + self.product[0 + (amount_per_page * page_index)].detail)

        if (self.product[1 + (amount_per_page * page_index)] != None):
            self.ProductLabel2.setText(self.product[1 + (amount_per_page * page_index)].name)
            self.BuyingButton2.setText(str(self.product[1 + (amount_per_page * page_index)].price) + " Baht")
            self.ProductDescription2.setText("   " + self.product[1 + (amount_per_page * page_index)].detail)

        if (self.product[2 + (amount_per_page * page_index)] != None):
            self.ProductLabel3.setText(self.product[2 + (amount_per_page * page_index)].name)
            self.BuyingButton3.setText(str(self.product[2 + (amount_per_page * page_index)].price) + " Baht")
            self.ProductDescription3.setText("   " + self.product[2 + (amount_per_page * page_index)].detail)

        if (self.product[3 + (amount_per_page * page_index)] != None):
            self.ProductLabel4.setText(self.product[3 + (amount_per_page * page_index)].name)
            self.BuyingButton4.setText(str(self.product[3 + (amount_per_page * page_index)].price) + " Baht")
            self.ProductDescription4.setText("   " + self.product[3 + (amount_per_page * page_index)].detail)

        if (self.product[4 + (amount_per_page * page_index)] != None):
            self.ProductLabel5.setText(self.product[4 + (amount_per_page * page_index)].name)
            self.BuyingButton5.setText(str(self.product[4 + (amount_per_page * page_index)].price) + " Baht")
            self.ProductDescription5.setText("   " + self.product[4 + (amount_per_page * page_index)].detail)
        
    def increment(self, id):
        pass
        
