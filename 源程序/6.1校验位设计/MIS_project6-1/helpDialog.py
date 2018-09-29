# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showHelpDialog(object):
    def setupUi(self, showHelpDialog):
        showHelpDialog.setObjectName("showHelpDialog")
        showHelpDialog.resize(581, 469)
        self.textBrowser = QtWidgets.QTextBrowser(showHelpDialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 1, 581, 461))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(showHelpDialog)
        QtCore.QMetaObject.connectSlotsByName(showHelpDialog)

    def retranslateUi(self, showHelpDialog):
        _translate = QtCore.QCoreApplication.translate
        showHelpDialog.setWindowTitle(_translate("showHelpDialog", "helpDialog"))
        self.textBrowser.setHtml(_translate("showHelpDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">校验位设计标准，遵循</span><span style=\" font-size:12pt;\">ANSI/INCITS/ISO 7064-2003</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">《数据处理</span><span style=\" font-size:12pt;\">.</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">校验字符系统》算法标准。常用校验算法：</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">① 选权因子、模</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">② 求和：计算代码本体的每一位加权累加和</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">③ 求余数：以模除和求余数</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">④ 校验位：根据余数生成校验位码</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">         - </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">以余数为校验位码</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">         - </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">余数对应码表</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">⑤</span><span style=\" font-size:12pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">自检码</span><span style=\" font-size:12pt;\"> = </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">原代码本体</span><span style=\" font-size:12pt;\"> + </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">校验位码</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">(4) </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">保存</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">将当前输入界面的数据写入商品信息表。</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">(5) </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">退出</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">结束并退出。</span> </p></body></html>"))

