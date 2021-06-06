from PyQt5 import QtCore, QtGui, QtWidgets
from google.oauth2 import service_account

#firebase import
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class database:
    username = None
    password = None

    def __init__(self):
        #path in local pc and database
        self.service_account_path = "C:/Users/krita/Documents/GitHub/SEP-Project/UI Design/Protocol - Coding/serviceAccountKey.json"
        self.database_url_path = "https://fresh-python-default-rtdb.asia-southeast1.firebasedatabase.app"
        self.cred = credentials.Certificate(self.service_account_path)
        self.default_app = firebase_admin.initialize_app(self.cred, {'databaseURL': self.database_url_path} )

        #set ref to the root of database
        self.ref = db.reference('/')

    #push data to database via ref
    def push(self, data, db_directory = '/'):
        self.ref = db.reference(db_directory)
        self.ref.push(data)

        #implementation
        #database().push({'username' : 'AB', 'password' : '123456'}, 'sub_dir_name')

    #return the data reference in database
    def __get_data(self, key, value, db_directory = '/'):
        ref = db.reference(db_directory)
        search_data = ref.order_by_child(key).equal_to(value).get()

        #for the first key found, return value
        for key, val in search_data.items():
                return val
            
    def is_visible(self, key, value, db_directory = '/'):
        self.ref = db.reference(db_directory)

        #check if the data is visible
        if self.__get_data(key, value, db_directory) != None:
            return True
        else:
            return False
        
        #implementation
        #print(database().is_visible('username', 'ABC', '/users'))
    
    def get_username_password(self, key, value, db_directory = '/'):
        val = self.__get_data(self, key, value, db_directory)

        self.username = None
        self.password = None

        #set username & password receive from __get_data()
        if val != None:
            self.username = val["username"]
            self.password = val["password"]

        #implementation
        #print(database().get_username_password('username', 'ABC', '/users'))


    def get_product(self, db_directory = '/'):
        ref = db.reference(db_directory)
        product_data = ref.get()

        product_list = []

        #put all product in the list
        for key, val in product_data.items():
            product_list.append(val)

        return product_list

        #implementation
        #print(database().get_product('/product'))

    #print all the list in directory
    def show_list(self, db_directory = '/', print_data = True):
        self.ref = db.reference(db_directory)
        data = self.ref.get()

        #determine when to print the data
        if (print_data):
            print(data)

        #implementation
        #print(database().show_list('/users'))

#database().push({'name' : 'Carrot6', 'id' : '6', 'price': '6', 'detail': 'Any carrot6 is good.'}, 'product')