# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sell_product.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PageLabel = QLabel(self.centralwidget)
        self.PageLabel.setObjectName(u"PageLabel")
        self.PageLabel.setGeometry(QRect(30, 10, 581, 61))
        font = QFont()
        font.setPointSize(28)
        self.PageLabel.setFont(font)
        self.PageLabel.setStyleSheet(u"color: white;\n"
"background-color : \"rgb(0, 0, 0)\";\n"
"border-radius: 15px;\n"
"")
        self.ConfirmButton = QPushButton(self.centralwidget)
        self.ConfirmButton.setObjectName(u"ConfirmButton")
        self.ConfirmButton.setGeometry(QRect(280, 460, 75, 24))
        self.ConfirmButton.setStyleSheet(u"QPushButton {\n"
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
        self.InfoLabel = QLabel(self.centralwidget)
        self.InfoLabel.setObjectName(u"InfoLabel")
        self.InfoLabel.setGeometry(QRect(40, 80, 271, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.InfoLabel.setFont(font1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 120, 591, 311))
        self.frame.setStyleSheet(u"background-color: rgb(116, 183, 46);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.NameLabel = QLabel(self.frame)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setGeometry(QRect(20, 20, 111, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.NameLabel.setFont(font2)
        self.PriceLabel = QLabel(self.frame)
        self.PriceLabel.setObjectName(u"PriceLabel")
        self.PriceLabel.setGeometry(QRect(20, 70, 101, 31))
        self.PriceLabel.setFont(font2)
        self.DetailLabel = QLabel(self.frame)
        self.DetailLabel.setObjectName(u"DetailLabel")
        self.DetailLabel.setGeometry(QRect(20, 120, 141, 31))
        self.DetailLabel.setFont(font2)
        self.NameLineEdit = QLineEdit(self.frame)
        self.NameLineEdit.setObjectName(u"NameLineEdit")
        self.NameLineEdit.setGeometry(QRect(150, 20, 411, 31))
        self.NameLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.PriceLineEdit = QLineEdit(self.frame)
        self.PriceLineEdit.setObjectName(u"PriceLineEdit")
        self.PriceLineEdit.setGeometry(QRect(150, 70, 411, 31))
        self.PriceLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.DetailTextEdit = QTextEdit(self.frame)
        self.DetailTextEdit.setObjectName(u"DetailTextEdit")
        self.DetailTextEdit.setGeometry(QRect(150, 120, 411, 71))
        self.DetailTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.CategoryLabel = QLabel(self.frame)
        self.CategoryLabel.setObjectName(u"CategoryLabel")
        self.CategoryLabel.setGeometry(QRect(20, 210, 101, 31))
        self.CategoryLabel.setFont(font2)
        self.CategoryLineEdit = QLineEdit(self.frame)
        self.CategoryLineEdit.setObjectName(u"CategoryLineEdit")
        self.CategoryLineEdit.setGeometry(QRect(150, 210, 411, 31))
        self.CategoryLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.AmountLabel = QLabel(self.frame)
        self.AmountLabel.setObjectName(u"AmountLabel")
        self.AmountLabel.setGeometry(QRect(20, 260, 121, 31))
        self.AmountLabel.setFont(font2)
        self.AmountLineEdit = QLineEdit(self.frame)
        self.AmountLineEdit.setObjectName(u"AmountLineEdit")
        self.AmountLineEdit.setGeometry(QRect(150, 260, 411, 31))
        self.AmountLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 646, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PageLabel.setText(QCoreApplication.translate("MainWindow", u"Product Information (Temporary)", None))
        self.ConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.InfoLabel.setText(QCoreApplication.translate("MainWindow", u"Please fill in below to register a new account.", None))
        self.NameLabel.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.PriceLabel.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.DetailLabel.setText(QCoreApplication.translate("MainWindow", u"Detail", None))
        self.DetailTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.CategoryLabel.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.AmountLabel.setText(QCoreApplication.translate("MainWindow", u"Product Amount", None))
    # retranslateUi

