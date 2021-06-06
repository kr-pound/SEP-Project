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

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(CartWindow, self).__init__(parent)
        self.setupUi(self)
        #after push the button --> go back
        self.BackButton.clicked.connect(self.searchTransfer)

        #cart load button
        self.ReloadButton.clicked.connect(self.reload)

        self.CartProductLabel1.setText("None")

        
    @QtCore.pyqtSlot()
    def searchTransfer(self):
        self.search.emit()
        self.close()

    def reload(self):
        buy_count = 0
        CartProductClass.buy_list = [None] * 5

        for product in CartProductClass.product:
            #add more cart space
            if (product != None):
                if (buy_count % 5) and (buy_count > 0) and (product.buy_amount > 0):
                    CartProductClass.buy_list += [None] * 5
                    print("adding buy_count")

                if (product.buy_amount > 0):
                    #put product object into buy_list
                    CartProductClass.buy_list[buy_count] = product
                    buy_count += 1
            else:
                break

        #label note in CartWindow
        print(CartProductClass.buy_list)
        
        #print(CartProductClass.buy_list[0].name)

        self.CartProductLabel1.setText(CartProductClass.buy_list[0].name)

        


        


