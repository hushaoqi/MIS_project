# -*- coding: utf-8 -*- 

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
import sys
import pymysql

class Table(QWidget):

    def __init__(self):
        super(Table, self).__init__()
        self.setWindowTitle("数据库显示窗口")
        self.resize(1000,600)
        #创建SQL模型
        self.model = QStandardItemModel(20,16)
        self.model.setHorizontalHeaderLabels(['姓名', '英文名', '国籍', '性别','民族','证件类型','证件号码','出生年月','是否院士','是否博导','职称','最高学历','最高学位','毕业院校','毕业年份','所学专业'])


        config = {
            'host': 'localhost',  # 数据库所在主机IP
            'port': 3306,  # MySQL默认端口
            'user': 'root',  # mysql默认用户名
            'password': '12345',
            'db': 'com_information',  # 数据库
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
        }
        db = pymysql.connect(**config)
        print("数据库连接成功！")
        cursor = db.cursor()
        print("数据库指针寻找成功！")

        cursor.execute("SELECT  name,EngName,country,sex,nation,IDtype,ID,birthdate,isAcademicia,isDocent,jobTitle,education,degree,schoolTag,graduateYear,major from professors")

        self.results = cursor.fetchall()
        cursor.close()
        db.close()
        print(self.results)
        i = 0
        print(len(self.results))

        while(i < len(self.results)):
            self.model.setItem(i, 0,  QStandardItem(self.results[i]['name']))
            self.model.setItem(i, 1,  QStandardItem(self.results[i]['EngName']))
            self.model.setItem(i, 2,  QStandardItem(self.results[i]['country']))
            self.model.setItem(i, 3,  QStandardItem(self.results[i]['sex']))
            self.model.setItem(i, 4,  QStandardItem(self.results[i]['nation']))
            self.model.setItem(i, 5,  QStandardItem(self.results[i]['IDtype']))
            self.model.setItem(i, 6,  QStandardItem(self.results[i]['ID']))
            self.model.setItem(i, 7,  QStandardItem(self.results[i]['birthdate']))
            self.model.setItem(i, 8,  QStandardItem(self.results[i]['isAcademicia']))
            self.model.setItem(i, 9,  QStandardItem(self.results[i]['isDocent']))
            self.model.setItem(i, 10,  QStandardItem(self.results[i]['jobTitle']))
            self.model.setItem(i, 11,  QStandardItem(self.results[i]['education']))
            self.model.setItem(i, 12,  QStandardItem(self.results[i]['degree']))
            self.model.setItem(i, 13,  QStandardItem(self.results[i]['schoolTag']))
            self.model.setItem(i, 14,  QStandardItem(self.results[i]['graduateYear']))
            self.model.setItem(i, 15,  QStandardItem(self.results[i]['major']))
            i = i+1

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

