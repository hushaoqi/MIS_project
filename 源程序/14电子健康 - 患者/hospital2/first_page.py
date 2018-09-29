from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import pymysql
from PyQt5.QtWidgets import *
class first_page(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()

    def setupUI(self):
        self.setGeometry(QtCore.QRect(259, 29, 1051, 671))
        self.setObjectName("first_page_widget")
        self.big_picture_label = QtWidgets.QLabel(self)
        self.big_picture_label.setGeometry(QtCore.QRect(0, 0, 1051, 351))
        self.big_picture_label.setText("")
        self.big_picture_label.setPixmap(QtGui.QPixmap("source/bloodborne.jpg"))
        self.big_picture_label.setObjectName("big_picture_label")
        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setGeometry(QtCore.QRect(0, 360, 1051, 301))
        self.tableView.setObjectName("tableView")

        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()

        sql = 'select 问题,内容 from 用药小贴士'
        cursor.execute(sql)
        db.close()
        self.results = cursor.fetchall()
        i = 0
        self.tableView.setColumnCount(2)
        self.tableView.setRowCount(len(self.results))
        self.tableView.setHorizontalHeaderLabels(["问题", "回答"])
        self.tableView.setColumnWidth(0, 450)
        self.tableView.setColumnWidth(1, 750)

        while (i < len(self.results)):
            self.tableView.setRowHeight(i, 100)
            self.tableView.setItem(i, 0, QTableWidgetItem(self.results[i][0]))
            self.tableView.setItem(i, 1, QTableWidgetItem(self.results[i][1]))
            i = i + 1
