# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchEssay.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gradingWin import gradingWin
import sys
import pymysql as mc



class searchEssayWin(QtWidgets.QWidget):
    
    def __init__(self,Dialog,doctor):
        
        super().__init__()
        
        self.doctor = doctor
        self.tags = "*"                                #要查找的关键字（从编辑框获取）
        self.widget = QtWidgets.QWidget()
        self.selectedEssayID = []
        self.searchResult = []
        
        self.initUI(Dialog)
    
    
    def on_click_search(self):
    #-----------------refresh   ListWidget------------------------
        self.tags = self.lineEdit.text()
        #-------------search in DataBase---------------------
        
    def on_click_grading(self):
        gradWin = gradingWin(self.doctor)
        gradWin.show()
    
    
    
    
    def initUI(self,Dialog):
        self.setObjectName("Form")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 431, 241))
        self.groupBox.setObjectName("groupBox")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 131, 201))
        self.label_3.setObjectName("label_3")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(160, 30, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(812, 157, 201, 41))
        self.pushButton_search.setObjectName("pushButton")
        self.pushButton_search.clicked.connect(self.on_click_search)
        
        self.pushButton_grading = QtWidgets.QPushButton(Dialog)
        self.pushButton_grading.setGeometry(QtCore.QRect(812, 227, 201, 41))
        self.pushButton_grading.setObjectName("pushButton_2")
        self.pushButton_grading.clicked.connect(self.on_click_grading)
        
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(600, 227, 201, 41))
        self.pushButton_back.setObjectName("pushButton_3")
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 320, 1011, 331))
        self.listWidget.setObjectName("listView")
        #------------------sql 语句--筛选出该医生所有的文章------------#
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management", charset='utf8')
        cursor = db.cursor()
        sql = "SELECT 文章ID,文章题目 FROM 科普文 \
                WHERE 医生ID = '%s'" % (self.doctor)
        cursor.execute(sql)
        self.searchResult.append(cursor.fetchall())
        self.listWidget.clear()
        for i in self.searchResult[0]:
            self.listWidget.addItem(i[1])
        
        
        
        
        
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(560, 100, 451, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("搜索")
        
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.label_3.setText(_translate("Form", "icon"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal     Resume</p></body></html>"))
        self.pushButton_search.setText(_translate("Form", "搜索"))
        self.pushButton_grading.setText(_translate("Form", "评分"))
        self.pushButton_back.setText(_translate("Form", "返回上个界面"))
        self.label.setText(_translate("Form", "搜索："))
        self.label_4.setText(_translate("Form", "搜索结果："))

    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = searchEssayWin("shan")
    window.show()
    sys.exit(app.exec_())
    














