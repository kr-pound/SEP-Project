# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
        MainWindow.resize(1014, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 200, 941, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 260, 101, 26))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 250, 61, 41))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 250, 141, 41))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(770, 250, 61, 31))
        self.label_7.setFont(font1)
        self.CoverFrame = QFrame(self.centralwidget)
        self.CoverFrame.setObjectName(u"CoverFrame")
        self.CoverFrame.setGeometry(QRect(150, 20, 711, 161))
        self.CoverFrame.setFocusPolicy(Qt.NoFocus)
        self.CoverFrame.setStyleSheet(u"QFrame {\n"
"	background: Black;\n"
"	border-radius: 40px;\n"
"}")
        self.CoverFrame.setFrameShape(QFrame.StyledPanel)
        self.CoverFrame.setFrameShadow(QFrame.Raised)
        self.KeywordInput = QLineEdit(self.CoverFrame)
        self.KeywordInput.setObjectName(u"KeywordInput")
        self.KeywordInput.setGeometry(QRect(210, 100, 301, 31))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setItalic(True)
        self.KeywordInput.setFont(font2)
        self.KeywordInput.setFocusPolicy(Qt.StrongFocus)
        self.KeywordInput.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.KeywordInput.setStyleSheet(u"QLineEdit {\n"
"	background: white;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: #717072;\n"
"}")
        self.KeywordInput.setEchoMode(QLineEdit.Normal)
        self.KeywordInput.setCursorPosition(15)
        self.KeywordInput.setDragEnabled(True)
        self.KeywordInput.setReadOnly(False)
        self.KeywordInput.setClearButtonEnabled(False)
        self.Search = QToolButton(self.CoverFrame)
        self.Search.setObjectName(u"Search")
        self.Search.setGeometry(QRect(480, 100, 31, 31))
        self.Search.setStyleSheet(u"QToolButton {\n"
"	background: transparent;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/search/search--v2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Search.setIcon(icon)
        self.CoverLabel = QLabel(self.CoverFrame)
        self.CoverLabel.setObjectName(u"CoverLabel")
        self.CoverLabel.setGeometry(QRect(210, 20, 301, 31))
        font3 = QFont()
        font3.setFamily(u"Rockwell Condensed")
        font3.setPointSize(22)
        self.CoverLabel.setFont(font3)
        self.CoverLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.CoverLabel.setAlignment(Qt.AlignCenter)
        self.DescriptionLabel = QLabel(self.CoverFrame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")
        self.DescriptionLabel.setGeometry(QRect(210, 60, 301, 31))
        font4 = QFont()
        font4.setFamily(u"Script MT Bold")
        font4.setPointSize(16)
        font4.setBold(True)
        self.DescriptionLabel.setFont(font4)
        self.DescriptionLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.DescriptionLabel.setAlignment(Qt.AlignCenter)
        self.BrandLabel = QLabel(self.CoverFrame)
        self.BrandLabel.setObjectName(u"BrandLabel")
        self.BrandLabel.setGeometry(QRect(10, 10, 71, 31))
        self.BrandLabel.setFont(font4)
        self.BrandLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.BrandLabel.setAlignment(Qt.AlignCenter)
        self.ProductFrame1 = QFrame(self.centralwidget)
        self.ProductFrame1.setObjectName(u"ProductFrame1")
        self.ProductFrame1.setGeometry(QRect(90, 300, 151, 331))
        self.ProductFrame1.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame1.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame1.setFrameShadow(QFrame.Raised)
        self.ProductPicture1 = QLabel(self.ProductFrame1)
        self.ProductPicture1.setObjectName(u"ProductPicture1")
        self.ProductPicture1.setGeometry(QRect(10, 10, 131, 91))
        self.ProductPicture1.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.ProductLabel1 = QLabel(self.ProductFrame1)
        self.ProductLabel1.setObjectName(u"ProductLabel1")
        self.ProductLabel1.setGeometry(QRect(10, 110, 101, 16))
        font5 = QFont()
        font5.setFamily(u"Franklin Gothic Medium Cond")
        font5.setPointSize(12)
        self.ProductLabel1.setFont(font5)
        self.ProductDescription1 = QTextBrowser(self.ProductFrame1)
        self.ProductDescription1.setObjectName(u"ProductDescription1")
        self.ProductDescription1.setGeometry(QRect(10, 130, 131, 121))
        font6 = QFont()
        font6.setFamily(u"Franklin Gothic Medium Cond")
        font6.setPointSize(10)
        self.ProductDescription1.setFont(font6)
        self.BuyingButton1 = QPushButton(self.ProductFrame1)
        self.BuyingButton1.setObjectName(u"BuyingButton1")
        self.BuyingButton1.setGeometry(QRect(20, 290, 111, 31))
        font7 = QFont()
        font7.setFamily(u"Franklin Gothic Medium Cond")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.BuyingButton1.setFont(font7)
        self.BuyingButton1.setStyleSheet(u"QPushButton {\n"
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
        self.ProductAmount1 = QLabel(self.ProductFrame1)
        self.ProductAmount1.setObjectName(u"ProductAmount1")
        self.ProductAmount1.setGeometry(QRect(20, 260, 111, 16))
        self.ProductAmount1.setFont(font5)
        self.ProductAmount1.setAlignment(Qt.AlignCenter)
        self.ProductIncrease1 = QPushButton(self.ProductFrame1)
        self.ProductIncrease1.setObjectName(u"ProductIncrease1")
        self.ProductIncrease1.setGeometry(QRect(110, 250, 21, 24))
        font8 = QFont()
        font8.setBold(True)
        self.ProductIncrease1.setFont(font8)
        self.ProductIncrease1.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease1 = QPushButton(self.ProductFrame1)
        self.ProductDecrease1.setObjectName(u"ProductDecrease1")
        self.ProductDecrease1.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease1.setFont(font8)
        self.ProductDecrease1.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductFrame3 = QFrame(self.centralwidget)
        self.ProductFrame3.setObjectName(u"ProductFrame3")
        self.ProductFrame3.setGeometry(QRect(430, 300, 151, 331))
        self.ProductFrame3.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame3.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame3.setFrameShadow(QFrame.Raised)
        self.ProductPicture3 = QLabel(self.ProductFrame3)
        self.ProductPicture3.setObjectName(u"ProductPicture3")
        self.ProductPicture3.setGeometry(QRect(10, 10, 131, 91))
        self.ProductPicture3.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.ProductLabel3 = QLabel(self.ProductFrame3)
        self.ProductLabel3.setObjectName(u"ProductLabel3")
        self.ProductLabel3.setGeometry(QRect(10, 110, 101, 16))
        self.ProductLabel3.setFont(font5)
        self.ProductDescription3 = QTextBrowser(self.ProductFrame3)
        self.ProductDescription3.setObjectName(u"ProductDescription3")
        self.ProductDescription3.setGeometry(QRect(10, 130, 131, 121))
        self.ProductDescription3.setFont(font6)
        self.BuyingButton3 = QPushButton(self.ProductFrame3)
        self.BuyingButton3.setObjectName(u"BuyingButton3")
        self.BuyingButton3.setGeometry(QRect(20, 290, 111, 31))
        self.BuyingButton3.setFont(font7)
        self.BuyingButton3.setStyleSheet(u"QPushButton {\n"
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
        self.ProductAmount3 = QLabel(self.ProductFrame3)
        self.ProductAmount3.setObjectName(u"ProductAmount3")
        self.ProductAmount3.setGeometry(QRect(20, 260, 111, 16))
        self.ProductAmount3.setFont(font5)
        self.ProductAmount3.setAlignment(Qt.AlignCenter)
        self.ProductIncrease3 = QPushButton(self.ProductFrame3)
        self.ProductIncrease3.setObjectName(u"ProductIncrease3")
        self.ProductIncrease3.setGeometry(QRect(110, 250, 21, 24))
        self.ProductIncrease3.setFont(font8)
        self.ProductIncrease3.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease3 = QPushButton(self.ProductFrame3)
        self.ProductDecrease3.setObjectName(u"ProductDecrease3")
        self.ProductDecrease3.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease3.setFont(font8)
        self.ProductDecrease3.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductFrame2 = QFrame(self.centralwidget)
        self.ProductFrame2.setObjectName(u"ProductFrame2")
        self.ProductFrame2.setGeometry(QRect(260, 300, 151, 331))
        self.ProductFrame2.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame2.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame2.setFrameShadow(QFrame.Raised)
        self.ProductPicture2 = QLabel(self.ProductFrame2)
        self.ProductPicture2.setObjectName(u"ProductPicture2")
        self.ProductPicture2.setGeometry(QRect(10, 10, 131, 91))
        self.ProductPicture2.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.ProductLabel2 = QLabel(self.ProductFrame2)
        self.ProductLabel2.setObjectName(u"ProductLabel2")
        self.ProductLabel2.setGeometry(QRect(10, 110, 101, 16))
        self.ProductLabel2.setFont(font5)
        self.ProductDescription2 = QTextBrowser(self.ProductFrame2)
        self.ProductDescription2.setObjectName(u"ProductDescription2")
        self.ProductDescription2.setGeometry(QRect(10, 130, 131, 121))
        self.ProductDescription2.setFont(font6)
        self.BuyingButton2 = QPushButton(self.ProductFrame2)
        self.BuyingButton2.setObjectName(u"BuyingButton2")
        self.BuyingButton2.setGeometry(QRect(20, 290, 111, 31))
        self.BuyingButton2.setFont(font7)
        self.BuyingButton2.setStyleSheet(u"QPushButton {\n"
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
        self.ProductAmount2 = QLabel(self.ProductFrame2)
        self.ProductAmount2.setObjectName(u"ProductAmount2")
        self.ProductAmount2.setGeometry(QRect(20, 260, 111, 16))
        self.ProductAmount2.setFont(font5)
        self.ProductAmount2.setAlignment(Qt.AlignCenter)
        self.ProductIncrease2 = QPushButton(self.ProductFrame2)
        self.ProductIncrease2.setObjectName(u"ProductIncrease2")
        self.ProductIncrease2.setGeometry(QRect(110, 250, 21, 24))
        self.ProductIncrease2.setFont(font8)
        self.ProductIncrease2.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease2 = QPushButton(self.ProductFrame2)
        self.ProductDecrease2.setObjectName(u"ProductDecrease2")
        self.ProductDecrease2.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease2.setFont(font8)
        self.ProductDecrease2.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductFrame4 = QFrame(self.centralwidget)
        self.ProductFrame4.setObjectName(u"ProductFrame4")
        self.ProductFrame4.setGeometry(QRect(600, 300, 151, 331))
        self.ProductFrame4.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame4.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame4.setFrameShadow(QFrame.Raised)
        self.ProductPicture4 = QLabel(self.ProductFrame4)
        self.ProductPicture4.setObjectName(u"ProductPicture4")
        self.ProductPicture4.setGeometry(QRect(10, 10, 131, 91))
        self.ProductPicture4.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.ProductLabel4 = QLabel(self.ProductFrame4)
        self.ProductLabel4.setObjectName(u"ProductLabel4")
        self.ProductLabel4.setGeometry(QRect(10, 110, 101, 16))
        self.ProductLabel4.setFont(font5)
        self.ProductDescription4 = QTextBrowser(self.ProductFrame4)
        self.ProductDescription4.setObjectName(u"ProductDescription4")
        self.ProductDescription4.setGeometry(QRect(10, 130, 131, 121))
        self.ProductDescription4.setFont(font6)
        self.BuyingButton4 = QPushButton(self.ProductFrame4)
        self.BuyingButton4.setObjectName(u"BuyingButton4")
        self.BuyingButton4.setGeometry(QRect(20, 290, 111, 31))
        self.BuyingButton4.setFont(font7)
        self.BuyingButton4.setStyleSheet(u"QPushButton {\n"
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
        self.ProductAmount4 = QLabel(self.ProductFrame4)
        self.ProductAmount4.setObjectName(u"ProductAmount4")
        self.ProductAmount4.setGeometry(QRect(20, 260, 111, 16))
        self.ProductAmount4.setFont(font5)
        self.ProductAmount4.setAlignment(Qt.AlignCenter)
        self.ProductIncrease4 = QPushButton(self.ProductFrame4)
        self.ProductIncrease4.setObjectName(u"ProductIncrease4")
        self.ProductIncrease4.setGeometry(QRect(110, 250, 21, 24))
        self.ProductIncrease4.setFont(font8)
        self.ProductIncrease4.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease4 = QPushButton(self.ProductFrame4)
        self.ProductDecrease4.setObjectName(u"ProductDecrease4")
        self.ProductDecrease4.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease4.setFont(font8)
        self.ProductDecrease4.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductFrame5 = QFrame(self.centralwidget)
        self.ProductFrame5.setObjectName(u"ProductFrame5")
        self.ProductFrame5.setGeometry(QRect(770, 300, 151, 331))
        self.ProductFrame5.setStyleSheet(u"QFrame {\n"
"	background: lightgray;\n"
"	border-radius: 30px;\n"
"}")
        self.ProductFrame5.setFrameShape(QFrame.StyledPanel)
        self.ProductFrame5.setFrameShadow(QFrame.Raised)
        self.ProductPicture5 = QLabel(self.ProductFrame5)
        self.ProductPicture5.setObjectName(u"ProductPicture5")
        self.ProductPicture5.setGeometry(QRect(10, 10, 131, 91))
        self.ProductPicture5.setStyleSheet(u"QLabel {\n"
"	image: url(:/)\n"
"}")
        self.ProductLabel5 = QLabel(self.ProductFrame5)
        self.ProductLabel5.setObjectName(u"ProductLabel5")
        self.ProductLabel5.setGeometry(QRect(10, 110, 101, 16))
        self.ProductLabel5.setFont(font5)
        self.ProductDescription5 = QTextBrowser(self.ProductFrame5)
        self.ProductDescription5.setObjectName(u"ProductDescription5")
        self.ProductDescription5.setGeometry(QRect(10, 130, 131, 121))
        self.ProductDescription5.setFont(font6)
        self.BuyingButton5 = QPushButton(self.ProductFrame5)
        self.BuyingButton5.setObjectName(u"BuyingButton5")
        self.BuyingButton5.setGeometry(QRect(20, 290, 111, 31))
        self.BuyingButton5.setFont(font7)
        self.BuyingButton5.setStyleSheet(u"QPushButton {\n"
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
        self.ProductAmount5 = QLabel(self.ProductFrame5)
        self.ProductAmount5.setObjectName(u"ProductAmount5")
        self.ProductAmount5.setGeometry(QRect(20, 260, 111, 16))
        self.ProductAmount5.setFont(font5)
        self.ProductAmount5.setAlignment(Qt.AlignCenter)
        self.ProductIncrease5 = QPushButton(self.ProductFrame5)
        self.ProductIncrease5.setObjectName(u"ProductIncrease5")
        self.ProductIncrease5.setGeometry(QRect(110, 250, 21, 24))
        self.ProductIncrease5.setFont(font8)
        self.ProductIncrease5.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease5 = QPushButton(self.ProductFrame5)
        self.ProductDecrease5.setObjectName(u"ProductDecrease5")
        self.ProductDecrease5.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease5.setFont(font8)
        self.ProductDecrease5.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.CartButton = QPushButton(self.centralwidget)
        self.CartButton.setObjectName(u"CartButton")
        self.CartButton.setGeometry(QRect(880, 20, 111, 31))
        self.CartButton.setFont(font7)
        self.CartButton.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background: lightgray;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"	background: lightblue;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.RightButton = QPushButton(self.centralwidget)
        self.RightButton.setObjectName(u"RightButton")
        self.RightButton.setGeometry(QRect(950, 420, 41, 41))
        self.RightButton.setFont(font7)
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
        self.LeftButton = QPushButton(self.centralwidget)
        self.LeftButton.setObjectName(u"LeftButton")
        self.LeftButton.setGeometry(QRect(20, 420, 41, 41))
        self.LeftButton.setFont(font7)
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
        self.RefreshButton = QPushButton(self.centralwidget)
        self.RefreshButton.setObjectName(u"RefreshButton")
        self.RefreshButton.setGeometry(QRect(880, 70, 111, 31))
        self.RefreshButton.setFont(font7)
        self.RefreshButton.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background: lightgray;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"	background: lightgreen;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.SellProductButton = QPushButton(self.centralwidget)
        self.SellProductButton.setObjectName(u"SellProductButton")
        self.SellProductButton.setGeometry(QRect(20, 20, 111, 31))
        self.SellProductButton.setFont(font7)
        self.SellProductButton.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background: lightgray;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"	background: lightblue;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1014, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Fresh! We only have fresh stuff here. All the items are organic & natural.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Vegetables", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fruits", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Daily products", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"OTOP", None))
#if QT_CONFIG(whatsthis)
        self.KeywordInput.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.KeywordInput.setText(QCoreApplication.translate("MainWindow", u"  Type keywords", None))
        self.KeywordInput.setPlaceholderText("")
        self.Search.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CoverLabel.setText(QCoreApplication.translate("MainWindow", u"Agricultural products", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"100+ Fresh Item for you", None))
        self.BrandLabel.setText(QCoreApplication.translate("MainWindow", u"Fresh", None))
        self.ProductPicture1.setText("")
        self.ProductLabel1.setText("")
        self.ProductDescription1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.BuyingButton1.setText(QCoreApplication.translate("MainWindow", u"0 Bath", None))
        self.ProductAmount1.setText(QCoreApplication.translate("MainWindow", u"Buy: 1", None))
        self.ProductIncrease1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ProductDecrease1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ProductPicture3.setText("")
        self.ProductLabel3.setText("")
        self.ProductDescription3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.BuyingButton3.setText(QCoreApplication.translate("MainWindow", u"0 Bath", None))
        self.ProductAmount3.setText(QCoreApplication.translate("MainWindow", u"Buy: 1", None))
        self.ProductIncrease3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ProductDecrease3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ProductPicture2.setText("")
        self.ProductLabel2.setText("")
        self.ProductDescription2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.BuyingButton2.setText(QCoreApplication.translate("MainWindow", u"0 Bath", None))
        self.ProductAmount2.setText(QCoreApplication.translate("MainWindow", u"Buy: 1", None))
        self.ProductIncrease2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ProductDecrease2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ProductPicture4.setText("")
        self.ProductLabel4.setText("")
        self.ProductDescription4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.BuyingButton4.setText(QCoreApplication.translate("MainWindow", u"0 Bath", None))
        self.ProductAmount4.setText(QCoreApplication.translate("MainWindow", u"Buy: 1", None))
        self.ProductIncrease4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ProductDecrease4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ProductPicture5.setText("")
        self.ProductLabel5.setText("")
        self.ProductDescription5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.BuyingButton5.setText(QCoreApplication.translate("MainWindow", u"0 Bath", None))
        self.ProductAmount5.setText(QCoreApplication.translate("MainWindow", u"Buy: 1", None))
        self.ProductIncrease5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ProductDecrease5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.CartButton.setText(QCoreApplication.translate("MainWindow", u"View Cart", None))
        self.RightButton.setText("")
        self.LeftButton.setText("")
        self.RefreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.SellProductButton.setText(QCoreApplication.translate("MainWindow", u"Sell Product", None))
    # retranslateUi

