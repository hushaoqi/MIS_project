# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '账户密码错误.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(264, 182)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 141))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setToolTip("")
        self.label.setStatusTip("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "账号密码错误！"))


class model_dialog_show_str(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self,str = "model_dialog",parent=None):
        super(model_dialog_show_str,self).__init__(parent)
        self.setupUi(self)

        self.label.setText(str)
