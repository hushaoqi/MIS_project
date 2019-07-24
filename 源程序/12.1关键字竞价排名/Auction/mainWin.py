
import pymysql
from PyQt5.QtSql import QSqlQuery

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from useRegisterWin import useRegisterWin
from useBidResultWin import  useBidResultWin

#这是主窗口类
class Ui_MainWindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(600, 350)
        mainwindow.setMinimumSize(QtCore.QSize(600, 350))
        mainwindow.setMaximumSize(QtCore.QSize(600, 350))
        mainwindow.setStyleSheet("")

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
        self.frame_search = QtWidgets.QFrame(self.centralwidget)
        self.frame_search.setGeometry(QtCore.QRect(40, 60, 500, 40))
        self.frame_search.setMinimumSize(QtCore.QSize(500, 40))
        self.frame_search.setMaximumSize(QtCore.QSize(500, 40))
        self.frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search.setObjectName("frame_search")
        self.search_key = QtWidgets.QLabel(self.frame_search)
        self.search_key.setGeometry(QtCore.QRect(60, 0, 200, 45))
        self.search_key.setMinimumSize(QtCore.QSize(200, 45))
        self.search_key.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.search_key.setFont(font)
        self.search_key.setStyleSheet("#search_key{\n"
                                      "        color:#000;\n"
                                      "        position:relative;\n"
                                      "        margin-left:5px;\n"
                                      "}")
        self.search_key.setObjectName("search_key")
        self.list_combox = QtWidgets.QComboBox(self.frame_search)
        self.list_combox.setGeometry(QtCore.QRect(200, 10, 200, 30))
        self.list_combox.setMinimumSize(QtCore.QSize(200, 30))
        self.list_combox.setMaximumSize(QtCore.QSize(200, 30))
        # self.list_combox.setStyleSheet("#list_combox{\n"
        #                                "        border:2px solid #a1a4ad;\n"
        #                                "        border-radius:5px;\n"
        #                                "    \n"
        #                                "}")
        self.list_combox.setObjectName("list_combox")
        self.list_combox.addItem("")
        self.list_combox.addItem("")
        self.list_combox.addItem("")

        #设置默认内容
        self.list_combox.setEditText("连衣裙")

        #对关键词下拉列表定义事件
        self.list_combox.activated[str].connect(self.showmessage)

        self.frame_senter = QtWidgets.QFrame(self.centralwidget)
        self.frame_senter.setGeometry(QtCore.QRect(60, 160, 460, 30))
        self.frame_senter.setMinimumSize(QtCore.QSize(460, 30))
        self.frame_senter.setMaximumSize(QtCore.QSize(460, 30))
        self.frame_senter.setStyleSheet("#frame_senter{\n"
                                        "        background:#a1a4ad;\n"
                                        "}")
        self.frame_senter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_senter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_senter.setObjectName("frame_senter")
        self.label2 = QtWidgets.QLabel(self.frame_senter)
        self.label2.setGeometry(QtCore.QRect(140, 0, 115, 30))
        self.label2.setMinimumSize(QtCore.QSize(115, 30))
        self.label2.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setStyleSheet("")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.frame_senter)
        self.label3.setGeometry(QtCore.QRect(270, 0, 115, 30))
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
        self.label4 = QtWidgets.QLabel(self.frame_senter)
        self.label4.setGeometry(QtCore.QRect(380, 0, 115, 30))
        self.label4.setMinimumSize(QtCore.QSize(115, 30))
        self.label4.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label1 = QtWidgets.QLabel(self.frame_senter)
        self.label1.setGeometry(QtCore.QRect(40, 0, 115, 30))
        self.label1.setMinimumSize(QtCore.QSize(115, 30))
        self.label1.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setStyleSheet("")
        self.label1.setObjectName("label1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 190, 460, 50))
        self.frame.setMinimumSize(QtCore.QSize(460, 50))
        self.frame.setMaximumSize(QtCore.QSize(460, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label6 = QtWidgets.QLabel(self.frame)
        self.label6.setGeometry(QtCore.QRect(180, 0, 30, 50))
        self.label6.setMinimumSize(QtCore.QSize(30, 50))
        self.label6.setMaximumSize(QtCore.QSize(30, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.pushButton1 = QtWidgets.QPushButton(self.frame)
        self.pushButton1.setGeometry(QtCore.QRect(250, 10, 80, 30))
        self.pushButton1.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton1.setMaximumSize(QtCore.QSize(80, 30))
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
        self.reg=useRegisterWin()
        self.pushButton1.clicked.connect(self.reg.show)
        self.pushButton2 = QtWidgets.QPushButton(self.frame)
        self.pushButton2.setGeometry(QtCore.QRect(360, 10, 80, 30))
        self.pushButton2.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton2.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("#pushButton2{\n"
                                       "        border:1px solid #000;\n"
                                       "        border-radius:3px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "        background:#a1a4ad;\n"
                                       "        color:white;\n"
                                       "}\n"
                                       "")
        self.pushButton2.setObjectName("pushButton2")
        self.rel=useBidResultWin()

        #对按钮添加事件
        self.pushButton2.clicked.connect(self.rel.show)

        self.lineEdit1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit1.setGeometry(QtCore.QRect(20, 10, 80, 30))
        self.lineEdit1.setMinimumSize(QtCore.QSize(80, 30))
        self.lineEdit1.setMaximumSize(QtCore.QSize(60, 30))

        #设置为只读模式
        self.lineEdit1.setReadOnly(True)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setStyleSheet("#lineEdit1{\n"
                                     "        border:0px;\n"
                                     "}\n"
                                     "QLineEdit{\n"
                                     "        padding-left:15px;\n"
                                     "}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit2.setGeometry(QtCore.QRect(150, 10, 30, 30))
        self.lineEdit2.setMinimumSize(QtCore.QSize(30, 30))
        self.lineEdit2.setMaximumSize(QtCore.QSize(30, 30))

        self.lineEdit2.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setStyleSheet("#lineEdit2{\n"
                                     "        border:0px;\n"
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
        self.keywords_title.setText(_translate("mainwindow", "关键字竞拍系统"))
        self.search_key.setText(_translate("mainwindow", "查询关键字"))
        self.list_combox.setItemText(0, _translate("mainwindow", "连衣裙"))
        self.list_combox.setItemText(1, _translate("mainwindow", "衬衫"))
        self.list_combox.setItemText(2, _translate("mainwindow", "羽绒服"))
        self.label2.setText(_translate("mainwindow", "起拍价格"))
        self.label3.setText(_translate("mainwindow", "操作"))
        self.label4.setText(_translate("mainwindow", "查询"))
        self.label1.setText(_translate("mainwindow", "关键词"))
        self.label6.setText(_translate("mainwindow", "元"))
        self.pushButton1.setText(_translate("mainwindow", "竞价"))
        self.pushButton2.setText(_translate("mainwindow", "竞拍结果"))
        self.lineEdit1.setText(_translate("mainwindow", "连衣裙"))
        self.lineEdit2.setText(_translate("mainwindow", "5"))

    def showmessage(self):
        #ss存储当前下拉框值
        ss = self.list_combox.currentText()
        #print(ss)
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
        cursor.execute("SELECT * from keyinfo ")
        #存储查询结果
        self.results = cursor.fetchall()
        #print(self.results)
        i=0
        l=len(self.results)
        while(i<l):
            s1=self.results[i]['keywords']
            s2=self.results[i]['intialPri']
            #print(s1)
            #print(s2)
            if(ss==s1):
                #print("find")
                sql = ("UPDATE keyinfo SET flag = 1 where keywords ='%s'") % ss
                cursor.execute(sql)
                db.commit()
                sql = ("UPDATE keyinfo SET flag = 0 where keywords <>'%s'") % ss
                cursor.execute(sql)
                db.commit()
                #设置显示内容
                self.lineEdit1.setText(s1)
                self.lineEdit2.setText(str(s2))
                #self.list_combox.setEditText(s1)
                #self.list_combox.setCurrentText(s1)
            i=i+1
        cursor.close()
        db.close()


    def closeEvent(self, event):
         #print("关闭了窗体")
         ss = "连衣裙"
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
         # print("数据库连接成功！")
         cursor = db.cursor()
         # print("数据库指针寻找成功！")
         cursor.execute("SELECT * from keyinfo ")
         # 存储查询结果
         self.results = cursor.fetchall()
         #print(self.results)
         i = 0
         l = len(self.results)
         while (i < l):
             s1 = self.results[i]['keywords']
             #s2 = self.results[i]['intialPri']
             if (ss == s1):
                 # //print("True")
                 # #print("find")
                 sql = ("UPDATE keyinfo SET flag = 1 where keywords ='%s'") % ss
                 cursor.execute(sql)
                 db.commit()
                 sql = ("UPDATE keyinfo SET flag = 0 where keywords <>'%s'") % ss
                 cursor.execute(sql)
                 db.commit()
             i = i + 1
         cursor.close()
         db.close()












