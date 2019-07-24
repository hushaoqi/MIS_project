# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicineDetails.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql as mc



class medicineDetails(QtWidgets.QWidget):
    
    def __init__(self,Dialog,selectedMedicine):
        super().__init__()
        
        self.selectedMedicine = selectedMedicine
        self.sqlResult = []
        
        print(self.selectedMedicine)
        
        sql =   "select 药品ID,药品名称,成分性状,适用病症,用法用量,不良反应,禁忌,注意事项,药物过量,药物毒理,价格,报销情况,有效期,贮存方式 from 药品\
                where 药品ID = '%s'" % self.selectedMedicine
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management",charset="utf8")
        cursor = db.cursor()
        
        cursor.execute(sql)
        
        self.sqlResult.append(cursor.fetchall())
        
        self.text1 = "成分性状：" + self.sqlResult[0][0][2] + '\n\n' +\
                "适用病症：" + self.sqlResult[0][0][3] + '\n\n' +\
                "用法用量：" + self.sqlResult[0][0][4] + '\n\n' +\
                "不良反应：" + self.sqlResult[0][0][5] + '\n\n' +\
                "禁忌：" + self.sqlResult[0][0][6] + '\n\n' +\
                "注意事项：" + self.sqlResult[0][0][7] + '\n\n' +\
                "药物过量：" + self.sqlResult[0][0][8] + '\n\n' +\
                "药物毒理：" + self.sqlResult[0][0][9] + '\n\n'
        
        self.text2 = "价格：" + str(self.sqlResult[0][0][10]) + '\n\n' +\
                "报销情况：" + str(self.sqlResult[0][0][11]) + '\n\n'
        
        self.text3 = "有效期：" + str(self.sqlResult[0][0][12]) + '\n\n' +\
                     "贮藏方式：" + self.sqlResult[0][0][13] + '\n\n'
        
        self.initUI(Dialog)
    
    
    def on_click_1(self):
        
        self.widget2.hide()
        self.widget3.hide()
        
        self.widget1.show()
        self.pushButton_3.setStyleSheet("background-color:white;color:black")
        self.pushButton_4.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_2.setStyleSheet("background-color:blue;color:white")
        
    def on_click_2(self):
        
        self.widget1.hide()
        self.widget3.hide()
        
        self.widget2.show()
        self.pushButton_2.setStyleSheet("background-color:white;color:black")
        self.pushButton_4.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_3.setStyleSheet("background-color:blue;color:white")
        
    def on_click_3(self):
        
        self.widget1.hide()
        self.widget2.hide()
        
        self.widget3.show()
        self.pushButton_2.setStyleSheet("background-color:white;color:black")
        self.pushButton_3.setStyleSheet("background-color:white;color:black")
        
        self.pushButton_4.setStyleSheet("background-color:blue;color:white")
        
    
    
    
    def initUI(self, Dialog):
        
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 261, 671))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 311))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(50, 580, 141, 51))
        self.pushButton.setObjectName("pushButton")
        
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(300, 30, 641, 491))
        self.widget1.setObjectName("widget")
        
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(300, 30, 641, 491))
        self.widget2.setObjectName("widget")
        
        self.widget3 = QtWidgets.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(300, 30, 641, 491))
        self.widget3.setObjectName("widget")
        
        self.textBrowser1 = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser1.setGeometry(QtCore.QRect(0, 160, 641, 431))
        self.textBrowser1.setObjectName("textBrowser")
        self.textBrowser1.setText(self.text1)
        
        self.textBrowser2 = QtWidgets.QTextBrowser(self.widget2)
        self.textBrowser2.setGeometry(QtCore.QRect(0, 160, 641, 431))
        self.textBrowser2.setObjectName("textBrowser")
        self.textBrowser2.setText(self.text2)
        
        self.textBrowser3 = QtWidgets.QTextBrowser(self.widget3)
        self.textBrowser3.setGeometry(QtCore.QRect(0, 160, 641, 431))
        self.textBrowser3.setObjectName("textBrowser")
        self.textBrowser3.setText(self.text3)
        
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 641, 161))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setGeometry(QtCore.QRect(300, 30, 641, 161))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_3")
        
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setGeometry(QtCore.QRect(300, 30, 641, 161))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(35)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_3")
        
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 545, 201, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_click_1)
        
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 545, 201, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_click_2)
        
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(740, 545, 201, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.on_click_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("Form", "药品详情"))
        self.label.setText(_translate("Form", "Icon"))
        self.label_2.setText(_translate("Form", "药品详情"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.label_3.setText(_translate("Form", "    " + self.sqlResult[0][0][1]))
        self.label_4.setText(_translate("Form", "    " + self.sqlResult[0][0][1]))
        self.label_5.setText(_translate("Form", "    " + self.sqlResult[0][0][1]))
        self.pushButton_2.setText(_translate("Form", "药理信息"))
        self.pushButton_3.setText(_translate("Form", "花费信息"))
        self.pushButton_4.setText(_translate("Form", "生产贮存"))

