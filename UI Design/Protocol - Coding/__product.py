from PyQt5 import QtCore, QtGui, QtWidgets

from os import environ
from __database import database

#product store in class
class CartProductClass():
    product = [None] * 5
    product_list = None

    #buying product list
    buy_list = [None] * 6

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

    productAmount1 = 0
    productAmount2 = 0
    productAmount3 = 0
    productAmount4 = 0
    productAmount5 = 0


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
    def label_product_detail(self, current_page, amount_per_page, product_list):
        page_index = current_page - 1

        if (product_list[0 + (amount_per_page * page_index)] != None):
            self.productLabel1 = product_list[0 + (amount_per_page * page_index)].name
            self.buyingButton1 = str(product_list[0 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription1 = "   " + product_list[0 + (amount_per_page * page_index)].detail
            self.productAmount1 = product_list[0 + (amount_per_page * page_index)].buy_amount

        if (product_list[1 + (amount_per_page * page_index)] != None):
            self.productLabel2 = product_list[1 + (amount_per_page * page_index)].name
            self.buyingButton2 = str(product_list[1 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription2 = "   " + product_list[1 + (amount_per_page * page_index)].detail
            self.productAmount2 = product_list[1 + (amount_per_page * page_index)].buy_amount

        if (product_list[2 + (amount_per_page * page_index)] != None):
            self.productLabel3 = product_list[2 + (amount_per_page * page_index)].name
            self.buyingButton3 = str(product_list[2 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription3 = "   " + product_list[0 + (amount_per_page * page_index)].detail
            self.productAmount3 = product_list[2 + (amount_per_page * page_index)].buy_amount

        if (product_list[3 + (amount_per_page * page_index)] != None):
            self.productLabel4 = product_list[3 + (amount_per_page * page_index)].name
            self.buyingButton4 = str(product_list[3 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription4 = "   " + product_list[3 + (amount_per_page * page_index)].detail
            self.productAmount4 = product_list[3 + (amount_per_page * page_index)].buy_amount

        if (product_list[4 + (amount_per_page * page_index)] != None):
            self.productLabel5 = product_list[4 + (amount_per_page * page_index)].name
            self.buyingButton5 = str(product_list[4 + (amount_per_page * page_index)].price) + " Baht"
            self.productDescription5 = "   " + product_list[4 + (amount_per_page * page_index)].detail
            self.productAmount5 = product_list[4 + (amount_per_page * page_index)].buy_amount


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


