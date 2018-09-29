# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MIS_project6-1'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from parityBitMain import *
from helpDialog import  *
from PyQt5.QtSql import *
import pymysql
from dataViewModel import *
import mysql
from dataViewModel import Table
from SQLtableModel import SqlShow
class CheckCode(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(CheckCode,self).__init__(parent)
        self.setupUi(self)
        #设置Ui_MainWindow窗口逻辑功能

    #帮助页面显示函数
    def helpShow(self):
        self.h = HelpDialog()

        self.h.show()


    #退出显示函数
    def Exec(self):
        self.close()

    #显示源码按钮点击槽函数,打开源码文件
    def CodeShowClick(self):
        code = QProcess.execute("explorer jiaoyancode.txt")


    #商品编码处理函数
    def ProcessAndSave(self):
        print("生成编码")
        codestr = self.commodityCodeText.text()

        #权因子：1、2、3、4、5 模：M=11
        sum = 1*int(codestr[0])+2*int(codestr[1])+3*int(codestr[2])+4*int(codestr[3])+5*int(codestr[4])
        R = sum % 11
        #注：以11为模，余数为10时按0处理。
        if R == 10:
            R = 0
        output_Code = codestr+str(R)
        #测试
        print(sum,R,output_Code)

        commodity_Code = self.commodityCodeText.text()
        commodity_Name = self.commodityNameText.text()
        specification_ = self.specificationText.text()
        charge_Unit    = self.chargeUnitText.text()
        unit_Price     = self.unitPriceText.text()

        #测试
        print(commodity_Code,commodity_Name,specification_,charge_Unit,unit_Price,output_Code)
        #插入数据库信息
        #mysql.InsertInformation(commodity_Code,commodity_Name,specification_,charge_Unit,unit_Price,output_Code)
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
        print("数据库连接成功！")
        cursor = db.cursor()
        print("数据库指针寻找成功！")

        n = cursor.execute("INSERT INTO information(commodityCode, commodityName, specification, chargeUnit,unitPrice,outputCode) VALUES ('%s', '%s', '%s', '%s' ,'%s' ,'%s')"
                           %(commodity_Code,commodity_Name,specification_,charge_Unit,unit_Price,output_Code))
        print("修改了 %s 行数据" % n)
        db.commit()  # 提交到数据库执行
        print("数据库插入成功！")
        cursor.close()
        db.close()
        print("数据库关闭成功！")
        #将生成的编码显示在文本框中
        self.commodityCodeText.setText("校验码:%s"% output_Code)

    #  数据库显示函数
    def showDatebase(self):
        self.SQL_show = Table()
        self.SQL_show.show()


class HelpDialog(QMainWindow,Ui_showHelpDialog):
    def __init__(self,parent = None):
        super(HelpDialog,self).__init__(parent)
        self.setupUi(self)
        #设置Ui_showHelpDialog窗口逻辑功能


if __name__=="__main__":
    app = QApplication(sys.argv)
    checkcode = CheckCode()
    checkcode.show()

    sys.exit(app.exec_())


