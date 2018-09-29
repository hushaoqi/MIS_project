# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class HHP_scrollarea_widget(QtWidgets.QWidget):

    def __init__(self,parent = None,x = 0,y = 0,text_Browser = "",
                 mainwindows = None,conn_fun = None,departmentID = ""):
        super(HHP_scrollarea_widget,self).__init__(parent)

        self.setGeometry(QtCore.QRect(0, 0, 909, 150))
        self.move(x, y)
        self.departmentID = departmentID


        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("source/我的.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(115, 60, 641, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(text_Browser)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(770, 60, 90, 51))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName(str(departmentID))
        self.pushButton.setText("选择")

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 160, 851, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # self.pushButton.clicked.connect(lambda: conn_fun(department_id = departmentID))

    def wid_remove(self,x,y):
        self.move(x,y)

    def setTextBrowser(self,text_Browser):
        self.textBrowser.setText(text_Browser)
