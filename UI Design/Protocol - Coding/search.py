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

    product_list = None
    product = [None] * 5
    page = 1
    #the buying of product id
    buy_id = None

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> view cart
        self.CartButton.clicked.connect(self.cartTransfer)

        db = database()

        #receive product dictionary from database
        self.product_list = db.get_product('/product')
        #create list of each product object in page
        while(len(self.product) < len(self.product_list)):
            self.product += [None] * 5
        
        #store product objects in the list
        id_count = 0
        for product in self.product_list:
            #get any data from dictionary
            id = self.product[id_count] = product["id"]
            name = self.product[id_count] = product["name"]
            price = self.product[id_count] = product["price"]
            detail = self.product[id_count] = product["detail"]

            #store the object within a list
            self.product[id_count] = ProductClass(id, name, price, detail)
            id_count += 1

        print(self.product)

        #product label color
        self.ProductLabel1.setStyleSheet("color: darkgreen;")
        self.ProductLabel2.setStyleSheet("color: darkgreen;")
        self.ProductLabel3.setStyleSheet("color: darkgreen;")
        self.ProductLabel4.setStyleSheet("color: darkgreen;")
        self.ProductLabel5.setStyleSheet("color: darkgreen;")

        #insert product info
        self.label_product_detail(self.page, 5)

        #change pages to show product info
        self.RightButton.clicked.connect(self.rightTransfer)
        self.LeftButton.clicked.connect(self.leftTransfer)

        #buying button push --> send object to buy method
        self.BuyingButton1.clicked.connect(self.buy_id0)
        self.BuyingButton2.clicked.connect(self.buy_id1)
        self.BuyingButton3.clicked.connect(self.buy_id2)
        self.BuyingButton4.clicked.connect(self.buy_id3)
        self.BuyingButton5.clicked.connect(self.buy_id4)

    @QtCore.pyqtSlot()
    def cartTransfer(self):
        self.cart.emit()
        self.close()

    #change the page of product show
    def rightTransfer(self):
        if (self.page * 5 < len(self.product_list)):
            self.page += 1
            self.clear_label_product_detail()
            self.label_product_detail(self.page, 5)
    
    def leftTransfer(self):
        if (self.page > 1):
            self.page -= 1
            self.clear_label_product_detail()
            self.label_product_detail(self.page, 5)

    #generated buy id & set buy_amount in each product object
    def buy_id0(self):
        self.buy_id = ((self.page - 1) * 5) + 0
        if (self.buy_id < len(self.product_list)):
            self.product[self.buy_id].buy_amount = 1
    def buy_id1(self):
        self.buy_id = ((self.page - 1) * 5) + 1
        if (self.buy_id < len(self.product_list)):
            self.product[self.buy_id].buy_amount = 1
    def buy_id2(self):
        self.buy_id = ((self.page - 1) * 5) + 2
        if (self.buy_id < len(self.product_list)):
            self.product[self.buy_id].buy_amount = 1
    def buy_id3(self):
        self.buy_id = ((self.page - 1) * 5) + 3
        if (self.buy_id < len(self.product_list)):
            self.product[self.buy_id].buy_amount = 1
    def buy_id4(self):
        self.buy_id = ((self.page - 1) * 5) + 4
        if (self.buy_id < len(self.product_list)):
            self.product[self.buy_id].buy_amount = 1


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

    #clear any product show
    def clear_label_product_detail(self):
        lebel_cleared = ""
        buying_button_cleaed = "0 Baht"
        description_cleared = ""

        self.ProductLabel1.setText(lebel_cleared)
        self.ProductLabel2.setText(lebel_cleared)
        self.ProductLabel3.setText(lebel_cleared)
        self.ProductLabel4.setText(lebel_cleared)
        self.ProductLabel5.setText(lebel_cleared)

        self.BuyingButton1.setText(buying_button_cleaed)
        self.BuyingButton2.setText(buying_button_cleaed)
        self.BuyingButton3.setText(buying_button_cleaed)
        self.BuyingButton4.setText(buying_button_cleaed)
        self.BuyingButton5.setText(buying_button_cleaed)

        self.ProductDescription1.setText(description_cleared)
        self.ProductDescription2.setText(description_cleared)
        self.ProductDescription3.setText(description_cleared)
        self.ProductDescription4.setText(description_cleared)
        self.ProductDescription5.setText(description_cleared)
        
    def increment(self, id):
        pass
        
