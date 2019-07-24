# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#要注意的是跳转界面第二个必须使用QDialog类，不能使用QWidget，我也不知道为什么，特别注意
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit
import Dialog,Dialog2
import sys
import pymysql
import traceback
from PyQt5.QtWidgets import *


class Ui_Form(object):  #这是用PyQt Designer生成的代码，很简单的，拖动控件，生成ui文件，然后UIC转换成py文件
    def setupUi(self, Form):
        #定义主界面大小
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.form = Form

        #系统名称标签
        self.SystemName = QtWidgets.QLabel(self.form)
        self.SystemName.setGeometry(QtCore.QRect(280, 110, 241, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SystemName.sizePolicy().hasHeightForWidth())
        self.SystemName.setSizePolicy(sizePolicy)
        self.SystemName.setTextFormat(QtCore.Qt.AutoText)
        self.SystemName.setAlignment(QtCore.Qt.AlignCenter)
        self.SystemName.setObjectName("SystemName")
        #账号标签
        self.Account = QtWidgets.QLabel(self.form)
        self.Account.setGeometry(QtCore.QRect(200, 234, 81, 21))
        self.Account.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Account.setObjectName("Account")
        #密码标签
        self.Passowrd = QtWidgets.QLabel(self.form)
        self.Passowrd.setGeometry(QtCore.QRect(210, 315, 71, 20))
        self.Passowrd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Passowrd.setObjectName("Passowrd")
        #账号输入控件
        self.AccountInput = QtWidgets.QTextEdit(self.form)
        self.AccountInput.setGeometry(QtCore.QRect(290, 230, 261, 41))
        self.AccountInput.setObjectName("AccountInput")
        #密码输入控件
        self.PasswordInput = QtWidgets.QLineEdit(self.form)
        self.PasswordInput.setGeometry(QtCore.QRect(290, 310, 261, 41))
        self.PasswordInput.setEchoMode(QLineEdit.Password)
        #登录点击按钮
        self.LoginButton = QtWidgets.QPushButton(self.form)
        self.LoginButton.setGeometry(QtCore.QRect(460, 390, 93, 28))
        self.LoginButton.setObjectName("LoginButton")
        #关闭窗口按钮
        self.ExitButton = QtWidgets.QPushButton(self.form)
        self.ExitButton.setGeometry(QtCore.QRect(300, 390, 93, 28))
        self.ExitButton.setObjectName("ExitButton")

 #       self.btn_exit = QtWidgets.QPushButton(Form)
 #       self.btn_exit.setGeometry(QtCore.QRect(310, 140, 75, 23))
 #       self.btn_exit.setObjectName("btn_exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        #界面窗口标题
        Form.setWindowTitle(_translate("Form", "企业管理系统"))
 #       self.btn_exit.setText(_translate("Form", "Exit"))
        #退出按钮名和设置退出按钮点击事件
        self.ExitButton.setText(_translate("Form", "退出"))
        self.ExitButton.clicked.connect(self.exit)
        #系统名称
        self.SystemName.setText(_translate("Form", "XX企业管理系统"))
        #账号标签名和密码标签名
        self.Account.setText(_translate("Form", "用户名："))
        self.Passowrd.setText(_translate("Form", "密码："))
#        pe = QPalette()
#        self.Passowrd.setAutoFillBackground(True)
#        pe.setColor(QPalette.Window, Qt.white)
#        self.Passowrd.setPalette(pe)
        #登录按钮名和设置登录按钮点击事件
        self.LoginButton.setText(_translate("Form", "登录"))
        self.LoginButton.clicked.connect(self.jump_to_login)
        #设置窗口图标
        self.form.setWindowIcon(QIcon('E:\\pycharmtest\\jinli.jpg'))

    def jump_to_login(self):
        #在这里进行数据库查询，认证用户名和密码的正确性
        self.conn = pymysql.connect(  # 建立一个连接，命名为conn
            host='localhost',  # 主机
            user='root',  # 本地用户
            passwd='12345',  # 密码
            db='test',  # 连接数据库名
            charset='utf8'
        )
        self.cur = self.conn.cursor()
        name = self.AccountInput.toPlainText()#获取输入的用户名
        passwd = self.PasswordInput.text()  #获取输入的密码
        self.sql = "select * from users where ID= '" + name + \
            "' and Password='" + passwd + "'"
        print("登录信息：",self.sql)
        try:
            res = self.cur.execute(self.sql)
            print("res:",res)

            self.rows = self.cur.fetchall()
            print("self.rows",self.rows)
            self.ID = self.rows[0][0]#（这里获取数据库中正确的用户名）
            #隐藏主界面并进入登录界面
            self.form.hide()
            form1 = QtWidgets.QDialog()
            ui = Dialog.Ui_Dialog1()
            #name为输入的账号，ID为数据库中查询到的账号
            ui.setupUi(form1, name, self.ID)
            #将输入的用户名和数据库中正确的用户名传入
            form1.show()
            form1.exec_()
            self.form.show()
        except Exception:  # 捕获所有异常
            # 如果发生异常，则回滚
            print("登录发生异常")
            traceback.print_exc()
            self.conn.rollback()
        self.cur.close()
        self.conn.close()


    def exit(self):
        self.form.close()


if __name__ == "__main__":
    #显示主界面
    app = QApplication(sys.argv)
    form = QtWidgets.QWidget()
    window = Ui_Form()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())