# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:14:23 2018

@author: gmx
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'privatePharmacy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from reDiagnose import reDiagnose


class reDiaMainWin(QtWidgets.QWidget):
    
    def __init__(self,Dialog,patientID):
        super().__init__()
        
        self.patientID = patientID
    
        self.initUI(Dialog)
    
    

    
    def initUI(self,Dialog):
        self.setObjectName("Form")
        self.resize(1061, 769)
        
        
        self.widget_reDiagnose = QtWidgets.QWidget(Dialog)
        self.widget_reDiagnose.setGeometry(QtCore.QRect(10, 10, 1041, 751))
        self.widget_reDiagnose.setObjectName("widget_reDiagnose")
        self.win_reDiagnose = reDiagnose(self.widget_reDiagnose,self.patientID)
        #self.win_reDiagnose.pushButton.clicked.connect(self.on_click_reDiagnose)
        
        self.widget_reDiagnose.show()
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "私人药房"))





# app = QtWidgets.QApplication(sys.argv)
# private_phar = reDiaMainWin()
# private_phar.show()
# sys.exit(app.exec_())

