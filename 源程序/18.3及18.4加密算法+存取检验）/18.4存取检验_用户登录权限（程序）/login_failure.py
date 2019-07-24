# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_failure.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_failure(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 200)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(75, 10, 171, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 251, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 90, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 140, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 140, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录失败"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">登录失败界面</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "对不起，您的访问密码或权限错误！"))
        self.label_3.setText(_translate("Form", "请重新登录。"))
        self.pushButton.setText(_translate("Form", "重新登录"))
        self.pushButton_2.setText(_translate("Form", "取消"))

