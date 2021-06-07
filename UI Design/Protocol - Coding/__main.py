from PyQt5 import QtCore, QtGui, QtWidgets

from login import LoginWindow
from register import RegisterWindow
from search import SearchWindow
from cart import CartWindow
from sell_product import SellProductWindow

from os import environ


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == "__main__":
    import sys
    suppress_qt_warnings()

    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    search = SearchWindow()
    register = RegisterWindow()
    cart = CartWindow()
    sell_product = SellProductWindow()
    
    #connect login with the search page
    login.logged.connect(search.show)
    login.register.connect(register.show)
    register.login.connect(login.show)
    search.cart.connect(cart.show)
    cart.search.connect(search.show)

    search.sell_product.connect(sell_product.show)
    sell_product.search.connect(search.show)
    
    #show login page
    login.show()
    sys.exit(app.exec_())