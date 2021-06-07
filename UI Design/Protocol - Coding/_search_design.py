# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 941, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 101, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 250, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.CoverFrame = QtWidgets.QFrame(self.centralwidget)
        self.CoverFrame.setGeometry(QtCore.QRect(150, 20, 711, 161))
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
        self.ProductFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame1.setGeometry(QtCore.QRect(90, 300, 151, 331))
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
"    image: url(:/)\n"
"}")
        self.ProductPicture1.setText("")
        self.ProductPicture1.setObjectName("ProductPicture1")
        self.ProductLabel1 = QtWidgets.QLabel(self.ProductFrame1)
        self.ProductLabel1.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel1.setFont(font)
        self.ProductLabel1.setText("")
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
        self.ProductFrame3 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame3.setGeometry(QtCore.QRect(430, 300, 151, 331))
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
"    image: url(:/)\n"
"}")
        self.ProductPicture3.setText("")
        self.ProductPicture3.setObjectName("ProductPicture3")
        self.ProductLabel3 = QtWidgets.QLabel(self.ProductFrame3)
        self.ProductLabel3.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel3.setFont(font)
        self.ProductLabel3.setText("")
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
        self.ProductFrame2 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame2.setGeometry(QtCore.QRect(260, 300, 151, 331))
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
"    image: url(:/)\n"
"}")
        self.ProductPicture2.setText("")
        self.ProductPicture2.setObjectName("ProductPicture2")
        self.ProductLabel2 = QtWidgets.QLabel(self.ProductFrame2)
        self.ProductLabel2.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel2.setFont(font)
        self.ProductLabel2.setText("")
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
        self.ProductFrame4 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame4.setGeometry(QtCore.QRect(600, 300, 151, 331))
        self.ProductFrame4.setStyleSheet("QFrame {\n"
"    background: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame4.setObjectName("ProductFrame4")
        self.ProductPicture4 = QtWidgets.QLabel(self.ProductFrame4)
        self.ProductPicture4.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture4.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture4.setText("")
        self.ProductPicture4.setObjectName("ProductPicture4")
        self.ProductLabel4 = QtWidgets.QLabel(self.ProductFrame4)
        self.ProductLabel4.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel4.setFont(font)
        self.ProductLabel4.setText("")
        self.ProductLabel4.setObjectName("ProductLabel4")
        self.ProductDescription4 = QtWidgets.QTextBrowser(self.ProductFrame4)
        self.ProductDescription4.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription4.setFont(font)
        self.ProductDescription4.setObjectName("ProductDescription4")
        self.BuyingButton4 = QtWidgets.QPushButton(self.ProductFrame4)
        self.BuyingButton4.setGeometry(QtCore.QRect(20, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton4.setFont(font)
        self.BuyingButton4.setStyleSheet("QPushButton {\n"
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
        self.BuyingButton4.setObjectName("BuyingButton4")
        self.ProductAmount4 = QtWidgets.QLabel(self.ProductFrame4)
        self.ProductAmount4.setGeometry(QtCore.QRect(20, 260, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount4.setFont(font)
        self.ProductAmount4.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount4.setObjectName("ProductAmount4")
        self.ProductIncrease4 = QtWidgets.QPushButton(self.ProductFrame4)
        self.ProductIncrease4.setGeometry(QtCore.QRect(110, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease4.setFont(font)
        self.ProductIncrease4.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductIncrease4.setObjectName("ProductIncrease4")
        self.ProductDecrease4 = QtWidgets.QPushButton(self.ProductFrame4)
        self.ProductDecrease4.setGeometry(QtCore.QRect(20, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease4.setFont(font)
        self.ProductDecrease4.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductDecrease4.setObjectName("ProductDecrease4")
        self.ProductFrame5 = QtWidgets.QFrame(self.centralwidget)
        self.ProductFrame5.setGeometry(QtCore.QRect(770, 300, 151, 331))
        self.ProductFrame5.setStyleSheet("QFrame {\n"
"    background: lightgray;\n"
"    border-radius: 30px;\n"
"}")
        self.ProductFrame5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProductFrame5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductFrame5.setObjectName("ProductFrame5")
        self.ProductPicture5 = QtWidgets.QLabel(self.ProductFrame5)
        self.ProductPicture5.setGeometry(QtCore.QRect(10, 10, 131, 91))
        self.ProductPicture5.setStyleSheet("QLabel {\n"
"    image: url(:/)\n"
"}")
        self.ProductPicture5.setText("")
        self.ProductPicture5.setObjectName("ProductPicture5")
        self.ProductLabel5 = QtWidgets.QLabel(self.ProductFrame5)
        self.ProductLabel5.setGeometry(QtCore.QRect(10, 110, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductLabel5.setFont(font)
        self.ProductLabel5.setText("")
        self.ProductLabel5.setObjectName("ProductLabel5")
        self.ProductDescription5 = QtWidgets.QTextBrowser(self.ProductFrame5)
        self.ProductDescription5.setGeometry(QtCore.QRect(10, 130, 131, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.ProductDescription5.setFont(font)
        self.ProductDescription5.setObjectName("ProductDescription5")
        self.BuyingButton5 = QtWidgets.QPushButton(self.ProductFrame5)
        self.BuyingButton5.setGeometry(QtCore.QRect(20, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.BuyingButton5.setFont(font)
        self.BuyingButton5.setStyleSheet("QPushButton {\n"
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
        self.BuyingButton5.setObjectName("BuyingButton5")
        self.ProductAmount5 = QtWidgets.QLabel(self.ProductFrame5)
        self.ProductAmount5.setGeometry(QtCore.QRect(20, 260, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.ProductAmount5.setFont(font)
        self.ProductAmount5.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductAmount5.setObjectName("ProductAmount5")
        self.ProductIncrease5 = QtWidgets.QPushButton(self.ProductFrame5)
        self.ProductIncrease5.setGeometry(QtCore.QRect(110, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductIncrease5.setFont(font)
        self.ProductIncrease5.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductIncrease5.setObjectName("ProductIncrease5")
        self.ProductDecrease5 = QtWidgets.QPushButton(self.ProductFrame5)
        self.ProductDecrease5.setGeometry(QtCore.QRect(20, 250, 21, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.ProductDecrease5.setFont(font)
        self.ProductDecrease5.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"}")
        self.ProductDecrease5.setObjectName("ProductDecrease5")
        self.CartButton = QtWidgets.QPushButton(self.centralwidget)
        self.CartButton.setGeometry(QtCore.QRect(880, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.CartButton.setFont(font)
        self.CartButton.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background: lightgray;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background: lightblue;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.CartButton.setObjectName("CartButton")
        self.RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightButton.setGeometry(QtCore.QRect(950, 420, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RightButton.setFont(font)
        self.RightButton.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"    border-radius: 20px;\n"
"    image: url(:/others/Arrow/rightArrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: lightgreen;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.RightButton.setText("")
        self.RightButton.setObjectName("RightButton")
        self.LeftButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftButton.setGeometry(QtCore.QRect(20, 420, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.LeftButton.setFont(font)
        self.LeftButton.setStyleSheet("QPushButton {\n"
"    background: lightgray;\n"
"    border-radius: 20px;\n"
"    image: url(:/others/Arrow/leftArrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: lightgreen;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.LeftButton.setText("")
        self.LeftButton.setObjectName("LeftButton")
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setGeometry(QtCore.QRect(880, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background: lightgray;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background: lightgreen;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.RefreshButton.setObjectName("RefreshButton")
        self.SellProductButton = QtWidgets.QPushButton(self.centralwidget)
        self.SellProductButton.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SellProductButton.setFont(font)
        self.SellProductButton.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background: lightgray;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background: lightblue;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.SellProductButton.setObjectName("SellProductButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to Fresh! We only have fresh stuff here. All the items are organic & natural."))
        self.label_4.setText(_translate("MainWindow", "Vegetables"))
        self.label_5.setText(_translate("MainWindow", "Fruits"))
        self.label_6.setText(_translate("MainWindow", "Daily products"))
        self.label_7.setText(_translate("MainWindow", "OTOP"))
        self.KeywordInput.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.KeywordInput.setText(_translate("MainWindow", "  Type keywords"))
        self.Search.setText(_translate("MainWindow", "..."))
        self.CoverLabel.setText(_translate("MainWindow", "Agricultural products"))
        self.DescriptionLabel.setText(_translate("MainWindow", "100+ Fresh Item for you"))
        self.BrandLabel.setText(_translate("MainWindow", "Fresh"))
        self.ProductDescription1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton1.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount1.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease1.setText(_translate("MainWindow", "+"))
        self.ProductDecrease1.setText(_translate("MainWindow", "-"))
        self.ProductDescription3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton3.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount3.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease3.setText(_translate("MainWindow", "+"))
        self.ProductDecrease3.setText(_translate("MainWindow", "-"))
        self.ProductDescription2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton2.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount2.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease2.setText(_translate("MainWindow", "+"))
        self.ProductDecrease2.setText(_translate("MainWindow", "-"))
        self.ProductDescription4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton4.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount4.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease4.setText(_translate("MainWindow", "+"))
        self.ProductDecrease4.setText(_translate("MainWindow", "-"))
        self.ProductDescription5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Franklin Gothic Medium Cond\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.BuyingButton5.setText(_translate("MainWindow", "0 Bath"))
        self.ProductAmount5.setText(_translate("MainWindow", "Buy: 1"))
        self.ProductIncrease5.setText(_translate("MainWindow", "+"))
        self.ProductDecrease5.setText(_translate("MainWindow", "-"))
        self.CartButton.setText(_translate("MainWindow", "View Cart"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.SellProductButton.setText(_translate("MainWindow", "Sell Product"))
import pic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
