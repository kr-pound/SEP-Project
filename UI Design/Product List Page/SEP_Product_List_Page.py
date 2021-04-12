# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SEP_Product_List_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class Ui_UserForm(object):
    def setupUi(self, UserForm):
        UserForm.setObjectName("UserForm")
        UserForm.resize(791, 638)
        UserForm.setStyleSheet("QWidget {\n"
"    background-image: url(:/bg/green-slate.jpg);\n"
"}")
        self.CoverFrame = QtWidgets.QFrame(UserForm)
        self.CoverFrame.setGeometry(QtCore.QRect(40, 20, 711, 161))
        self.CoverFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CoverFrame.setStyleSheet("QFrame {\n"
"    background: Black;\n"
"    border-radius: 40px;\n"
"}")
        self.CoverFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CoverFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CoverFrame.setObjectName("CoverFrame")
        self.KeywordInput = QtWidgets.QLineEdit(self.CoverFrame)
        self.KeywordInput.setGeometry(QtCore.QRect(210, 100, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.KeywordInput.setFont(font)
        self.KeywordInput.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.KeywordInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.KeywordInput.setStyleSheet("QLineEdit {\n"
"    background: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: #717072;\n"
"}")
        self.KeywordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.KeywordInput.setCursorPosition(15)
        self.KeywordInput.setDragEnabled(True)
        self.KeywordInput.setReadOnly(False)
        self.KeywordInput.setPlaceholderText("")
        self.KeywordInput.setClearButtonEnabled(False)
        self.KeywordInput.setObjectName("KeywordInput")
        self.Search = QtWidgets.QToolButton(self.CoverFrame)
        self.Search.setGeometry(QtCore.QRect(480, 100, 31, 31))
        self.Search.setStyleSheet("QToolButton {\n"
"    background: transparent;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/search/search--v2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search.setIcon(icon)
        self.Search.setObjectName("Search")
        self.CoverLabel = QtWidgets.QLabel(self.CoverFrame)
        self.CoverLabel.setGeometry(QtCore.QRect(210, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(22)
        self.CoverLabel.setFont(font)
        self.CoverLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CoverLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CoverLabel.setObjectName("CoverLabel")
        self.DescriptionLabel = QtWidgets.QLabel(self.CoverFrame)
        self.DescriptionLabel.setGeometry(QtCore.QRect(210, 60, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        self.DescriptionLabel.setFont(font)
        self.DescriptionLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.DescriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.BrandLabel = QtWidgets.QLabel(self.CoverFrame)
        self.BrandLabel.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        self.BrandLabel.setFont(font)
        self.BrandLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.BrandLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrandLabel.setObjectName("BrandLabel")
        self.ProductFrame1 = QtWidgets.QFrame(UserForm)
        self.ProductFrame1.setGeometry(QtCore.QRect(40, 220, 151, 331))
        self.ProductFrame1.setStyleSheet("QFrame {\n"
"    background: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame1.setObjectName("ProductFrame1")
        self.ProductPicture1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductPicture1.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture1.setStyleSheet("QLabel {\n"
"    image: url(:/real product/carrot_PNG4985.png);\n"
"}")
        self.ProductPicture1.setText("")
        self.ProductPicture1.setObjectName("ProductPicture1")
        self.ProductLabel1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductLabel1.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel1.setFont(font)
        self.ProductLabel1.setObjectName("ProductLabel1")
        self.ProductDescription1 = QtWidgets.QTextBrowser(self.ProductFrame1)
        self.ProductDescription1.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription1.setFont(font)
        self.ProductDescription1.setObjectName("ProductDescription1")
        self.BuyingButton1 = QtWidgets.QPushButton(self.ProductFrame1)
        self.BuyingButton1.setGeometry(QtCore.QRect(20, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton1.setFont(font)
        self.BuyingButton1.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #64AB25;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.BuyingButton1.setObjectName("BuyingButton1")
        self.ProductAmount1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductAmount1.setGeometry(QtCore.QRect(20, 260, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount1.setFont(font)
        self.ProductAmount1.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount1.setObjectName("ProductAmount1")
        self.ProductIncrease1 = QtWidgets.QPushButton(self.ProductFrame1)
        self.ProductIncrease1.setGeometry(QtCore.QRect(110, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease1.setFont(font)
        self.ProductIncrease1.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductIncrease1.setObjectName("ProductIncrease1")
        self.ProductDecrease1 = QtWidgets.QPushButton(self.ProductFrame1)
        self.ProductDecrease1.setGeometry(QtCore.QRect(20, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease1.setFont(font)
        self.ProductDecrease1.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductDecrease1.setObjectName("ProductDecrease1")
        self.LoadMoreButton = QtWidgets.QPushButton(UserForm)
        self.LoadMoreButton.setGeometry(QtCore.QRect(340, 580, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.LoadMoreButton.setFont(font)
        self.LoadMoreButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #64AB25;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}")
        self.LoadMoreButton.setObjectName("LoadMoreButton")
        self.ProductFrame2 = QtWidgets.QFrame(UserForm)
        self.ProductFrame2.setGeometry(QtCore.QRect(220, 220, 151, 331))
        self.ProductFrame2.setStyleSheet("QFrame {\n"
"    background: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame2.setObjectName("ProductFrame2")
        self.ProductPicture2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductPicture2.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture2.setStyleSheet("QLabel {\n"
"    \n"
"    image: url(:/real product/wheat_PNG85.png);\n"
"}")
        self.ProductPicture2.setText("")
        self.ProductPicture2.setObjectName("ProductPicture2")
        self.ProductLabel2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductLabel2.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel2.setFont(font)
        self.ProductLabel2.setObjectName("ProductLabel2")
        self.ProductDescription2 = QtWidgets.QTextBrowser(self.ProductFrame2)
        self.ProductDescription2.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription2.setFont(font)
        self.ProductDescription2.setObjectName("ProductDescription2")
        self.BuyingButton2 = QtWidgets.QPushButton(self.ProductFrame2)
        self.BuyingButton2.setGeometry(QtCore.QRect(20, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton2.setFont(font)
        self.BuyingButton2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #64AB25;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.BuyingButton2.setObjectName("BuyingButton2")
        self.ProductAmount2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductAmount2.setGeometry(QtCore.QRect(20, 260, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount2.setFont(font)
        self.ProductAmount2.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount2.setObjectName("ProductAmount2")
        self.ProductIncrease2 = QtWidgets.QPushButton(self.ProductFrame2)
        self.ProductIncrease2.setGeometry(QtCore.QRect(110, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease2.setFont(font)
        self.ProductIncrease2.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductIncrease2.setObjectName("ProductIncrease2")
        self.ProductDecrease2 = QtWidgets.QPushButton(self.ProductFrame2)
        self.ProductDecrease2.setGeometry(QtCore.QRect(20, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease2.setFont(font)
        self.ProductDecrease2.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductDecrease2.setObjectName("ProductDecrease2")
        self.ProductFrame3 = QtWidgets.QFrame(UserForm)
        self.ProductFrame3.setGeometry(QtCore.QRect(410, 220, 151, 331))
        self.ProductFrame3.setStyleSheet("QFrame {\n"
"    background: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame3.setObjectName("ProductFrame3")
        self.ProductPicture3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductPicture3.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture3.setStyleSheet("QLabel {\n"
"    \n"
"    image: url(https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png);\n"
"}")
        self.ProductPicture3.setText("")
        self.ProductPicture3.setObjectName("ProductPicture3")
        self.ProductLabel3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductLabel3.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel3.setFont(font)
        self.ProductLabel3.setObjectName("ProductLabel3")
        self.ProductDescription3 = QtWidgets.QTextBrowser(self.ProductFrame3)
        self.ProductDescription3.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription3.setFont(font)
        self.ProductDescription3.setObjectName("ProductDescription3")
        self.BuyingButton3 = QtWidgets.QPushButton(self.ProductFrame3)
        self.BuyingButton3.setGeometry(QtCore.QRect(20, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton3.setFont(font)
        self.BuyingButton3.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background: #64AB25;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #64AB25;\n"
"    background: #333;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.BuyingButton3.setObjectName("BuyingButton3")
        self.ProductAmount3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductAmount3.setGeometry(QtCore.QRect(20, 260, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount3.setFont(font)
        self.ProductAmount3.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount3.setObjectName("ProductAmount3")
        self.ProductIncrease3 = QtWidgets.QPushButton(self.ProductFrame3)
        self.ProductIncrease3.setGeometry(QtCore.QRect(110, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease3.setFont(font)
        self.ProductIncrease3.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductIncrease3.setObjectName("ProductIncrease3")
        self.ProductDecrease3 = QtWidgets.QPushButton(self.ProductFrame3)
        self.ProductDecrease3.setGeometry(QtCore.QRect(20, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease3.setFont(font)
        self.ProductDecrease3.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductDecrease3.setObjectName("ProductDecrease3")

        self.retranslateUi(UserForm)
        QtCore.QMetaObject.connectSlotsByName(UserForm)

    def retranslateUi(self, UserForm):
        _translate = QtCore.QCoreApplication.translate
        UserForm.setWindowTitle(_translate("UserForm", "Form"))
        self.KeywordInput.setWhatsThis(_translate("UserForm", "<html><head/><body><p><br/></p></body></html>"))
        self.KeywordInput.setText(_translate("UserForm", "  Type keywords"))
        self.Search.setText(_translate("UserForm", "..."))
        self.CoverLabel.setText(_translate("UserForm", "Agricultural products"))
        self.DescriptionLabel.setText(_translate("UserForm", "100+ Fresh Item for you"))
        self.BrandLabel.setText(_translate("UserForm", "Fresh"))
        self.ProductLabel1.setText(_translate("UserForm", "Carrot"))
        self.ProductDescription1.setHtml(_translate("UserForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\';\">      Carrot, carrot and carots. So many carrots.</span></p></body></html>"))
        self.BuyingButton1.setText(_translate("UserForm", "10 Bath"))
        self.ProductAmount1.setText(_translate("UserForm", "Buy: 1"))
        self.ProductIncrease1.setText(_translate("UserForm", "+"))
        self.ProductDecrease1.setText(_translate("UserForm", "-"))
        self.LoadMoreButton.setText(_translate("UserForm", "Load More !!!"))
        self.ProductLabel2.setText(_translate("UserForm", "Wheat"))
        self.ProductDescription2.setHtml(_translate("UserForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\';\">      cereal from wheat. &gt;=&lt;</span></p></body></html>"))
        self.BuyingButton2.setText(_translate("UserForm", "5 Bath"))
        self.ProductAmount2.setText(_translate("UserForm", "Buy: 1"))
        self.ProductIncrease2.setText(_translate("UserForm", "+"))
        self.ProductDecrease2.setText(_translate("UserForm", "-"))
        self.ProductLabel3.setText(_translate("UserForm", "Cabbage"))
        self.ProductDescription3.setHtml(_translate("UserForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\';\">      Vegetable for health!!!</span></p></body></html>"))
        self.BuyingButton3.setText(_translate("UserForm", "15 Bath"))
        self.ProductAmount3.setText(_translate("UserForm", "Buy: 1"))
        self.ProductIncrease3.setText(_translate("UserForm", "+"))
        self.ProductDecrease3.setText(_translate("UserForm", "-"))
import pic_rc


if __name__ == "__main__":
        suppress_qt_warnings()

        import sys
        app = QtWidgets.QApplication(sys.argv)
        UserForm = QtWidgets.QWidget()
        ui = Ui_UserForm()
        ui.setupUi(UserForm)
        UserForm.show()
        sys.exit(app.exec_())
