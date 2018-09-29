from PyQt5 import QtCore,QtWidgets

class Ui_Sure(QtWidgets.QDialog):
    def setupUi(self, Sure):
        Sure.setObjectName("Sure")
        Sure.resize(200, 100)
        self.Sure = QtWidgets.QPushButton(Sure)
        self.Sure.setGeometry(QtCore.QRect(62.5, 37.5, 75, 25))
        self.Sure.setObjectName("Sure")
        self.Sure.raise_()

        self.retranslateUi(Sure)
        QtCore.QMetaObject.connectSlotsByName(Sure)

    def retranslateUi(self, Sure):
        _translate = QtCore.QCoreApplication.translate
        Sure.setWindowTitle(_translate("Sure", "Diagol"))
        self.Sure.setText(_translate("Sure", "确定"))

# if __name__=="__main__":
#     import sys
#     app=QtWidgets.QApplication(sys.argv)
#     dialog=QtWidgets.QDialog()
#     ui=Ui_Sure()
#     ui.setupUi(dialog)
#     dialog.show()
#     sys.exit(app.exec_())