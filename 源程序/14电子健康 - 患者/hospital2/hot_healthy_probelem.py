from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
class fifth_page_widget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        #self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("PMD_HHP")
        self.page_title_label = QtWidgets.QLabel(self)
        self.page_title_label.setGeometry(QtCore.QRect(370, 10, 201, 91))
        font = QtGui.QFont()
        font.setFamily("思源宋体 CN")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.page_title_label.setFont(font)
        self.page_title_label.setObjectName("page_title_label")
        self.no_answer_button = QtWidgets.QPushButton(self)
        self.no_answer_button.setGeometry(QtCore.QRect(740, 60, 221, 41))
        self.no_answer_button.setObjectName("no_answer_button")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(50, 120, 911, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 909, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.page_title_label.setText(_translate("Form", "热点健康问题"))
        self.no_answer_button.setText(_translate("Form", "没有解决我的问题"))
