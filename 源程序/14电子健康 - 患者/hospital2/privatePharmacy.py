# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'privatePharmacy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from medicineList import medicineList
from medicineDetails import medicineDetails
from PyQt5.QtWidgets import *
class privatePharmacy(QtWidgets.QWidget):
    
    def __init__(self,Dialog,patientID):
        super().__init__()
        
        self.patientID = patientID
        self.Dialog = []
        self.Dialog.append(Dialog)
    
        self.initUI(Dialog)
    
    
    def on_click_seeMedicineDetails(self):
        if self.win_medicineList.selectedMedicine != '':
            self.widget_medicineList.hide()

            self.widget_medicineDetails = QtWidgets.QWidget(self.Dialog[0])
            self.widget_medicineDetails.setGeometry(QtCore.QRect(10, 10, 1041, 751))
            self.widget_medicineDetails.setObjectName("widget")

            self.win_medicineDetails = medicineDetails(self.widget_medicineDetails,self.win_medicineList.selectedMedicine)
            self.win_medicineDetails.pushButton.clicked.connect(self.on_click_backToMedicineList)

            self.widget_medicineDetails.show()
        else:
            QMessageBox.warning(self, "警告", "请选择药品信息", QMessageBox.Cancel)
    
    def on_click_backToMedicineList(self):
        
        self.widget_medicineDetails.hide()
        
        self.widget_medicineList.show()
    
    def initUI(self,Dialog):
        self.setObjectName("Form")
        self.resize(1061, 769)
        
        
        self.widget_medicineList = QtWidgets.QWidget(Dialog)
        self.widget_medicineList.setGeometry(QtCore.QRect(10, 10, 1041, 751))
        self.widget_medicineList.setObjectName("widget_medicineList")
        self.win_medicineList = medicineList(self.widget_medicineList,self.patientID)
        self.win_medicineList.pushButton.clicked.connect(self.on_click_seeMedicineDetails)
        
        self.widget_medicineList.show()
        
        
        
        self.widget_medicineDetails = QtWidgets.QWidget(Dialog)
        self.widget_medicineDetails.setGeometry(QtCore.QRect(10, 10, 1041, 751))
        self.widget_medicineDetails.setObjectName("widget")
        
        self.widget_medicineDetails.hide()
        
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "私人药房"))





# app = QtWidgets.QApplication(sys.argv)
# private_phar = privatePharmacy()
# private_phar.show()
# sys.exit(app.exec_())


