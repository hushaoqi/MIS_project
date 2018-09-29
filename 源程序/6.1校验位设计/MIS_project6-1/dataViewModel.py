# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中QTableView表格视图控件的例子
   
  
'''

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
        self.resize(650,600)
        #创建SQL模型
        self.model=QStandardItemModel(20,6)
        self.model.setHorizontalHeaderLabels(['商品编码','商品名称','型号','计量单位','单价','输出编码'])


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

        cursor.execute("SELECT commodityCode, commodityName, specification, chargeUnit,unitPrice,outputCode from information")

        self.results = cursor.fetchall()
        cursor.close()
        db.close()
        print(self.results)
        i = 0
        print(len(self.results))

        while(i < len(self.results)):
            self.model.setItem(i, 0,  QStandardItem(self.results[i]['commodityCode']))
            self.model.setItem(i, 1,  QStandardItem(self.results[i]['commodityName']))
            self.model.setItem(i, 2,  QStandardItem(self.results[i]['specification']))
            self.model.setItem(i, 3,  QStandardItem(self.results[i]['chargeUnit']))
            self.model.setItem(i, 4,  QStandardItem(str(self.results[i]['unitPrice'])))
            self.model.setItem(i, 5,  QStandardItem(self.results[i]['outputCode']))
            i = i+1

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

