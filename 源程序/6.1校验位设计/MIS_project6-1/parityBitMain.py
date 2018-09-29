# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(300, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.inputWidget = QtWidgets.QWidget(self.centralwidget)
        self.inputWidget.setGeometry(QtCore.QRect(90, 100, 331, 311))
        self.inputWidget.setObjectName("inputWidget")
        self.commodityNameLabel = QtWidgets.QLabel(self.inputWidget)
        self.commodityNameLabel.setGeometry(QtCore.QRect(40, 80, 80, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commodityNameLabel.setFont(font)
        self.commodityNameLabel.setObjectName("commodityNameLabel")

        self.commodityCodeText = QtWidgets.QLineEdit(self.inputWidget)


        self.commodityCodeText.setGeometry(QtCore.QRect(180, 10, 134, 31))
        self.commodityCodeText.setObjectName("commodityCodeText")
        self.specificationLabel = QtWidgets.QLabel(self.inputWidget)
        self.specificationLabel.setGeometry(QtCore.QRect(40, 150, 80, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.specificationLabel.setFont(font)
        self.specificationLabel.setObjectName("specificationLabel")

        self.commodityNameText = QtWidgets.QLineEdit(self.inputWidget)


        self.commodityNameText.setGeometry(QtCore.QRect(180, 80, 134, 31))
        self.commodityNameText.setAutoFillBackground(False)
        self.commodityNameText.setObjectName("commodityNameText")

        self.specificationText = QtWidgets.QLineEdit(self.inputWidget)

        self.specificationText.setGeometry(QtCore.QRect(180, 150, 134, 31))
        self.specificationText.setObjectName("specificationText")

        self.chargeUnitText = QtWidgets.QLineEdit(self.inputWidget)


        self.chargeUnitText.setGeometry(QtCore.QRect(180, 220, 134, 31))
        self.chargeUnitText.setObjectName("chargeUnitText")
        self.chargeUnitLabel = QtWidgets.QLabel(self.inputWidget)
        self.chargeUnitLabel.setGeometry(QtCore.QRect(40, 220, 80, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chargeUnitLabel.setFont(font)
        self.chargeUnitLabel.setObjectName("chargeUnitLabel")
        self.commodityCodeLabel = QtWidgets.QLabel(self.inputWidget)
        self.commodityCodeLabel.setGeometry(QtCore.QRect(40, 10, 80, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.commodityCodeLabel.setFont(font)
        self.commodityCodeLabel.setObjectName("commodityCodeLabel")
        self.unitPriceLabel = QtWidgets.QLabel(self.inputWidget)
        self.unitPriceLabel.setGeometry(QtCore.QRect(40, 280, 80, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.unitPriceLabel.setFont(font)
        self.unitPriceLabel.setObjectName("unitPriceLabel")

        self.unitPriceText = QtWidgets.QLineEdit(self.inputWidget)


        self.unitPriceText.setGeometry(QtCore.QRect(180, 280, 134, 31))
        self.unitPriceText.setObjectName("unitPriceText")
        self.conceptWidget = QtWidgets.QWidget(self.centralwidget)
        self.conceptWidget.setGeometry(QtCore.QRect(460, 100, 281, 311))
        self.conceptWidget.setObjectName("conceptWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.conceptWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 261, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.showCodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.showCodeButton.setGeometry(QtCore.QRect(120, 420, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.showCodeButton.setFont(font)
        self.showCodeButton.setObjectName("showCodeButton")
        self.showDatebaseButton = QtWidgets.QPushButton(self.centralwidget)
        self.showDatebaseButton.setGeometry(QtCore.QRect(280, 420, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.showDatebaseButton.setFont(font)
        self.showDatebaseButton.setObjectName("showDatebaseButton")
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setGeometry(QtCore.QRect(440, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.helpButton.setFont(font)
        self.helpButton.setObjectName("helpButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(570, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(690, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #点击显示源代码按钮，跳出代码文件选择
        self.showCodeButton.clicked.connect(MainWindow.CodeShowClick)

        #点击显示数据库按钮，显示数据库
        self.showDatebaseButton.clicked.connect(MainWindow.showDatebase)

        #点击帮助按钮，显示帮助信息界面
        self.helpButton.clicked.connect(MainWindow.helpShow)

        #点击退出按钮，退出主界面
        self.exitButton.clicked.connect(MainWindow.Exec)


        # 点击保存按钮，获得商品编码并将数据保存到数据库com_information的information表中
        self.saveButton.clicked.connect(MainWindow.ProcessAndSave)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow-ParityBit"))
        self.titleLabel.setText(_translate("MainWindow", "代 码 校 验 位 检 验"))
        self.commodityNameLabel.setText(_translate("MainWindow", "商品名称"))
        self.specificationLabel.setText(_translate("MainWindow", " 规  格 "))
        self.chargeUnitLabel.setText(_translate("MainWindow", "计量单位"))
        self.commodityCodeLabel.setText(_translate("MainWindow", "商品编码"))
        self.unitPriceLabel.setText(_translate("MainWindow", " 单  价"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">校验位设计规则</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">商品编码本体码为：</span><span style=\" font-size:10pt; color:#000000;\">ABCDE</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">权因子：</span><span style=\" font-size:10pt; color:#000000;\">1</span><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">、</span><span style=\" font-size:10pt; color:#000000;\">2</span><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">、</span><span style=\" font-size:10pt; color:#000000;\">3</span><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">、</span><span style=\" font-size:10pt; color:#000000;\">4</span><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">、</span><span style=\" font-size:10pt; color:#000000;\">5</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">模：</span><span style=\" font-size:10pt; color:#000000;\">M=11</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-size:10pt; color:#000000;\">A   B   C   D   E</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">×</span><span style=\" font-size:10pt; color:#000000;\">   1   2   3   4   5</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-size:10pt; color:#000000;\">1A + 2B + 3C + 4D + 5E = Sum</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-size:10pt; color:#000000;\">Sum </span><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">÷</span><span style=\" font-size:10pt; color:#000000;\"> 11 = R</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">校验位为</span><span style=\" font-size:10pt; color:#000000;\">R</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%;\"><span style=\" font-family:\'宋体\'; font-size:10pt; color:#000000;\">则商品编码为：</span><span style=\" font-size:10pt; color:#000000;\">ABCDER</span> </p></body></html>"))
        self.showCodeButton.setText(_translate("MainWindow", "显示源代码"))
        self.showDatebaseButton.setText(_translate("MainWindow", "显示数据库"))
        self.helpButton.setText(_translate("MainWindow", "帮助"))
        self.saveButton.setText(_translate("MainWindow", "保存"))
        self.exitButton.setText(_translate("MainWindow", "退出"))
        # self.outputCodeButton.setText(_translate("MainWindow", "生成编码"))


