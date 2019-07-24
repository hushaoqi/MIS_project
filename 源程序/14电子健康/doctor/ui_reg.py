# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reg.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Reg(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 10, 161, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 160, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 210, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 90, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(210, 130, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(210, 170, 54, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(210, 210, 54, 12))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 80, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 130, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 170, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(280, 210, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "医生注册系统"))
        self.label_2.setText(_translate("Form", "账号"))
        self.label_3.setText(_translate("Form", "密码"))
        self.label_4.setText(_translate("Form", "再次输入"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;user&quot;+&quot;两位数字&quot;</span></p></body></html>"))
        self.lineEdit_2.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;示例：user01&quot;</span></p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;两次密码要一致&quot;</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.label_5.setText(_translate("Form", "姓名"))
        self.label_6.setText(_translate("Form", "职称"))
        self.label_7.setText(_translate("Form", "科室ID"))
        self.label_8.setText(_translate("Form", "医院ID"))
        self.lineEdit_4.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;两个字母&quot;</span></p></body></html>"))
        self.lineEdit_5.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;主(副)治医生/实习生&quot;</span></p></body></html>"))
        self.lineEdit_6.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;2001/2002/2003&quot;</span></p></body></html>"))
        self.lineEdit_7.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;1001/1002/1003&quot;</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "返回"))

import sys
from PyQt5.QtWidgets import QApplication
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    doctor=Ui_Reg()
    doctor.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())