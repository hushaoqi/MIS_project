# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette
import pymysql
from PyQt5.QtWidgets import QMainWindow, QApplication
import Dialog2

class Ui_Dialog1(object):
    def setupUi(self, Dialog1,name,self_ID):
        #定义主界面大小
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(800, 600)
        self.dialog=Dialog1
        self.name= name
        self.ID = self_ID

        #注销按钮
        self.Logout = QtWidgets.QPushButton(Dialog1)
        self.Logout.setGeometry(QtCore.QRect(610, 500, 93, 28))
        self.Logout.setObjectName("Logout")

        #定义一个放置4个信息访问按钮的垂直布局
        self.verticalLayoutWidget = QtWidgets.QWidget(self.dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 120, 101, 229))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #个人信息按钮
        self.Personal_Info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Personal_Info.setObjectName("Personal_Info")
        self.Personal_Info.setText("个人信息")
        self.verticalLayout.addWidget(self.Personal_Info)                       #将button放在一个垂直布局中

        #本月工资按钮
        self.CurMonth_Salary = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CurMonth_Salary.setObjectName("CurMonth_Salary")
        self.verticalLayout.addWidget(self.CurMonth_Salary)                     #将button放在一个垂直布局中
        self.CurMonth_Salary.setText("本月工资")

        #历史工资按钮
        self.All_Salary = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.All_Salary.setObjectName("All_Salary")
        self.verticalLayout.addWidget(self.All_Salary)                          #将button放在一个垂直布局中
        self.All_Salary.setText("历史工资")

        #信息修改按钮
        self.Change_Info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Change_Info.setObjectName("Change_Info")
        self.verticalLayout.addWidget(self.Change_Info)                         #将button放在一个垂直布局中
        self.Change_Info.setText("修改信息")

        #构成界面的水平布线和垂直布线
        self.line = QtWidgets.QFrame(self.dialog)
        self.line.setGeometry(QtCore.QRect(110, 470, 591, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.dialog)
        self.line_2.setGeometry(QtCore.QRect(110, 110, 591, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.dialog)
        self.line_3.setGeometry(QtCore.QRect(100, 120, 20, 361))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.dialog)
        self.line_4.setGeometry(QtCore.QRect(690, 120, 20, 361))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.dialog)
        self.line_5.setGeometry(QtCore.QRect(210, 120, 20, 361))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        #个人信息
        self.Name = QtWidgets.QLabel(self.dialog)               #姓名标签
        self.Name.setGeometry(QtCore.QRect(250, 150, 91, 41))
        self.Name.setObjectName("Name")
        self.NameDis = QtWidgets.QLabel(self.dialog)            #姓名显示
        self.NameDis.setGeometry(QtCore.QRect(300, 160, 291, 31))
        self.NameDis.setObjectName("NameDis")
        self.Name.setText("姓名：")
        self.Sex = QtWidgets.QLabel(self.dialog)                #性别标签
        self.Sex.setGeometry(QtCore.QRect(250, 210, 72, 15))
        self.Sex.setObjectName("Sex")
        self.Sex.setText("性别：")
        self.SexDis = QtWidgets.QLabel(self.dialog)             #性别显示
        self.SexDis.setGeometry(QtCore.QRect(300, 210, 291, 31))
        self.SexDis.setObjectName("SexDis")
        self.Age = QtWidgets.QLabel(self.dialog)                #年龄标签
        self.Age.setGeometry(QtCore.QRect(250, 260, 72, 15))
        self.Age.setObjectName("Age")
        self.Age.setText("年龄：")
        self.AgeDis = QtWidgets.QLabel(self.dialog)             #年龄显示
        self.AgeDis.setGeometry(QtCore.QRect(300, 260, 291, 31))
        self.AgeDis.setObjectName("AgeDis")
        self.Hobby = QtWidgets.QLabel(self.dialog)              #兴趣爱好标签
        self.Hobby.setGeometry(QtCore.QRect(250, 310, 72, 15))
        self.Hobby.setObjectName("Hobby")
        self.Hobby.setText("兴趣爱好：")
        self.HobbyDis = QtWidgets.QLabel(self.dialog)           #兴趣爱好显示
        self.HobbyDis.setGeometry(QtCore.QRect(300, 330, 331, 121))
        self.HobbyDis.setObjectName("HobbyDis")

        #本月工资
        self.Name_1 = QtWidgets.QLabel(self.dialog)             #姓名标签
        self.Name_1.setGeometry(QtCore.QRect(250, 150, 91, 41))
        self.Name_1.setObjectName("Name_1")
        self.Name_1.setText("姓名：")
        self.Name_2 = QtWidgets.QLabel(self.dialog)             #姓名显示
        self.Name_2.setGeometry(QtCore.QRect(320, 150, 291, 31))
        self.Name_2.setObjectName("Name_2")
        self.BasicSal = QtWidgets.QLabel(self.dialog)           #基本工资标签
        self.BasicSal.setGeometry(QtCore.QRect(250, 210, 72, 15))
        self.BasicSal.setObjectName("BasicSal")
        self.BasicSal.setText("基本工资：")
        self.BasicSal_2 = QtWidgets.QLabel(self.dialog)         #基本工资显示
        self.BasicSal_2.setGeometry(QtCore.QRect(320, 200, 291, 31))
        self.BasicSal_2.setObjectName("BasicSal_2")
        self.Reward = QtWidgets.QLabel(self.dialog)             #奖金标签
        self.Reward.setGeometry(QtCore.QRect(250, 260, 72, 15))
        self.Reward.setObjectName("Reward")
        self.Reward.setText("奖金：")
        self.Reward_2 = QtWidgets.QLabel(self.dialog)           #奖金显示
        self.Reward_2.setGeometry(QtCore.QRect(320, 250, 291, 31))
        self.Reward_2.setObjectName("Reward_2")
        self.Penalty = QtWidgets.QLabel(self.dialog)            #罚款标签
        self.Penalty.setGeometry(QtCore.QRect(250, 310, 72, 15))
        self.Penalty.setObjectName("Penalty")
        self.Penalty.setText("罚款：")
        self.Penalty_2 = QtWidgets.QLabel(self.dialog)          #罚款显示
        self.Penalty_2.setGeometry(QtCore.QRect(320, 300, 291, 31))
        self.Penalty_2.setObjectName("Penalty_2")
        self.Salary = QtWidgets.QLabel(self.dialog)             #应发工资标签
        self.Salary.setGeometry(QtCore.QRect(250, 360, 72, 15))
        self.Salary.setObjectName("Salary")
        self.Salary.setText("应发工资：")
        self.Salary_2 = QtWidgets.QLabel(self.dialog)           #应发工资显示
        self.Salary_2.setGeometry(QtCore.QRect(320, 350, 291, 31))
        self.Salary_2.setObjectName("Salary_2")

        #历史工资（通过将历史工资信息显示在一个ListWidget中)
        #self.init()
        self.DateColumn = QtWidgets.QLabel(self.dialog)             #显示数据的列名（月份+实发工资）
        self.DateColumn.setGeometry(QtCore.QRect(280,150,380,20))
        self.DateColumn.setText("月份\t\t  实发工资")
        self.listWidget = QtWidgets.QListWidget(self.dialog)        #逐行显示工资的滚动部件
        self.listWidget.setGeometry(QtCore.QRect(270, 170, 380, 260))

        #修改信息
        self.NameEdit = QtWidgets.QTextEdit(self.dialog)            #姓名修改输入框
        self.NameEdit.setGeometry(QtCore.QRect(300, 160, 291, 31))
        self.NameEdit.setObjectName("NameEdit")
        self.SexEdit = QtWidgets.QTextEdit(self.dialog)             #性别修改输入框
        self.SexEdit.setGeometry(QtCore.QRect(300, 210, 291, 31))
        self.SexEdit.setObjectName("SexEdit")
        self.AgeEdit = QtWidgets.QTextEdit(self.dialog)             #年龄修改输入框
        self.AgeEdit.setGeometry(QtCore.QRect(300, 260, 291, 31))
        self.AgeEdit.setObjectName("AgeEdit")
        self.HobbyEdit = QtWidgets.QTextEdit(self.dialog)           #兴趣爱好修改输入框
        self.HobbyEdit.setGeometry(QtCore.QRect(300, 330, 331, 100))
        self.HobbyEdit.setObjectName("HobbyEdit")
        self.NameEditDis = ''
        self.AgeEditDis = ''
        self.SexEditDis = ''
        self.HobbyEditDis = ''

        #保存修改信息按钮
        self.Check = QtWidgets.QPushButton(self.dialog)
        self.Check.setGeometry(QtCore.QRect(420, 440, 93, 28))
        self.Check.setText("保存")
        self.Check.setObjectName("Check")

        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='12345',
            db='test',
            charset='utf8',
        )

        self.cur1 = self.conn.cursor()
        self.sqlstring = "select * from self_information where ID='" \
            + self.ID + "'"
        if (self.name==self.ID):#判断输入账号和查询到的账号是否相等，相等则读入数据库信息
            #按工号读取个人信息
            self.cur1.execute(self.sqlstring)
            self.rows = self.cur1.fetchall()
            self.cur1.close()

            #个人信息显示数据初始化
            self.NameDis.setText(self.rows[0][1])
            self.SexDis.setText(self.rows[0][2])
            self.AgeDis.setText(str(self.rows[0][-2]))       
            self.HobbyDis.setText(self.rows[0][-1])

            #保存个人信息缓存
            self.NameEditDis = self.rows[0][1]
            self.SexEditDis = self.rows[0][2]
            self.AgeEditDis = str(self.rows[0][-2])
            self.HobbyEditDis = self.rows[0][-1]

            #按月份查找本月工资
            self.cur2 = self.conn.cursor()
            self.sqlstring2 = "select * from salary_month where Month=201807 and ID='" \
                + self.ID + "'"
            self.cur2.execute(self.sqlstring2)
            self.rows2 = self.cur2.fetchall()
            self.cur2.close()

            #本月工资显示数据初始化
            self.Name_2.setText(self.rows2[0][2])
            self.BasicSal_2.setText(str(self.rows2[0][3]))
            self.Reward_2.setText(str(self.rows2[0][4]))
            self.Penalty_2.setText(str(self.rows2[0][5]))
            self.Salary_2.setText(str(self.rows2[0][6]))

            #按工号读取工资表
            self.cur3 = self.conn.cursor()
            self.sqlstring3 = "select * from salary_month where ID='" \
                + self.ID + "'"
            self.cur3.execute(self.sqlstring3)
            self.rows3 = self.cur3.fetchall()
            self.cur3.close()
            #将读取到的历史工资按月份逐条注入
            for self.row in self.rows3:
                self.listWidget.addItem(str(self.row[1]) \
                    + '\t\t' + str(self.row[6]))

        #设置调色板颜色为白色
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.white)

        #个人信息界面初始化(将调色板颜色填充在部件中)
        self.NameDis.setAutoFillBackground(True)
        self.AgeDis.setAutoFillBackground(True)
        self.SexDis.setAutoFillBackground(True)
        self.HobbyDis.setAutoFillBackground(True)
        self.NameDis.setPalette(pe)
        self.AgeDis.setPalette(pe)
        self.SexDis.setPalette(pe)
        self.HobbyDis.setPalette(pe)

        #本月工资界面初始化(将调色板颜色填充在部件中 + 隐藏界面部件)
        self.Name_2.setAutoFillBackground(True)
        self.BasicSal_2.setAutoFillBackground(True)
        self.Penalty_2.setAutoFillBackground(True)
        self.Salary_2.setAutoFillBackground(True)
        self.Reward_2.setAutoFillBackground(True)
        self.Name_2.setPalette(pe)
        self.BasicSal_2.setPalette(pe)
        self.Penalty_2.setPalette(pe)
        self.Salary_2.setPalette(pe)
        self.Reward_2.setPalette(pe)
        self.Name_1.hide()
        self.Name_2.hide()
        self.BasicSal_2.hide()
        self.BasicSal.hide()
        self.Penalty.hide()
        self.Penalty_2.hide()
        self.Reward.hide()
        self.Reward_2.hide()
        self.Salary.hide()
        self.Salary_2.hide()

        #历史工资界面初始化(隐藏界面部件)
        self.listWidget.hide()
        self.DateColumn.hide()

        #信息修改界面初始化(隐藏界面部件)
        self.NameEdit.hide()
        self.AgeEdit.hide()
        self.SexEdit.hide()
        self.HobbyEdit.hide()
        self.Check.hide()

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        #button显示注销文本
        self.Logout.setText(_translate("Dialog1", "注销"))
        #设置注销登录点击事件
        self.Logout.clicked.connect(self.jump_to_main)
        #设置查看个人信息点击事件
        self.Personal_Info.clicked.connect(self.jump_to_personalInfo)
        #设置查看本月工资按钮点击事件
        self.CurMonth_Salary.clicked.connect(self.jump_to_curSalary)
        #设置查看历史工资按钮点击事件
        self.All_Salary.clicked.connect(self.jump_to_allSalary)
        #设置信息修改按钮点击事件
        self.Change_Info.clicked.connect(self.jump_to_changeInfo)
        #设置信息修改保存按钮点击事件
        self.Check.clicked.connect(self.save_changeInfo)
        #修改会话标题
        self.dialog.setWindowTitle("用户登录界面")

    def jump_to_main(self):
        self.dialog.close()

    def jump_to_personalInfo(self):
        #显示个人信息
        self.Age.show()
        self.AgeDis.show()
        self.Name.show()
        self.NameDis.show()
        self.Sex.show()
        self.SexDis.show()
        self.Hobby.show()
        self.HobbyDis.show()

        #隐藏工资信息
        self.Name_1.hide()
        self.Name_2.hide()
        self.Reward.hide()
        self.Reward_2.hide()
        self.Penalty.hide()
        self.Penalty_2.hide()
        self.BasicSal.hide()
        self.BasicSal_2.hide()
        self.Salary.hide()
        self.Salary_2.hide()

        #隐藏信息修改
        self.NameEdit.hide()
        self.AgeEdit.hide()
        self.SexEdit.hide()
        self.HobbyEdit.hide()
        self.Check.hide()

        # 隐藏历史工资
        self.listWidget.hide()
        self.DateColumn.hide()

    def jump_to_curSalary(self):
        #显示工资信息
        self.Name_1.show()
        self.Name_2.show()
        self.Reward.show()
        self.Reward_2.show()
        self.Penalty.show()
        self.Penalty_2.show()
        self.BasicSal.show()
        self.BasicSal_2.show()
        self.Salary.show()
        self.Salary_2.show()

        #隐藏个人信息界面部件
        self.Age.hide()
        self.AgeDis.hide()
        self.Name.hide()
        self.NameDis.hide()
        self.Sex.hide()
        self.SexDis.hide()
        self.Hobby.hide()
        self.HobbyDis.hide()

        #隐藏信息修改界面部件
        self.NameEdit.hide()
        self.AgeEdit.hide()
        self.SexEdit.hide()
        self.HobbyEdit.hide()
        self.Check.hide()

        #隐藏历史工资界面部件
        self.listWidget.hide()
        self.DateColumn.hide()

    def jump_to_allSalary(self):
        #显示历史工资界面部件
        self.listWidget.show()
        self.DateColumn.show()

        # 隐藏个人信息界面部件
        self.Age.hide()
        self.AgeDis.hide()
        self.Name.hide()
        self.NameDis.hide()
        self.Sex.hide()
        self.SexDis.hide()
        self.Hobby.hide()
        self.HobbyDis.hide()

        # 隐藏工资信息界面部件
        self.Name_1.hide()
        self.Name_2.hide()
        self.Reward.hide()
        self.Reward_2.hide()
        self.Penalty.hide()
        self.Penalty_2.hide()
        self.BasicSal.hide()
        self.BasicSal_2.hide()
        self.Salary.hide()
        self.Salary_2.hide()

        #隐藏信息修改界面部件
        self.NameEdit.hide()
        self.AgeEdit.hide()
        self.SexEdit.hide()
        self.HobbyEdit.hide()
        self.Check.hide()

    def jump_to_changeInfo(self):
        #显示信息修改界面部件，并将个人信息缓存读入个人信息修改的部件中
        self.NameEdit.setText(self.NameEditDis)
        self.AgeEdit.setText(self.AgeEditDis)
        self.SexEdit.setText(self.SexEditDis)
        self.HobbyEdit.setText(self.HobbyEditDis)
        self.NameEdit.show()
        self.Name.show()
        self.AgeEdit.show()
        self.Age.show()
        self.SexEdit.show()
        self.Sex.show()
        self.HobbyEdit.show()
        self.Hobby.show()
        self.Check.show()

        #隐藏个人信息界面部件
        self.AgeDis.hide()
        self.NameDis.hide()
        self.SexDis.hide()
        self.HobbyDis.hide()

        #隐藏工资信息界面部件
        self.Name_1.hide()
        self.Name_2.hide()
        self.Reward.hide()
        self.Reward_2.hide()
        self.Penalty.hide()
        self.Penalty_2.hide()
        self.BasicSal.hide()
        self.BasicSal_2.hide()
        self.Salary.hide()
        self.Salary_2.hide()

        #隐藏历史工资界面部件
        self.listWidget.hide()
        self.DateColumn.hide()

    #保存修改
    def save_changeInfo(self):
        if(self.name == self.ID):
            #禁止名字、性别、年龄为空，若发生以上现象弹出保存失败会话
            if(self.NameEdit.toPlainText() == '' or self.SexEdit.toPlainText() == '' or self.AgeEdit.toPlainText() == ''):
                form1 = QtWidgets.QDialog()
                ui = Dialog2.Ui_Dialog2()
                ui.setupUi(form1, False)
                form1.exec_()
            else:
                #进行数据库信息修改
                self.cur4 = self.conn.cursor()
                self.cur5 = self.conn.cursor()
                #将修改更新到数据库中
                self.sqlstring4 = "update self_information set Name='"+ \
                    self.NameEdit.toPlainText()+"',Sex = '"+self.SexEdit.toPlainText()+"',Age='"+self.AgeEdit.toPlainText()+"',Hobbies= '"+\
                    self.HobbyEdit.toPlainText()+"'where ID='"+self.ID+"'"
                self.sqlstring5="update salary_month set Name='"+self.NameEdit.toPlainText()+"'where ID='"+self.ID+"'"
                try:
                    #修改数据库数据
                    self.cur4.execute(self.sqlstring4)
                    self.conn.commit()
                    self.cur4.close()
                    self.cur5.execute(self.sqlstring5)
                    self.conn.commit()
                    self.cur5.close()

                    # 修改界面显示数据
                    self.NameDis.setText(self.NameEdit.toPlainText())
                    self.SexDis.setText(self.SexEdit.toPlainText())
                    self.AgeDis.setText(self.AgeEdit.toPlainText())
                    self.HobbyDis.setText(self.HobbyEdit.toPlainText())
                    self.Name_2.setText(self.NameEdit.toPlainText())

                    #更新个人信息的缓存
                    self.NameEditDis = self.NameEdit.toPlainText()
                    self.AgeEditDis = self.AgeEdit.toPlainText()
                    self.SexEditDis = self.SexEdit.toPlainText()
                    self.HobbyEditDis = self.HobbyEdit.toPlainText()

                    #弹出保存成功会话
                    form1 = QtWidgets.QDialog()
                    ui = Dialog2.Ui_Dialog2()
                    ui.setupUi(form1, True)
                    form1.exec_()
                except Exception:  # 捕获所有异常
                    # 如果发生异常，则回滚
                    print("发生异常")
                    #数据库操作回滚
                    self.conn.rollback()

                    #弹出保存失败会话
                    form1 = QtWidgets.QDialog()
                    ui = Dialog2.Ui_Dialog2()
                    ui.setupUi(form1, False)
                    form1.exec_()
        else:
            form1 = QtWidgets.QDialog()
            ui = Dialog2.Ui_Dialog2()
            ui.setupUi(form1, False)
            form1.exec_()
        




