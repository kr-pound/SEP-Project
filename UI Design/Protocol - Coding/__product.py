from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow

from os import environ
from __database import database

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