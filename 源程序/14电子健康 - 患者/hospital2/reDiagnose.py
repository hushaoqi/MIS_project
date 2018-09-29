# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reDiagnose.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from chattingWin import chattingWin
import pymysql as mc
from PyQt5.QtWidgets import  *
class reDiagnose(object):
    
    def __init__(self,Dialog,patientID):
        super().__init__()
        
        self.patientID = patientID
        self.doctorID = ''
        self.sqlResult = []
        self.dialog=Dialog
        sql =   "select 病历ID,存档时间,主诉,医生ID from 病历\
                where 患者ID = '%s'" % self.patientID
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
        cursor = db.cursor()
        
        cursor.execute(sql)
        
        self.sqlResult.append(cursor.fetchall())
        
        self.initUI(Dialog)
    
    
    def on_click_startChatting(self):
        try:
            self.chattingWin = chattingWin(self.doctorID,self.patientID)
            self.chattingWin.show()
        except:
            QMessageBox.warning(self.dialog, "警告", "医生端不在线", QMessageBox.Cancel)
        
    def on_click_listItems(self):
        
        self.doctorID = self.sqlResult[0][self.listWidget.currentRow()][3]
    
    
    
    def initUI(self, Dialog):
        Dialog.setObjectName("Form")
        
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 181, 601))
        self.groupBox.setObjectName("groupBox")
        
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click_startChatting)
        
        
        #self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton_2.setGeometry(QtCore.QRect(30, 530, 93, 28))
        #self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 141, 251))
        self.label.setObjectName("label")
        
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(230, 20, 711, 591))
        self.listWidget.setObjectName("listWidget")
        #print(self.sqlResult[0][0][2])
        for i in self.sqlResult[0]:
            self.listWidget.addItem(i[2])
        self.listWidget.itemClicked.connect(self.on_click_listItems)
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "历史病例"))
        self.pushButton.setText(_translate("Form", "开始复诊"))
        #self.pushButton_2.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "Icon"))

