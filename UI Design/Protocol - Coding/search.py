from PyQt5 import QtCore, QtGui, QtWidgets
from _search_design import Ui_MainWindow as Ui_SearchWindow
from __product import CartProductClass

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class SearchWindow(QtWidgets.QMainWindow, Ui_SearchWindow):
    cart = QtCore.pyqtSignal()

    page = 1
    #the buying of product id
    buy_index = None

    cpClass = CartProductClass()
    

    def __init__(self, parent=None):
        #super the class to setup the Ui
        super(SearchWindow, self).__init__(parent)
        self.setupUi(self)

        #after push the button --> view cart
        self.CartButton.clicked.connect(self.cartTransfer)
        
        #product label color
        self.ProductLabel1.setStyleSheet("color: darkgreen;")
        self.ProductLabel2.setStyleSheet("color: darkgreen;")
        self.ProductLabel3.setStyleSheet("color: darkgreen;")
        self.ProductLabel4.setStyleSheet("color: darkgreen;")
        self.ProductLabel5.setStyleSheet("color: darkgreen;")

        #change pages to show product info
        self.RightButton.clicked.connect(self.rightTransfer)
        self.LeftButton.clicked.connect(self.leftTransfer)

        #increment button
        self.ProductIncrease1.clicked.connect(self.increment0)
        self.ProductIncrease2.clicked.connect(self.increment1)
        self.ProductIncrease3.clicked.connect(self.increment2)
        self.ProductIncrease4.clicked.connect(self.increment3)
        self.ProductIncrease5.clicked.connect(self.increment4)

        #buying button push --> send object to buy method
        self.BuyingButton1.clicked.connect(self.buy_index0)
        self.BuyingButton2.clicked.connect(self.buy_index1)
        self.BuyingButton3.clicked.connect(self.buy_index2)
        self.BuyingButton4.clicked.connect(self.buy_index3)
        self.BuyingButton5.clicked.connect(self.buy_index4)

        #insert product info
        self.cpClass.label_product_detail(1, 5, self.cpClass.product)
        self.set_product_detail()

    @QtCore.pyqtSlot()
    def cartTransfer(self):
        self.cart.emit()
        self.close()

    #change the page of product show
    def rightTransfer(self):
        if (self.page * 5 < len(self.cpClass.product_list)):
            self.page += 1

            #reset product info
            self.cpClass.clear_label_product_detail()
            self.set_product_detail()
            self.cpClass.label_product_detail(self.page, 5, self.cpClass.product)
            self.set_product_detail()
    
    def leftTransfer(self):
        if (self.page > 1):
            self.page -= 1

            #reset product info
            self.cpClass.clear_label_product_detail()
            self.set_product_detail()
            self.cpClass.label_product_detail(self.page, 5, self.cpClass.product)
            self.set_product_detail()

    #generated buy id & set buy_amount in each product object
    def buy_index0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount1.text().split()[-1])
            print("Buy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def buy_index1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount2.text().split()[-1])
            print("Buy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def buy_index2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount3.text().split()[-1])
            print("Buy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def buy_index3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount4.text().split()[-1])
            print("Buy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def buy_index4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount = int(self.ProductAmount5.text().split()[-1])
            print("Buy Amount: " + str(self.cpClass.product[self.buy_index].buy_amount))

    #label product amount
    def amount_label0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount1.setText("Buy: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def amount_label1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount1.setText("Buy: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def amount_label2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount1.setText("Buy: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def amount_label3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount1.setText("Buy: " + str(self.cpClass.product[self.buy_index].buy_amount))
    def amount_label4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)):
            self.ProductAmount1.setText("Buy: " + str(self.cpClass.product[self.buy_index].buy_amount))


    #increment button
    def increment0(self):
        self.buy_index = ((self.page - 1) * 5) + 0
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount += 1
            self.amount_label0()
    def increment1(self):
        self.buy_index = ((self.page - 1) * 5) + 1
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount += 1
            self.amount_label1()
    def increment2(self):
        self.buy_index = ((self.page - 1) * 5) + 2
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount += 1
            self.amount_label2()
    def increment3(self):
        self.buy_index = ((self.page - 1) * 5) + 3
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount += 1
            self.amount_label3()
    def increment4(self):
        self.buy_index = ((self.page - 1) * 5) + 4
        if (self.buy_index < len(self.cpClass.product_list)):
            self.cpClass.product[self.buy_index].buy_amount += 1
            self.amount_label4()

    #label product information
    def set_product_detail(self):
        self.ProductLabel1.setText(self.cpClass.productLabel1)
        self.BuyingButton1.setText(self.cpClass.buyingButton1)
        self.ProductDescription1.setText(self.cpClass.productDescription1)

        self.ProductLabel2.setText(self.cpClass.productLabel2)
        self.BuyingButton2.setText(self.cpClass.buyingButton2)
        self.ProductDescription2.setText(self.cpClass.productDescription2)

        self.ProductLabel3.setText(self.cpClass.productLabel3)
        self.BuyingButton3.setText(self.cpClass.buyingButton3)
        self.ProductDescription3.setText(self.cpClass.productDescription3)

        self.ProductLabel4.setText(self.cpClass.productLabel4)
        self.BuyingButton4.setText(self.cpClass.buyingButton4)
        self.ProductDescription4.setText(self.cpClass.productDescription4)

        self.ProductLabel5.setText(self.cpClass.productLabel5)
        self.BuyingButton5.setText(self.cpClass.buyingButton5)
        self.ProductDescription5.setText(self.cpClass.productDescription5)

    
    
        
