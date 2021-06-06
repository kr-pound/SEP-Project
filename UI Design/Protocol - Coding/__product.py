from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow

from os import environ
from __database import database

#product store in class
class CartProductClass():
    product = [None] * 5
    product_list = None

    #product information
    productLabel1 = None
    productLabel2 = None
    productLabel3 = None
    productLabel4 = None
    productLabel5 = None

    buyingButton1 = None
    buyingButton2 = None
    buyingButton3 = None
    buyingButton4 = None
    buyingButton5 = None

    productDescription1 = None
    productDescription2 = None
    productDescription3 = None
    productDescription4 = None
    productDescription5 = None

    def __init__(self):
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

    #generate product information
    def label_product_detail(self, current_page, amount_per_page):
        page_index = current_page - 1

        if (self.product[0 + (amount_per_page * page_index)] != None):
            self.productLabel1 = self.product[0 + (amount_per_page * page_index)].name
            self.buyingButton1 = str(self.product[0 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription1 = "   " + self.product[0 + (amount_per_page * page_index)].detail

        if (self.product[1 + (amount_per_page * page_index)] != None):
            self.productLabel2 = self.product[1 + (amount_per_page * page_index)].name
            self.buyingButton2 = str(self.product[1 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription2 = "   " + self.product[1 + (amount_per_page * page_index)].detail

        if (self.product[2 + (amount_per_page * page_index)] != None):
            self.productLabel3 = self.product[2 + (amount_per_page * page_index)].name
            self.buyingButton3 = str(self.product[2 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription3 = "   " + self.product[0 + (amount_per_page * page_index)].detail

        if (self.product[3 + (amount_per_page * page_index)] != None):
            self.productLabel4 = self.product[3 + (amount_per_page * page_index)].name
            self.buyingButton4 = str(self.product[3 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription4 = "   " + self.product[3 + (amount_per_page * page_index)].detail

        if (self.product[4 + (amount_per_page * page_index)] != None):
            self.productLabel5 = self.product[4 + (amount_per_page * page_index)].name
            self.buyingButton5 = str(self.product[4 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription5 = "   " + self.product[4 + (amount_per_page * page_index)].detail


    #clear any product show
    def clear_label_product_detail(self):
        lebel_cleared = ""
        buying_button_cleaed = "0 Baht"
        description_cleared = ""

        self.productLabel1 = lebel_cleared
        self.productLabel2 = lebel_cleared
        self.productLabel3 = lebel_cleared
        self.productLabel4 = lebel_cleared
        self.productLabel5 = lebel_cleared

        self.buyingButton1 = buying_button_cleaed
        self.buyingButton2 = buying_button_cleaed
        self.buyingButton3 = buying_button_cleaed
        self.buyingButton4 = buying_button_cleaed
        self.buyingButton5 = buying_button_cleaed

        self.productDescription1 = description_cleared
        self.productDescription2 = description_cleared
        self.productDescription3 = description_cleared
        self.productDescription4 = description_cleared
        self.productDescription5 = description_cleared




#class of each product info
class ProductClass():
    id = None
    name = None
    price = None
    detail = None

    buy_amount = 0

    def __init__(self, id, name, price, detail):
        self.id = id
        self.name = name
        self.price = price
        self.detail = detail


