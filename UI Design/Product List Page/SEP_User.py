# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SEP_User.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pic_rc

class Ui_UserForm(object):
    def setupUi(self, UserForm):
        if not UserForm.objectName():
            UserForm.setObjectName(u"UserForm")
        UserForm.resize(791, 638)
        UserForm.setStyleSheet(u"QWidget {\n"
"	background-image: url(:/bg/green-slate.jpg);\n"
"}")
        self.CoverFrame = QFrame(UserForm)
        self.CoverFrame.setObjectName(u"CoverFrame")
        self.CoverFrame.setGeometry(QRect(40, 20, 711, 161))
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
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.KeywordInput.setFont(font)
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
        font1 = QFont()
        font1.setFamily(u"Rockwell Condensed")
        font1.setPointSize(22)
        self.CoverLabel.setFont(font1)
        self.CoverLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.CoverLabel.setAlignment(Qt.AlignCenter)
        self.DescriptionLabel = QLabel(self.CoverFrame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")
        self.DescriptionLabel.setGeometry(QRect(210, 60, 301, 31))
        font2 = QFont()
        font2.setFamily(u"Script MT Bold")
        font2.setPointSize(16)
        font2.setBold(True)
        self.DescriptionLabel.setFont(font2)
        self.DescriptionLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.DescriptionLabel.setAlignment(Qt.AlignCenter)
        self.BrandLabel = QLabel(self.CoverFrame)
        self.BrandLabel.setObjectName(u"BrandLabel")
        self.BrandLabel.setGeometry(QRect(10, 10, 71, 31))
        self.BrandLabel.setFont(font2)
        self.BrandLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.BrandLabel.setAlignment(Qt.AlignCenter)
        self.ProductFrame1 = QFrame(UserForm)
        self.ProductFrame1.setObjectName(u"ProductFrame1")
        self.ProductFrame1.setGeometry(QRect(40, 220, 151, 331))
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
"	image: url(:/real product/carrot_PNG4985.png);\n"
"}")
        self.ProductLabel1 = QLabel(self.ProductFrame1)
        self.ProductLabel1.setObjectName(u"ProductLabel1")
        self.ProductLabel1.setGeometry(QRect(10, 110, 101, 16))
        font3 = QFont()
        font3.setFamily(u"Franklin Gothic Medium Cond")
        font3.setPointSize(12)
        self.ProductLabel1.setFont(font3)
        self.ProductDescription1 = QTextBrowser(self.ProductFrame1)
        self.ProductDescription1.setObjectName(u"ProductDescription1")
        self.ProductDescription1.setGeometry(QRect(10, 130, 131, 121))
        font4 = QFont()
        font4.setFamily(u"Franklin Gothic Medium Cond")
        font4.setPointSize(10)
        self.ProductDescription1.setFont(font4)
        self.BuyingButton1 = QPushButton(self.ProductFrame1)
        self.BuyingButton1.setObjectName(u"BuyingButton1")
        self.BuyingButton1.setGeometry(QRect(20, 290, 111, 31))
        font5 = QFont()
        font5.setFamily(u"Franklin Gothic Medium Cond")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.BuyingButton1.setFont(font5)
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
        self.ProductAmount1.setFont(font3)
        self.ProductAmount1.setAlignment(Qt.AlignCenter)
        self.ProductIncrease1 = QPushButton(self.ProductFrame1)
        self.ProductIncrease1.setObjectName(u"ProductIncrease1")
        self.ProductIncrease1.setGeometry(QRect(110, 250, 21, 24))
        font6 = QFont()
        font6.setBold(True)
        self.ProductIncrease1.setFont(font6)
        self.ProductIncrease1.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease1 = QPushButton(self.ProductFrame1)
        self.ProductDecrease1.setObjectName(u"ProductDecrease1")
        self.ProductDecrease1.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease1.setFont(font6)
        self.ProductDecrease1.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.LoadMoreButton = QPushButton(UserForm)
        self.LoadMoreButton.setObjectName(u"LoadMoreButton")
        self.LoadMoreButton.setGeometry(QRect(340, 580, 111, 31))
        self.LoadMoreButton.setFont(font3)
        self.LoadMoreButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background: #64AB25;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #64AB25;\n"
"	background: #333;\n"
"	border-radius: 15px;\n"
"}")
        self.ProductFrame2 = QFrame(UserForm)
        self.ProductFrame2.setObjectName(u"ProductFrame2")
        self.ProductFrame2.setGeometry(QRect(220, 220, 151, 331))
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
"	\n"
"	image: url(:/real product/wheat_PNG85.png);\n"
"}")
        self.ProductLabel2 = QLabel(self.ProductFrame2)
        self.ProductLabel2.setObjectName(u"ProductLabel2")
        self.ProductLabel2.setGeometry(QRect(10, 110, 101, 16))
        self.ProductLabel2.setFont(font3)
        self.ProductDescription2 = QTextBrowser(self.ProductFrame2)
        self.ProductDescription2.setObjectName(u"ProductDescription2")
        self.ProductDescription2.setGeometry(QRect(10, 130, 131, 121))
        self.ProductDescription2.setFont(font4)
        self.BuyingButton2 = QPushButton(self.ProductFrame2)
        self.BuyingButton2.setObjectName(u"BuyingButton2")
        self.BuyingButton2.setGeometry(QRect(20, 290, 111, 31))
        self.BuyingButton2.setFont(font5)
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
        self.ProductAmount2.setFont(font3)
        self.ProductAmount2.setAlignment(Qt.AlignCenter)
        self.ProductIncrease2 = QPushButton(self.ProductFrame2)
        self.ProductIncrease2.setObjectName(u"ProductIncrease2")
        self.ProductIncrease2.setGeometry(QRect(110, 250, 21, 24))
        self.ProductIncrease2.setFont(font6)
        self.ProductIncrease2.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease2 = QPushButton(self.ProductFrame2)
        self.ProductDecrease2.setObjectName(u"ProductDecrease2")
        self.ProductDecrease2.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease2.setFont(font6)
        self.ProductDecrease2.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductFrame3 = QFrame(UserForm)
        self.ProductFrame3.setObjectName(u"ProductFrame3")
        self.ProductFrame3.setGeometry(QRect(410, 220, 151, 331))
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
"	\n"
"	image: url(:/real product/cabbage_PNG8803.png);\n"
"}")
        self.ProductLabel3 = QLabel(self.ProductFrame3)
        self.ProductLabel3.setObjectName(u"ProductLabel3")
        self.ProductLabel3.setGeometry(QRect(10, 110, 101, 16))
        self.ProductLabel3.setFont(font3)
        self.ProductDescription3 = QTextBrowser(self.ProductFrame3)
        self.ProductDescription3.setObjectName(u"ProductDescription3")
        self.ProductDescription3.setGeometry(QRect(10, 130, 131, 121))
        self.ProductDescription3.setFont(font4)
        self.BuyingButton3 = QPushButton(self.ProductFrame3)
        self.BuyingButton3.setObjectName(u"BuyingButton3")
        self.BuyingButton3.setGeometry(QRect(20, 290, 111, 31))
        self.BuyingButton3.setFont(font5)
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
        self.ProductAmount3.setFont(font3)
        self.ProductAmount3.setAlignment(Qt.AlignCenter)
        self.ProductIncrease3 = QPushButton(self.ProductFrame3)
        self.ProductIncrease3.setObjectName(u"ProductIncrease3")
        self.ProductIncrease3.setGeometry(QRect(110, 250, 21, 24))
        self.ProductIncrease3.setFont(font6)
        self.ProductIncrease3.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")
        self.ProductDecrease3 = QPushButton(self.ProductFrame3)
        self.ProductDecrease3.setObjectName(u"ProductDecrease3")
        self.ProductDecrease3.setGeometry(QRect(20, 250, 21, 24))
        self.ProductDecrease3.setFont(font6)
        self.ProductDecrease3.setStyleSheet(u"QPushButton {\n"
"	background: lightgray;\n"
"}")

        self.retranslateUi(UserForm)

        QMetaObject.connectSlotsByName(UserForm)
    # setupUi

    def retranslateUi(self, UserForm):
        UserForm.setWindowTitle(QCoreApplication.translate("UserForm", u"Form", None))
#if QT_CONFIG(whatsthis)
        self.KeywordInput.setWhatsThis(QCoreApplication.translate("UserForm", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.KeywordInput.setText(QCoreApplication.translate("UserForm", u"  Type keywords", None))
        self.KeywordInput.setPlaceholderText("")
        self.Search.setText(QCoreApplication.translate("UserForm", u"...", None))
        self.CoverLabel.setText(QCoreApplication.translate("UserForm", u"Agricultural products", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("UserForm", u"100+ Fresh Item for you", None))
        self.BrandLabel.setText(QCoreApplication.translate("UserForm", u"Fresh", None))
        self.ProductPicture1.setText("")
        self.ProductLabel1.setText(QCoreApplication.translate("UserForm", u"Carrot", None))
        self.ProductDescription1.setHtml(QCoreApplication.translate("UserForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">      Carrot, carrot and carots. So many carrots.</span></p></body></html>", None))
        self.BuyingButton1.setText(QCoreApplication.translate("UserForm", u"10 Bath", None))
        self.ProductAmount1.setText(QCoreApplication.translate("UserForm", u"Buy: 1", None))
        self.ProductIncrease1.setText(QCoreApplication.translate("UserForm", u"+", None))
        self.ProductDecrease1.setText(QCoreApplication.translate("UserForm", u"-", None))
        self.LoadMoreButton.setText(QCoreApplication.translate("UserForm", u"Load More !!!", None))
        self.ProductPicture2.setText("")
        self.ProductLabel2.setText(QCoreApplication.translate("UserForm", u"Wheat", None))
        self.ProductDescription2.setHtml(QCoreApplication.translate("UserForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">      cereal from wheat. &gt;=&lt;</span></p></body></html>", None))
        self.BuyingButton2.setText(QCoreApplication.translate("UserForm", u"5 Bath", None))
        self.ProductAmount2.setText(QCoreApplication.translate("UserForm", u"Buy: 1", None))
        self.ProductIncrease2.setText(QCoreApplication.translate("UserForm", u"+", None))
        self.ProductDecrease2.setText(QCoreApplication.translate("UserForm", u"-", None))
        self.ProductPicture3.setText("")
        self.ProductLabel3.setText(QCoreApplication.translate("UserForm", u"Cabbage", None))
        self.ProductDescription3.setHtml(QCoreApplication.translate("UserForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Franklin Gothic Medium Cond'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">      Vegetable for health!!!</span></p></body></html>", None))
        self.BuyingButton3.setText(QCoreApplication.translate("UserForm", u"15 Bath", None))
        self.ProductAmount3.setText(QCoreApplication.translate("UserForm", u"Buy: 1", None))
        self.ProductIncrease3.setText(QCoreApplication.translate("UserForm", u"+", None))
        self.ProductDecrease3.setText(QCoreApplication.translate("UserForm", u"-", None))
    # retranslateUi

