# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicineList.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql as mc

class medicineList(QtWidgets.QWidget):
    
    def __init__(self,Dialog,patientID):
        super().__init__()
        
        self.patientID = patientID
        self.selectedMedicine = ''
        self.sqlResult = []
        
        sql =   "select 药品ID,药品名称 from 药品\
                where 药品ID in (select 药品ID from 开药单 where 患者ID = '%s')" % self.patientID
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management", charset='utf8')
        cursor = db.cursor()
        
        cursor.execute(sql)
        
        self.sqlResult.append(cursor.fetchall())
        
        
        
        self.initUI(Dialog)
    
    
    def on_click_listWidget(self):
        self.selectedMedicine = self.sqlResult[0][self.listWidget.currentRow()][0]     #------在查询结果里定位
    
    
    def initUI(self, Dialog):
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 520, 121, 71))
        self.pushButton.setObjectName("pushButton")
        
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(300, 40, 691, 551))
        self.listWidget.setObjectName("listWidget")
        
        for i in self.sqlResult[0]:
            self.listWidget.addItem(i[1])
        
        self.listWidget.itemClicked.connect(self.on_click_listWidget)
        
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 171, 281))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "查看详情"))
        self.label.setText(_translate("Form", "Icon Here"))

