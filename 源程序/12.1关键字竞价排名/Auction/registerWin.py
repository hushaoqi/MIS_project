from PyQt5 import QtCore, QtGui, QtWidgets
from useBidWin import useBidWin
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import  pymysql

#这是登记类
class Ui_RegisterWin(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(600, 350)
        mainwindow.setMinimumSize(QtCore.QSize(600, 350))
        mainwindow.setMaximumSize(QtCore.QSize(600, 350))

        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setGeometry(QtCore.QRect(40, 0, 500, 50))
        self.frame_top.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_top.setMaximumSize(QtCore.QSize(500, 50))
        self.frame_top.setStyleSheet("#frame_top{\n"
"        border-bottom:3px solid #a1a4ad;\n"
"}")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.keywords_title = QtWidgets.QLabel(self.frame_top)
        self.keywords_title.setGeometry(QtCore.QRect(0, 10, 300, 40))
        self.keywords_title.setMinimumSize(QtCore.QSize(300, 40))
        self.keywords_title.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.keywords_title.setFont(font)
        self.keywords_title.setStyleSheet(" #keywords_title{\n"
"        color:#000000;\n"
"}")
        self.keywords_title.setObjectName("keywords_title")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(170, 230, 100, 30))
        self.pushButton1.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton1.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("#pushButton1{\n"
"        border:1px solid #000;\n"
"        border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background:#a1a4ad;\n"
"        color:white;\n"
"}\n"
"")
        self.pushButton1.setObjectName("pushButton1")
        self.bid=useBidWin()
        #按钮点击事件
        self.pushButton1.clicked.connect(self.showbidwin)

        self.label4_2 = QtWidgets.QLabel(self.centralwidget)
        self.label4_2.setGeometry(QtCore.QRect(200, 90, 115, 30))
        self.label4_2.setMinimumSize(QtCore.QSize(115, 30))
        self.label4_2.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label4_2.setFont(font)
        self.label4_2.setObjectName("label4_2")
        self.list_combox = QtWidgets.QComboBox(self.centralwidget)
        self.list_combox.setGeometry(QtCore.QRect(280, 90, 150, 30))
        self.list_combox.setMinimumSize(QtCore.QSize(150, 30))
        self.list_combox.setMaximumSize(QtCore.QSize(150, 30))
#         self.list_combox.setStyleSheet("#list_combox{\n"
# "        border:2px solid #a1a4ad;\n"
# "        border-radius:5px;\n"
# "    \n"
# "}")
        self.list_combox.setObjectName("list_combox")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(310, 230, 100, 30))
        self.pushButton2.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton2.setMaximumSize(QtCore.QSize(100, 30))

        #按钮点击事件
        self.pushButton2.clicked.connect(self.clo)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("#pushButton2{\n"
"        border:1px solid #000;\n"
"        border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background:#a1a4ad;\n"
"        color:white;\n"
"}\n"
"")
        self.pushButton2.setObjectName("pushButton2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(200, 140, 115, 30))
        self.label3.setMinimumSize(QtCore.QSize(115, 30))
        self.label3.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setStyleSheet("QLabel{\n"
"        text-align:center;\n"
"}")
        self.label3.setObjectName("label3")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(280, 140, 150, 30))
        self.lineEdit2.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setStyleSheet("#lineEdit2{\n"
"        border:1px solid #a1a4ad;\n"
"}\n"
"QLineEdit{\n"
"        padding-left:10px;\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "关键字竞拍系统"))
        self.keywords_title.setText(_translate("mainwindow", "登录界面"))
        self.pushButton1.setText(_translate("mainwindow", "登录"))
        self.label4_2.setText(_translate("mainwindow", "公司："))
        self.list_combox.setItemText(0, _translate("mainwindow", "公司1"))
        self.list_combox.setItemText(1, _translate("mainwindow", "公司2"))
        self.list_combox.setItemText(2, _translate("mainwindow", "公司3"))
        self.list_combox.setItemText(3, _translate("mainwindow", "公司4"))
        self.list_combox.setItemText(4, _translate("mainwindow", "公司5"))
        self.list_combox.setItemText(5, _translate("mainwindow", "公司6"))
        self.list_combox.setItemText(6, _translate("mainwindow", "公司7"))
        self.list_combox.setItemText(7, _translate("mainwindow", "公司8"))
        self.list_combox.setItemText(8, _translate("mainwindow", "公司9"))
        self.list_combox.setItemText(9, _translate("mainwindow", "公司10"))
        self.list_combox.setItemText(10, _translate("mainwindow", "公司11"))
        self.list_combox.setItemText(11, _translate("mainwindow", "公司12"))
        self.pushButton2.setText(_translate("mainwindow", "返回"))
        self.label3.setText(_translate("mainwindow", "密码："))
        self.lineEdit2.setText(_translate("mainwindow", ""))

    def showbidwin(self):
        text1=self.list_combox.currentText()
        text2=self.lineEdit2.text()
        #print(text1)
        #print(text2)
        config = {
            'host': 'localhost',  # 数据库所在主机IP
            'port': 3306,  # MySQL默认端口
            'user': 'root',  # mysql默认用户名
            'password': '12345',
            'db': 'auctiondb',  # 数据库
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
        }
        db = pymysql.connect(**config)
        #print("数据库连接成功！")
        cursor = db.cursor()
        #print("数据库指针寻找成功！")

        cursor.execute("SELECT * from company")
        self.results = cursor.fetchall()
        #print(self.results)
        cursor.close()
        db.close()
        i = 0
        l = len(self.results)
        flag=False
        while (i < l):
            s1 = self.results[i]['company']
            s2 = self.results[i]['password']
            #print(s1)
            #print(s2)
            if (s1==text1 and s2==text2):
                flag=True
            i = i + 1
        if(flag):
            #修改flag
            db = pymysql.connect(**config)
            #print("数据库连接成功！")
            cursor = db.cursor()
            #print("数据库指针寻找成功！")
            sql = ("UPDATE company SET flag = 1 where company ='%s'") % text1
            cursor.execute(sql)
            db.commit()
            sql = ("UPDATE company SET flag = 0 where company <>'%s'") % text1
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()

            self.lineEdit2.setText("")

            self.bid.show()
            self.bid.showKeyWords()
            self.hide()
        else:
            #输入不和法操作
            if(self.lineEdit2.text()==""):
                self.message1=QMessageBox.information(self,"提示","请输入密码")
            else:
                self.lineEdit2.setText("")
                self.message2= QMessageBox.information(self, "提示", "密码错误，重新输入")

    def clo(self):
        #print("关闭窗体")
        self.hide()

    def closeEvent(self, event):
        self.list_combox.setCurrentIndex(0)