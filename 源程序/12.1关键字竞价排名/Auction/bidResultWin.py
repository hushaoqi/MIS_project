from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
#结果竞价界面
class Ui_BidResultWin(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(600, 350)
        mainwindow.setMinimumSize(QtCore.QSize(600, 350))
        mainwindow.setMaximumSize(QtCore.QSize(600, 350))
        mainwindow.setStyleSheet("QMainWindow #mainwindow{\n"
#"        background-color:#ffffff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setGeometry(QtCore.QRect(40, 0, 500, 50))
        self.frame_top.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_top.setMaximumSize(QtCore.QSize(500, 50))
        self.frame_top.setStyleSheet("#frame_top{\n"
#"        background:#fff;\n"
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
#         self.list_combox.setStyleSheet("#list_combox{\n"
# "        border:2px solid #a1a4ad;\n"
# "        border-radius:5px;\n"
# "    \n"
# "}")
#         self.list_combox.setObjectName("list_combox")

        #设置listcombox默认值
        self.list_combox.setEditText("公司1")
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

        self.list_combox.activated.connect(self.change)


        #下拉列表框点击事件
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(43, 150, 491, 131))
        self.textEdit.setStyleSheet("#textEdit{\n"
"        border:2px solid #a1a4ad;\n"
"        font:14px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
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
        self.keywords_title.setText(_translate("mainwindow", "竞拍结果"))
        self.search_key.setText(_translate("mainwindow", "查询公司"))
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

    def change(self):

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

        # 清空数据表
        cursor.execute("delete from fianlpri")
        db.commit()

        # 获取关键字
        cursor.execute("SELECT * from keyinfo where flag=1")
        self.results = cursor.fetchall()
        i = 0
        l = len(self.results)
        # print(l)
        i = 0
        while (i < l):
            keys_keywords = self.results[i]['keywords']
            keys_intialPri = self.results[i]['intialPri']
            i = i + 1
        # print(keys_keywords)

        sql = ("select * from auctiont where keywords = '%s'") % (keys_keywords)
        cursor.execute(sql)
        # cursor.execute("SELECT * from auctiont where ")
        self.results = cursor.fetchall()
        i = 0
        l = len(self.results)
        #print(l)

        while (i < l):
            com = self.results[i]['company']
            key = self.results[i]['keywords']
            pri = self.results[i]['weightPri']
            #
            # print(com)
            # print(key)
            # print(pri)
            #
            sql = ("insert into fianlpri values('%s','%s',%f)") % (
            com, key, float(pri))
            cursor.execute(sql)
            db.commit()
            i = i + 1
        cursor.close()
        db.close()
        #
        # 获取排序数据
        db = pymysql.connect(**config)
        # print("数据库连接成功！")
        cursor = db.cursor()
        # print("数据库指针寻找成功！")

        # 获取因子
        cursor.execute("SELECT * from company")
        self.result = cursor.fetchall()
        # len = len(self.result)
        # print(len)
        yinzinum = len(self.result)
        # print(yinzinum)

        # 获取关键字
        cursor.execute("SELECT * from fianlpri order by finalPri desc ")
        self.results = cursor.fetchall()
        l = len(self.results)
        #print(l)
        #print(self.results)

        i = 0
        num = -1
        current_gov = self.list_combox.currentText()

        self.list_combox.setEditText(current_gov)
        # 设置标志
        flag = False
        while (i < l):
            com = self.results[i]['company']
            key = self.results[i]['keywords']
            pri = self.results[i]['finalPri']
            if (current_gov == com):
                flag = True
                num = i
            # print(com)
            # print(key)
            # print(pri)
            i = i + 1

        # print(self.results)
        #print(num)
        #print(flag)
        cursor.close()
        db.close()


        #print(self.result)


        if (flag):
            #print("该公司参加了")
            # self.textEdit.setText("共有"+str(l)+"个公司参加竞价\n\n")
            # print(num)
            # print(self.results)
            # 默认为weight为0.8
            if ((num + 1) <= 10):
                # print(self.results)
                # print(l)
                weight = 0.8
                #print(num)
                #print(self.results)
                if(num<=l-2):
                    next=self.results[num+1]['company']
                    #print(next)
                    lenCompany=len(self.result)
                    temp= self.results[num+1]['company']
                    j = 0
                    #print(temp)
                    while(j<lenCompany):
                        if(temp==self.result[j]['company']):
                            weight = self.result[j]['weight']
                        j=j+1

                #print(weight)
                finallyprice = self.results[num]['finalPri'] / weight

                self.textEdit.setText("共有" + str(l)
                                      + "个公司参加竞价\n\n" + self.results[num][
                                          'company'] + "\n\n" +
                                      "您的排名为" + str(
                    num + 1) + "!\n\n" + "您需要支付的费用为" + "%.2f" % (finallyprice))
            else:
                self.textEdit.setText("共有" + str(l)
                                      + "个公司参加竞价\n\n" + current_gov + "竞价失败" + "\n\n" + "欢迎下次竞价")
        else:
            # print("该公司没有参加")
            self.textEdit.setText("共有" + str(
                l) + "个公司参加竞价\n\n" + current_gov + "没有参加" + key + "竞价" + "\n\n" + "请先完成竞价!")
        # cursor.close()
        # db.close()

    def closeEvent(self, event):
        self.textEdit.setText("")
        #print(self.list_combox.currentIndex())
        self.list_combox.setCurrentIndex(0)






