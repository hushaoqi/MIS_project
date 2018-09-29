# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NegoResult(object):
    def setupUi(self, NegoResult):
        NegoResult.setObjectName("NegoResult")
        NegoResult.resize(660, 500)
        self.Start_txt = QtWidgets.QTextEdit(NegoResult)
        self.Start_txt.setGeometry(QtCore.QRect(40, 40, 580, 180))
        self.Start_txt.setObjectName("Start_txt")
        self.Result_txt = QtWidgets.QTextEdit(NegoResult)
        self.Result_txt.setGeometry(QtCore.QRect(40, 270, 580, 180))
        self.Result_txt.setObjectName("Result_txt")
        self.Start = QtWidgets.QLabel(NegoResult)
        self.Start.setGeometry(QtCore.QRect(305, 10, 61, 16))
        self.Start.setObjectName("Start")
        self.Result = QtWidgets.QLabel(NegoResult)
        self.Result.setGeometry(QtCore.QRect(305, 240, 61, 16))
        self.Result.setObjectName("Result")
        self.InforSave = QtWidgets.QPushButton(NegoResult)
        self.InforSave.setGeometry(QtCore.QRect(160, 460, 75, 25))
        self.InforSave.setObjectName("InforSave")
        self.Quit = QtWidgets.QPushButton(NegoResult)
        self.Quit.setGeometry(QtCore.QRect(410, 460, 75, 25))
        self.Quit.setObjectName("Quit")

        self.retranslateUi(NegoResult)
        QtCore.QMetaObject.connectSlotsByName(NegoResult)

    def retranslateUi(self, NegoResult):
        _translate = QtCore.QCoreApplication.translate
        NegoResult.setWindowTitle(_translate("NegoResult", "Form"))
        self.Start.setText(_translate("NegoResult", "谈判过程"))
        self.Result.setText(_translate("NegoResult", "谈判结果"))
        self.InforSave.setText(_translate("NegoResult", "信息存储"))
        self.Quit.setText(_translate("NegoResult", "退出"))


# if __name__=="__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_NegoResult()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())