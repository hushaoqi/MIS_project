from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import pymysql
class second_page_widget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        self.setGeometry(QtCore.QRect(260, 20, 981, 681))
        self.setObjectName("second_page_widget")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(430, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #医院
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(150, 100, 150, 28))
        self.comboBox.setObjectName("comboBox")
        sql = 'select  distinct 医院名 from 医院'

        cursor.execute(sql)
        db.close()
        results_hosi=cursor.fetchall()
        #把医院一个个插进去
        for i in range(len(results_hosi)):
            self.comboBox.addItem(results_hosi[i][0])

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(430, 100, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #科室
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(570, 100, 69, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("内科")
        self.comboBox_2.addItem("外科")
        self.comboBox_2.addItem("儿科")
        # self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(140, 160, 411, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 20, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 20, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")



        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(60, 300, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(self)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 300, 69, 28))
        self.comboBox_3.setObjectName("comboBox_7")
        self.comboBox_3.addItem("一小时")
        self.comboBox_3.addItem("一个半小时")
        self.comboBox_3.addItem("两个小时")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(60, 370, 57, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 350, 411, 61))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 20, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 20, 103, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")

        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setGeometry(QtCore.QRect(50, 410, 891, 161))
        self.tableView.setObjectName("tableView")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self)
        self.dateTimeEdit.setGeometry(QtCore.QRect(150, 240, 194, 30))
        self.dateTimeEdit.setObjectName("dateTimeEdit")




        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(260, 600, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 600, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi()
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "挂号单"))
        self.label_2.setText(_translate("Form", "医院"))
        self.label_3.setText(_translate("Form", "科室"))
        self.label_4.setText(_translate("Form", "挂号类型"))
        self.radioButton.setText(_translate("Form", "为自己挂号"))
        self.radioButton_2.setText(_translate("Form", "为他人挂号"))
        self.label_5.setText(_translate("Form", "时间"))
        self.label_6.setText(_translate("Form", "时长"))
        #self.comboBox_3.setItemText(0, _translate("Form", "一小时"))
        self.label_7.setText(_translate("Form", "医生"))
        self.radioButton_3.setText(_translate("Form", "推荐医生"))
        self.radioButton_4.setText(_translate("Form", "自己选择"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "取消"))

