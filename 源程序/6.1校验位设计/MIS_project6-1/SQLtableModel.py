# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlTableModel
from PyQt5.QtCore import Qt

class SqlShow(QWidget):
    def __init__(self,parent = None):
        super(SqlShow, self).__init__(parent)
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")  # set address
        db.setDatabaseName("com_information")
        db.setUserName("root");  # set user name
        db.setPassword("root");  # set user pwd
        #打开连接数据库
        dbConn = self.db.open()
        model = QSqlTableModel()
        delrow = -1
        self.initializeModel(model)
        view1 = self.createView("Table Model (View 1)", model)
        view1.clicked.connect(self.findrow)

        dlg = QDialog()
        layout = QVBoxLayout()
        layout.addWidget(view1)
        addBtn = QPushButton("添加一行")
        addBtn.clicked.connect(self.addrow)
        layout.addWidget(addBtn)

        delBtn = QPushButton("删除一行")
        delBtn.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
        layout.addWidget(delBtn)
        dlg.setLayout(layout)
        dlg.setWindowTitle("显示数据库")
        dlg.resize(650, 650)
        dlg.show()
        #关闭数据库
        db.close()
    def initializeModel(model):
        model.setTable('infomation')
        model.setEditStrategy( QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, Qt.Horizontal, "commodityCode")
        model.setHeaderData(1, Qt.Horizontal, "commodityName")
        model.setHeaderData(2, Qt.Horizontal, "specification")
        model.setHeaderData(3, Qt.Horizontal, "chargeUnit")
        model.setHeaderData(4, Qt.Horizontal, "unitPrice")
        model.setHeaderData(5, Qt.Horizontal, "outputCode")


    def createView(title, model):
        view =  QTableView()
        view.setModel(model)
        view.setWindowTitle(title)
        return view

    def addrow(model):
        ret = model.insertRows( model.rowCount(), 1 )
        print( 'insertRows=%s' %str(ret) )

    def findrow(i):
        delrow= i.row()
        print('del row=%s' % str(delrow) )




