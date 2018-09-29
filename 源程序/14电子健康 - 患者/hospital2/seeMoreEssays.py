# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seeMoreEssays.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql as mc


class seeMoreEssays(QtWidgets.QWidget):
    
    def __init__(self,essayID,doctorID,Dialog):
        
        super().__init__()
        
        self.essay = ''
        self.searchResult = []
        
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
        cursor = db.cursor()
        sql = "SELECT 文章题目,文章内容 FROM 科普文 \
                WHERE (医生ID,文章ID) = ('%s','%s')" % (doctorID,essayID)
        cursor.execute(sql)
        
        self.searchResult.append(cursor.fetchall())
        self.title = self.searchResult[0][0][0]
        print(self.searchResult)
        self.initUI(Dialog)
    
    
    def initUI(self, Dialog):
        self.setObjectName("Form")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 431, 171))
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 91, 111))
        self.label.setObjectName("label")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(140, 10, 256, 151))
        self.textBrowser.setObjectName("textBrowser")
        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 90, 481, 91))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(31)
        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 200, 981, 501))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setText(self.searchResult[0][0][1])
        
        self.pushButton_backToSearchEssay = QtWidgets.QPushButton(Dialog)
        self.pushButton_backToSearchEssay.setGeometry(QtCore.QRect(812, 150, 201, 41))
        self.pushButton_backToSearchEssay.setObjectName("pushButton_backToSearchEssay")
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.pushButton_backToSearchEssay.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "Pictures "))
        print("note:               ",self.title)
        self.label_2.setText(self.title)

