# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(833, 451)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 10, 200, 50))
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 110, 250, 100))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 250, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 250, 250, 100))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 250, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(550, 80, 250, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(550, 220, 250, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(300, 110, 90, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(410, 110, 90, 20))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(300, 150, 101, 20))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(410, 150, 90, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 180, 90, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 290, 90, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(410, 250, 90, 20))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(300, 250, 90, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(300, 290, 101, 20))
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 320, 90, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(550, 110, 250, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(550, 250, 250, 100))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 380, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.decrypt)
        self.pushButton.clicked.connect(Form.encrypt)
        self.pushButton_3.clicked.connect(Form.Tipshow)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "加密解密"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">加密算法界面</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">明文输入框</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">密文输入框</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">密文输出框</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">明文输出框</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "秘钥 偏移量K"))
        self.label_7.setText(_translate("Form", "秘钥 偏移方向"))
        self.comboBox.setItemText(0, _translate("Form", "向左偏移"))
        self.comboBox.setItemText(1, _translate("Form", "向右偏移"))
        self.pushButton.setText(_translate("Form", "加密"))
        self.comboBox_2.setItemText(0, _translate("Form", "向左偏移"))
        self.comboBox_2.setItemText(1, _translate("Form", "向右偏移"))
        self.label_8.setText(_translate("Form", "秘钥 偏移量K"))
        self.label_9.setText(_translate("Form", "秘钥 偏移方向"))
        self.pushButton_2.setText(_translate("Form", "解密"))
        self.pushButton_3.setText(_translate("Form", "算法原理"))

