# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pic_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 681)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 51))
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(770, 560, 201, 61))
        font1 = QFont()
        font1.setPointSize(18)
        self.pushButton_2.setFont(font1)
        self.ProductFrame1 = QFrame(self.centralwidget)
        self.ProductFrame1.setObjectName(u"ProductFrame1")
        self.ProductFrame1.setGeometry(QRect(50, 80, 441, 121))
        self.ProductFrame1.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame1.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame1.setFrameShadow(QFrame.Raised)
        self.DeleteButton1 = QPushButton(self.ProductFrame1)
        self.DeleteButton1.setObjectName(u"DeleteButton1")
        self.DeleteButton1.setGeometry(QRect(310, 80, 111, 31))
        font2 = QFont()
        font2.setFamily(u"Franklin Gothic Medium Cond")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.DeleteButton1.setFont(font2)
        self.DeleteButton1.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: red;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: darkred;\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartProductAmount1 = QLabel(self.ProductFrame1)
        self.CartProductAmount1.setObjectName(u"CartProductAmount1")
        self.CartProductAmount1.setGeometry(QRect(310, 50, 111, 16))
        font3 = QFont()
        font3.setFamily(u"Franklin Gothic Medium Cond")
        font3.setPointSize(12)
        self.CartProductAmount1.setFont(font3)
        self.CartProductAmount1.setAlignment(Qt.AlignCenter)
        self.CartProductLabel1 = QLabel(self.ProductFrame1)
        self.CartProductLabel1.setObjectName(u"CartProductLabel1")
        self.CartProductLabel1.setGeometry(QRect(170, 30, 121, 16))
        self.CartProductLabel1.setFont(font3)
        self.CartProductPicture1 = QLabel(self.ProductFrame1)
        self.CartProductPicture1.setObjectName(u"CartProductPicture1")
        self.CartProductPicture1.setGeometry(QRect(20, 20, 131, 91))
        self.CartProductPicture1.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.CartProductPrice1 = QLabel(self.ProductFrame1)
        self.CartProductPrice1.setObjectName(u"CartProductPrice1")
        self.CartProductPrice1.setGeometry(QRect(170, 90, 121, 16))
        self.CartProductPrice1.setFont(font3)
        self.BackButton = QPushButton(self.centralwidget)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(40, 570, 111, 31))
        self.BackButton.setFont(font2)
        self.BackButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: #64AB25;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #64AB25;\n"
"	background: #333;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.ReloadButton = QPushButton(self.centralwidget)
        self.ReloadButton.setObjectName(u"ReloadButton")
        self.ReloadButton.setGeometry(QRect(860, 510, 111, 31))
        self.ReloadButton.setFont(font2)
        self.ReloadButton.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background: lightgray;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: gray;\n"
"	background: lightblue;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.ProductFrame2 = QFrame(self.centralwidget)
        self.ProductFrame2.setObjectName(u"ProductFrame2")
        self.ProductFrame2.setGeometry(QRect(530, 80, 441, 121))
        self.ProductFrame2.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame2.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame2.setFrameShadow(QFrame.Raised)
        self.DeleteButton2 = QPushButton(self.ProductFrame2)
        self.DeleteButton2.setObjectName(u"DeleteButton2")
        self.DeleteButton2.setGeometry(QRect(310, 80, 111, 31))
        self.DeleteButton2.setFont(font2)
        self.DeleteButton2.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: red;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: darkred;\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartProductAmount2 = QLabel(self.ProductFrame2)
        self.CartProductAmount2.setObjectName(u"CartProductAmount2")
        self.CartProductAmount2.setGeometry(QRect(310, 50, 111, 16))
        self.CartProductAmount2.setFont(font3)
        self.CartProductAmount2.setAlignment(Qt.AlignCenter)
        self.CartProductLabel2 = QLabel(self.ProductFrame2)
        self.CartProductLabel2.setObjectName(u"CartProductLabel2")
        self.CartProductLabel2.setGeometry(QRect(170, 30, 121, 16))
        self.CartProductLabel2.setFont(font3)
        self.CartProductPicture2 = QLabel(self.ProductFrame2)
        self.CartProductPicture2.setObjectName(u"CartProductPicture2")
        self.CartProductPicture2.setGeometry(QRect(20, 20, 131, 91))
        self.CartProductPicture2.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.CartProductPrice2 = QLabel(self.ProductFrame2)
        self.CartProductPrice2.setObjectName(u"CartProductPrice2")
        self.CartProductPrice2.setGeometry(QRect(170, 90, 121, 16))
        self.CartProductPrice2.setFont(font3)
        self.ProductFrame3 = QFrame(self.centralwidget)
        self.ProductFrame3.setObjectName(u"ProductFrame3")
        self.ProductFrame3.setGeometry(QRect(50, 220, 441, 121))
        self.ProductFrame3.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame3.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame3.setFrameShadow(QFrame.Raised)
        self.DeleteButton3 = QPushButton(self.ProductFrame3)
        self.DeleteButton3.setObjectName(u"DeleteButton3")
        self.DeleteButton3.setGeometry(QRect(310, 80, 111, 31))
        self.DeleteButton3.setFont(font2)
        self.DeleteButton3.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: red;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: darkred;\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartProductAmount3 = QLabel(self.ProductFrame3)
        self.CartProductAmount3.setObjectName(u"CartProductAmount3")
        self.CartProductAmount3.setGeometry(QRect(310, 50, 111, 16))
        self.CartProductAmount3.setFont(font3)
        self.CartProductAmount3.setAlignment(Qt.AlignCenter)
        self.CartProductLabel3 = QLabel(self.ProductFrame3)
        self.CartProductLabel3.setObjectName(u"CartProductLabel3")
        self.CartProductLabel3.setGeometry(QRect(170, 30, 121, 16))
        self.CartProductLabel3.setFont(font3)
        self.CartProductPicture3 = QLabel(self.ProductFrame3)
        self.CartProductPicture3.setObjectName(u"CartProductPicture3")
        self.CartProductPicture3.setGeometry(QRect(20, 20, 131, 91))
        self.CartProductPicture3.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.CartProductPrice3 = QLabel(self.ProductFrame3)
        self.CartProductPrice3.setObjectName(u"CartProductPrice3")
        self.CartProductPrice3.setGeometry(QRect(170, 90, 121, 16))
        self.CartProductPrice3.setFont(font3)
        self.ProductFrame5 = QFrame(self.centralwidget)
        self.ProductFrame5.setObjectName(u"ProductFrame5")
        self.ProductFrame5.setGeometry(QRect(50, 360, 441, 121))
        self.ProductFrame5.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame5.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame5.setFrameShadow(QFrame.Raised)
        self.DeleteButton5 = QPushButton(self.ProductFrame5)
        self.DeleteButton5.setObjectName(u"DeleteButton5")
        self.DeleteButton5.setGeometry(QRect(310, 80, 111, 31))
        self.DeleteButton5.setFont(font2)
        self.DeleteButton5.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: red;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: darkred;\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartProductAmount5 = QLabel(self.ProductFrame5)
        self.CartProductAmount5.setObjectName(u"CartProductAmount5")
        self.CartProductAmount5.setGeometry(QRect(310, 50, 111, 16))
        self.CartProductAmount5.setFont(font3)
        self.CartProductAmount5.setAlignment(Qt.AlignCenter)
        self.CartProductLabel5 = QLabel(self.ProductFrame5)
        self.CartProductLabel5.setObjectName(u"CartProductLabel5")
        self.CartProductLabel5.setGeometry(QRect(170, 30, 121, 16))
        self.CartProductLabel5.setFont(font3)
        self.CartProductPicture5 = QLabel(self.ProductFrame5)
        self.CartProductPicture5.setObjectName(u"CartProductPicture5")
        self.CartProductPicture5.setGeometry(QRect(20, 20, 131, 91))
        self.CartProductPicture5.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.CartProductPrice5 = QLabel(self.ProductFrame5)
        self.CartProductPrice5.setObjectName(u"CartProductPrice5")
        self.CartProductPrice5.setGeometry(QRect(170, 90, 121, 16))
        self.CartProductPrice5.setFont(font3)
        self.ProductFrame4 = QFrame(self.centralwidget)
        self.ProductFrame4.setObjectName(u"ProductFrame4")
        self.ProductFrame4.setGeometry(QRect(530, 220, 441, 121))
        self.ProductFrame4.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame4.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame4.setFrameShadow(QFrame.Raised)
        self.DeleteButton4 = QPushButton(self.ProductFrame4)
        self.DeleteButton4.setObjectName(u"DeleteButton4")
        self.DeleteButton4.setGeometry(QRect(310, 80, 111, 31))
        self.DeleteButton4.setFont(font2)
        self.DeleteButton4.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: red;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: darkred;\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartProductAmount4 = QLabel(self.ProductFrame4)
        self.CartProductAmount4.setObjectName(u"CartProductAmount4")
        self.CartProductAmount4.setGeometry(QRect(310, 50, 111, 16))
        self.CartProductAmount4.setFont(font3)
        self.CartProductAmount4.setAlignment(Qt.AlignCenter)
        self.CartProductLabel4 = QLabel(self.ProductFrame4)
        self.CartProductLabel4.setObjectName(u"CartProductLabel4")
        self.CartProductLabel4.setGeometry(QRect(170, 30, 121, 16))
        self.CartProductLabel4.setFont(font3)
        self.CartProductPicture4 = QLabel(self.ProductFrame4)
        self.CartProductPicture4.setObjectName(u"CartProductPicture4")
        self.CartProductPicture4.setGeometry(QRect(20, 20, 131, 91))
        self.CartProductPicture4.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.CartProductPrice4 = QLabel(self.ProductFrame4)
        self.CartProductPrice4.setObjectName(u"CartProductPrice4")
        self.CartProductPrice4.setGeometry(QRect(170, 90, 121, 16))
        self.CartProductPrice4.setFont(font3)
        self.ProductFrame6 = QFrame(self.centralwidget)
        self.ProductFrame6.setObjectName(u"ProductFrame6")
        self.ProductFrame6.setGeometry(QRect(530, 360, 441, 121))
        self.ProductFrame6.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame6.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame6.setFrameShadow(QFrame.Raised)
        self.DeleteButton6 = QPushButton(self.ProductFrame6)
        self.DeleteButton6.setObjectName(u"DeleteButton6")
        self.DeleteButton6.setGeometry(QRect(310, 80, 111, 31))
        self.DeleteButton6.setFont(font2)
        self.DeleteButton6.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: red;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: darkred;\n"
"	background: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartProductAmount6 = QLabel(self.ProductFrame6)
        self.CartProductAmount6.setObjectName(u"CartProductAmount6")
        self.CartProductAmount6.setGeometry(QRect(310, 50, 111, 16))
        self.CartProductAmount6.setFont(font3)
        self.CartProductAmount6.setAlignment(Qt.AlignCenter)
        self.CartProductLabel6 = QLabel(self.ProductFrame6)
        self.CartProductLabel6.setObjectName(u"CartProductLabel6")
        self.CartProductLabel6.setGeometry(QRect(170, 30, 121, 16))
        self.CartProductLabel6.setFont(font3)
        self.CartProductPicture6 = QLabel(self.ProductFrame6)
        self.CartProductPicture6.setObjectName(u"CartProductPicture6")
        self.CartProductPicture6.setGeometry(QRect(20, 20, 131, 91))
        self.CartProductPicture6.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.CartProductPrice6 = QLabel(self.ProductFrame6)
        self.CartProductPrice6.setObjectName(u"CartProductPrice6")
        self.CartProductPrice6.setGeometry(QRect(170, 90, 121, 16))
        self.CartProductPrice6.setFont(font3)
        self.LeftButton = QPushButton(self.centralwidget)
        self.LeftButton.setObjectName(u"LeftButton")
        self.LeftButton.setGeometry(QRect(530, 510, 41, 41))
        self.LeftButton.setFont(font2)
        self.LeftButton.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"	border-radius: 20px;\n"
"	image: url(:/others/Arrow/leftArrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: lightgreen;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.RightButton = QPushButton(self.centralwidget)
        self.RightButton.setObjectName(u"RightButton")
        self.RightButton.setGeometry(QRect(630, 510, 41, 41))
        self.RightButton.setFont(font2)
        self.RightButton.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"	border-radius: 20px;\n"
"	image: url(:/others/Arrow/rightArrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: lightgreen;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1013, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cart:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Check out", None))
        self.DeleteButton1.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CartProductAmount1.setText(QCoreApplication.translate("MainWindow", u"Buy: 0", None))
        self.CartProductLabel1.setText("")
        self.CartProductPicture1.setText("")
        self.CartProductPrice1.setText("")
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.ReloadButton.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.DeleteButton2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CartProductAmount2.setText(QCoreApplication.translate("MainWindow", u"Buy: 0", None))
        self.CartProductLabel2.setText("")
        self.CartProductPicture2.setText("")
        self.CartProductPrice2.setText("")
        self.DeleteButton3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CartProductAmount3.setText(QCoreApplication.translate("MainWindow", u"Buy: 0", None))
        self.CartProductLabel3.setText("")
        self.CartProductPicture3.setText("")
        self.CartProductPrice3.setText("")
        self.DeleteButton5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CartProductAmount5.setText(QCoreApplication.translate("MainWindow", u"Buy: 0", None))
        self.CartProductLabel5.setText("")
        self.CartProductPicture5.setText("")
        self.CartProductPrice5.setText("")
        self.DeleteButton4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CartProductAmount4.setText(QCoreApplication.translate("MainWindow", u"Buy: 0", None))
        self.CartProductLabel4.setText("")
        self.CartProductPicture4.setText("")
        self.CartProductPrice4.setText("")
        self.DeleteButton6.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.CartProductAmount6.setText(QCoreApplication.translate("MainWindow", u"Buy: 0", None))
        self.CartProductLabel6.setText("")
        self.CartProductPicture6.setText("")
        self.CartProductPrice6.setText("")
        self.LeftButton.setText("")
        self.RightButton.setText("")
    # retranslateUi

