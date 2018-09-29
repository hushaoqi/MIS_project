from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
class chosePMD_from_AP_widget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.setObjectName("chosePMD_from_AP_widget")
        self.ComRan_comboBox = QtWidgets.QComboBox(self)
        self.ComRan_comboBox.setGeometry(QtCore.QRect(20, 40, 201, 26))
        self.ComRan_comboBox.setObjectName("ComRan_comboBox")
        self.ComRan_comboBox.addItem("")
        self.area_comboBox = QtWidgets.QComboBox(self)
        self.area_comboBox.setGeometry(QtCore.QRect(260, 40, 201, 26))
        self.area_comboBox.setObjectName("area_comboBox")
        self.area_comboBox.addItem("")
        self.area_comboBox.addItem("")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 941, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.PMD_summary_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.PMD_summary_widget.setGeometry(QtCore.QRect(30, 30, 881, 91))
        self.PMD_summary_widget.setObjectName("PMD_summary_widget")
        self.head_label = QtWidgets.QLabel(self.PMD_summary_widget)
        self.head_label.setGeometry(QtCore.QRect(20, 30, 41, 41))
        self.head_label.setText("")
        self.head_label.setPixmap(QtGui.QPixmap("../source/医生.png"))
        self.head_label.setScaledContents(True)
        self.head_label.setObjectName("head_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.PMD_summary_widget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 10, 731, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.chose_pushButton = QtWidgets.QPushButton(self.PMD_summary_widget)
        self.chose_pushButton.setGeometry(QtCore.QRect(809, 30, 61, 30))
        self.chose_pushButton.setObjectName("chose_pushButton")
        self.line = QtWidgets.QFrame(self.PMD_summary_widget)
        self.line.setGeometry(QtCore.QRect(0, 80, 881, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.department_comboBox = QtWidgets.QComboBox(self)
        self.department_comboBox.setGeometry(QtCore.QRect(490, 40, 201, 26))
        self.department_comboBox.setObjectName("department_comboBox")
        self.department_comboBox.addItem("")

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ComRan_comboBox.setItemText(0, _translate("Form", "综合排序"))
        self.area_comboBox.setItemText(0, _translate("Form", "选择地区"))
        self.area_comboBox.setItemText(1, _translate("Form", "甘井子"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">医生摘要包括头像  医院  科室  好评率</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.chose_pushButton.setText(_translate("Form", "选择"))
        self.department_comboBox.setItemText(0, _translate("Form", "选择科室"))