# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
import sys


class Ui_Dialog2(object):
    #传入标签，表示保存成功或失败
    def setupUi(self, Dialog2, flag):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(250, 150)
        self.flag = flag
        self.dialog = Dialog2
        #pushButotn初始化
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(85, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        #显示label初始化
        self.label = QtWidgets.QLabel(self.dialog)
        self.label.setGeometry(QtCore.QRect(90,50,75,23))
        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "保存信息"))
        #设置点击事件返回上一层
        self.pushButton.setText(_translate("Dialog2", "确定"))
        self.pushButton.clicked.connect(self.go_back)
        #根据flag显示保存情况
        if self.flag:
            self.label.setText(_translate("Dialog2", "保存成功"))
        else:
            self.label.setText(_translate("Dialog2", "保存失败"))
        

    def go_back(self):
        self.dialog.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())