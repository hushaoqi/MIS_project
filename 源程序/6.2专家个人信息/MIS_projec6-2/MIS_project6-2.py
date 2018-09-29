# -*- coding: utf-8 -*-

from MainWindow import *
from helpDialog import  *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import pymysql
import time
from dataViewModel import *
from dataViewModel import Table

class CheckMessage(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(CheckMessage,self).__init__(parent)
        self.setupUi(self)   #设置Ui_MainWindow窗口逻辑功能
        self.sex = '男'
        self.isAcademicia = '否'
        self.isDocent = '否'
        self.degree = '其他'
        self.EngName = 'Null'
        self.birthdate = "Null"
        self.graduateYear = "2014"
        self.schoolTag = "NUll"
        self.major = "NUll"
    # 获取姓名
    def getname(self):
        self.name = self.lineEdit_name.text()
        print(self.name)
    # 获取英文名
    def getEngName(self):
        self.EngName = self.lineEdit_EngName.text()
        print(self.EngName)
    # 获取证件号码
    def getID(self):
        self.ID = self.lineEdit_ID.text()
        print(self.ID)
    # 获取出生年月
    def getbirth(self):
        self.birthdate = self.lineEdit_birthdata.text()
        print(int(self.birthdate[5:7]))
        #print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        t = (time.strftime("%Y-%m", time.localtime()))
        #print(int(t[0:4]))
        if((int(t[0:4])-int(self.birthdate[0:4]))<18 or int(self.birthdate[5:7])>12):
            reply = QMessageBox.information(self,'输入提示','请输入真实正确信息(应>18岁）请重新输入！',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            print(reply)
            self.lineEdit_birthdata.clear()
    # 毕业年份
    def getgraduateYear(self):
        self.graduateYear = self.lineEdit_GraduateYear.text()
    #获取国籍
    def getCountry(self,country):
        self.country =country
    #获取性别
    def selectSex(self,text):
        self.sex = text

    #获取民族
    def getNation(self,nation):
        self.nation = nation
    #获取证件类型
    def getIDtype(self,IDtype):
        self.IDtype = IDtype
    #是否院士
    def selectAS(self,text):
        self.isAcademicia = text

    #是否博导
    def selectDoc(self,text):
            self.isDocent = text

    #职称
    def getJobTitle(self,jobTitle):
        self.jobTitle = jobTitle
    #最高学历
    def getEducation(self,education):
        self.education = education
    #最高学位
    def selectDegree(self,text):
        self.degree = text
    #显示源码按钮点击槽函数,打开源码文件
    def showCode(self):
        code = QProcess.execute("explorer professionalCode.txt")
    #数据库显示函数
    def showDatabase(self):
        self.SQL_show = Table()
        self.SQL_show.show()
    #帮助页面显示函数
    def showHelpPage(self):
        self.h = HelpDialog()
        self.h.show()

    #检查数据并保存函数
    def checkAndSaveData(self):
        # 毕业学校
        self.schoolTag = self.textEdit_school.toPlainText()
        # 所学专业
        self.major = self.textEdit_major.toPlainText()

        print(self.name, self.EngName, self.country, self.sex, self.nation, self.IDtype, self.ID, self.birthdate,
              self.isAcademicia, self.isDocent, self.jobTitle, self.education, self.degree, self.schoolTag,
              self.graduateYear, self.major)

        config = {
          'host':'localhost',#数据库所在主机IP
          'port':3306,#MySQL默认端口
          'user':'root',#mysql默认用户名
          'password':'12345',
          'db':'com_information',#数据库
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
        db = pymysql.connect(**config)
        print("数据库连接成功！准备插入数据！")
        cursor = db.cursor()
        print("数据库指针寻找成功！")
        n = cursor.execute("INSERT INTO professors"
                           "(name,EngName,country,sex,nation,IDtype,ID,birthdate,isAcademicia,isDocent,jobTitle,education,degree,schoolTag,graduateYear,major)"
                           " VALUES ('%s', '%s', '%s', '%s' ,'%s' ,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                           %(self.name,self.EngName,self.country,self.sex,self.nation,self.IDtype,self.ID,self.birthdate,self.isAcademicia,self.isDocent,self.jobTitle,self.education,self.degree,self.schoolTag,self.graduateYear,self.major))
        print("修改了 %s 行数据"% n)
        db.commit()  # 提交到数据库执行
        print("数据库插入成功！")
        cursor.close()
        db.close()
        print("数据库关闭成功！")
    #退出显示函数
    def Exit(self):
        self.close()


class HelpDialog(QMainWindow,Ui_showHelpDialog):
    def __init__(self,parent = None):
        super(HelpDialog,self).__init__(parent)
        self.setupUi(self)
        #设置Ui_showHelpDialog窗口逻辑功能


if __name__=="__main__":
    app = QApplication(sys.argv)
    check = CheckMessage()
    check.show()
    sys.exit(app.exec_())


