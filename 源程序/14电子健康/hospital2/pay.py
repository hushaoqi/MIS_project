from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
class pay(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.setObjectName("pay_widget")
        self.page_title_label = QtWidgets.QLabel(self)
        self.page_title_label.setGeometry(QtCore.QRect(390, 110, 241, 61))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.page_title_label.setFont(font)
        self.page_title_label.setObjectName("page_title_label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(440, 520, 90, 30))
        self.pushButton.setObjectName("pushButton")


        self.erweima_label= QtWidgets.QLabel(self)
        self.erweima_label.setGeometry(QtCore.QRect(360, 200, 300, 300))

        self.erweima_label.setText("")
        self.erweima_label.setPixmap(QtGui.QPixmap("source/erweima.jpeg").scaled((self.erweima_label.rect().size())))
        self.erweima_label.setObjectName("erweima_label")


        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.page_title_label.setText(_translate("Form", "支付页面"))
        self.pushButton.setText(_translate("Form", "支付"))

