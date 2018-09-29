from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
class expert_sys_widget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(False)
        self.setObjectName("expert_sys_widget")
        self.page_title_label = QtWidgets.QLabel(self)
        self.page_title_label.setGeometry(QtCore.QRect(370, 0, 261, 61))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.page_title_label.setFont(font)
        self.page_title_label.setAutoFillBackground(True)
        self.page_title_label.setObjectName("page_title_label")
        self.descrip_textBrowser = QtWidgets.QTextBrowser(self)
        self.descrip_textBrowser.setGeometry(QtCore.QRect(40, 100, 891, 341))
        self.descrip_textBrowser.setObjectName("descrip_textBrowser")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(440, 520, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.page_title_label.setText(_translate("Form", "专家系统病情分析"))
        self.descrip_textBrowser.setHtml(_translate("Form",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">专家系统详细描述</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "进入聊天"))
