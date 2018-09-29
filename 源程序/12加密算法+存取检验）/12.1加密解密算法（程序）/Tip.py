# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tip.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tip(object):
    def setupUi(self, Tip):
        Tip.setObjectName("Tip")
        Tip.resize(497, 253)
        self.pushButton = QtWidgets.QPushButton(Tip)
        self.pushButton.setGeometry(QtCore.QRect(360, 200, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Tip)
        self.label.setGeometry(QtCore.QRect(170, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily(".")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Tip)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 431, 21))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Tip)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 461, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Tip)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 471, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Tip)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 461, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Tip)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 471, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Tip)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 471, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Tip)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 471, 16))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Tip)
        self.pushButton.clicked.connect(Tip.close)
        QtCore.QMetaObject.connectSlotsByName(Tip)

    def retranslateUi(self, Tip):
        _translate = QtCore.QCoreApplication.translate
        Tip.setWindowTitle(_translate("Tip", "原理"))
        self.pushButton.setText(_translate("Tip", "返回"))
        self.label.setText(_translate("Tip", "算法原理"))
        self.label_2.setText(_translate("Tip", "在计算机中，有一种字符的编码形式叫ASCLL码，不同的字符对应"))
        self.label_3.setText(_translate("Tip", "不同的数字码。这里的加密算法是把输入的明文先全部转化为对应的"))
        self.label_4.setText(_translate("Tip", "ASCLL码，然后根据向左或向右偏移（减或者加）上一个偏移量（数字）"))
        self.label_5.setText(_translate("Tip", "得到新的ASCLL码，然后转化为字符的形式，这样得到的就是密文了。"))
        self.label_6.setText(_translate("Tip", "解密算法则和这个是一样的过程。比如A的ASCLL码是，向右偏移5个偏"))
        self.label_7.setText(_translate("Tip", "移量就是41+5=46，对应密文的ASCLL码就是46，转化为字符就是F，这"))
        self.label_8.setText(_translate("Tip", "样F就是A加密后的密文。解密则是相反的过程。"))

