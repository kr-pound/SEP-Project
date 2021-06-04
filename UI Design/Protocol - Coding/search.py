from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow

from os import environ
from __database import database

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

#class of each product info
class productClass():
    id = None
    name = None
    price = None
    detail = None

    def __init__(self, id, name, price, detail):
        self.id = id
        self.name = name
        self.price = price
        self.detail = detail


class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    product = None

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

        db = database()

        #receive product dictionary from database
        product_list = db.get_product('/product')
        #create list of each product object
        self.product = [None] * len(product_list)
        
        #store product objects in the list
        id_count = 0
        for product in product_list:
            #get any data from dictionary
            id = self.product[id_count] = product["id"]
            name = self.product[id_count] = product["name"]
            price = self.product[id_count] = product["price"]
            detail = self.product[id_count] = product["detail"]

            #store the object within a list
            self.product[id_count] = productClass(id, name, price, detail)
            id_count += 1

        self.label_product_detail(1)


    #label product information
    def label_product_detail(self, page):
        page_index = page - 1

        self.ProductLabel1.setText(self.product[0 + (4 * page_index)].name)
        self.ProductLabel2.setText(self.product[1 + (4 * page_index)].name)
        self.ProductLabel3.setText(self.product[2 + (4 * page_index)].name)

        self.BuyingButton1.setText(str(self.product[0 + (4 * page_index)].price) + " Baht")
        self.BuyingButton2.setText(str(self.product[1 + (4 * page_index)].price) + " Baht")
        self.BuyingButton3.setText(str(self.product[2 + (4 * page_index)].price) + " Baht")

        self.ProductDescription1.setText("   " + self.product[0 + (4 * page_index)].detail)
        self.ProductDescription2.setText("   " + self.product[1 + (4 * page_index)].detail)
        self.ProductDescription3.setText("   " + self.product[2 + (4 * page_index)].detail)

        
