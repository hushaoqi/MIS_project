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
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">①</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">  </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">必填项不可为空。</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">②</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">  </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">以选代输的主要方式：</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">从下拉列表中选择，如民族、证件类型、最高学历</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">单选按钮选择，如性别、是否院士、是否博导、最高学位</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">从链接中选择，如国籍、职称</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">③</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">  </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">提高人机接口可交互性的策略</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">简单清晰，符合习惯，不花哨；</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">各要素保持统一的形式和风格；</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">提供上下敏感的帮助信息，如出生年月项的输入格式；</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">有出错处理和帮助功能，如姓名、职称项上的帮助；</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">  -</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">    </span><span style=\" font-family:\'宋体\'; font-size:12pt;\">关键操作有突出提示，如对必填项用红色星号突出提醒。</span> </p></body></html>"))

