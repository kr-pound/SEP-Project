from PyQt5 import QtCore, QtGui, QtWidgets
from _cart_design import Ui_MainWindow as Ui_CartWindow
from __product import CartProductClass

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class CartWindow(QtWidgets.QMainWindow, Ui_CartWindow):
    search = QtCore.pyqtSignal()

    #list of product object in the cart
    buy_list = [None] * 5
    page = 1

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(CartWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> go back
        self.BackButton.clicked.connect(self.searchTransfer)

        #cart load button
        self.ReloadButton.clicked.connect(self.reload)

        self.LeftButton.clicked.connect(self.leftTransfer)
        self.RightButton.clicked.connect(self.rightTransfer)

        
    @QtCore.pyqtSlot()
    def searchTransfer(self):
        self.search.emit()
        self.close()

    def reload(self):
        self.clear_cart_label()

        buy_count = 0
        CartProductClass.buy_list = [None] * 6

        for product in CartProductClass.product:
            #add more cart space
            if (product != None):
                

                if (product.buy_amount > 0):
                    if (CartProductClass.buy_list[-1] != None):
                        CartProductClass.buy_list += [None] * 6

                    #put product object into buy_list
                    CartProductClass.buy_list[buy_count] = product
                    buy_count += 1
            else:
                break

        #label note in CartWindow
        print(CartProductClass.buy_list)

        self.label_product_cart_detail()
    
    #cart data label
    def label_product_cart_detail(self):
        page_index = self.page - 1

        if (CartProductClass.buy_list[0 + page_index * 6] != None):
            self.CartProductLabel1.setText(CartProductClass.buy_list[0 + page_index * 6].name)
        if (CartProductClass.buy_list[1 + page_index * 6] != None):
            self.CartProductLabel2.setText(CartProductClass.buy_list[1 + page_index * 6].name)
        if (CartProductClass.buy_list[2 + page_index * 6] != None):
            self.CartProductLabel3.setText(CartProductClass.buy_list[2 + page_index * 6].name)
        if (CartProductClass.buy_list[3 + page_index * 6] != None):
            self.CartProductLabel4.setText(CartProductClass.buy_list[3 + page_index * 6].name)
        if (CartProductClass.buy_list[4 + page_index * 6] != None):
            self.CartProductLabel5.setText(CartProductClass.buy_list[4 + page_index * 6].name)
        if (CartProductClass.buy_list[5 + page_index * 6] != None):
            self.CartProductLabel6.setText(CartProductClass.buy_list[5 + page_index * 6].name)

    def clear_cart_label(self):
        cleared_label = ""

        self.CartProductLabel1.setText(cleared_label)
        self.CartProductLabel2.setText(cleared_label)
        self.CartProductLabel3.setText(cleared_label)
        self.CartProductLabel4.setText(cleared_label)
        self.CartProductLabel5.setText(cleared_label)
        self.CartProductLabel6.setText(cleared_label)

    #change the page of product show
    def rightTransfer(self):
        if (self.page * 6 < len(CartProductClass.buy_list)):
            self.page += 1

            #reset product info
            self.reload()
    
    def leftTransfer(self):
        if (self.page > 1):
            self.page -= 1

            #reset product info
            self.reload()

        


