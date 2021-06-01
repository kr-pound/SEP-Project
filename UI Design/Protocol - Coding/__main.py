from PyQt5 import QtCore, QtGui, QtWidgets
from google.oauth2 import service_account

from login import LoginWindow
from register import RegisterWindow
from search import SearchWindow

from os import environ

#firebase import
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#path in local pc and database
service_account_path = "C:/Users/krita/Documents/GitHub/SEP-Project/UI Design/Protocol - Coding/serviceAccountKey.json"
database_url_path = "https://fresh-python-default-rtdb.asia-southeast1.firebasedatabase.app"
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred, {'databaseURL': database_url_path} )

#set ref to the root of database
ref = db.reference("/")

import json
with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)


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
    #connect login with the search page
    login.logged.connect(search.show)
    login.register.connect(register.show)
    register.login.connect(login.show)
    #show login page
    login.show()
    sys.exit(app.exec_())