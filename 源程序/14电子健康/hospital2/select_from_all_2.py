
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pymysql
class chosePMD_from_AP_widget_2(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8' )
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()


        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.setObjectName("chosePMD_from_AP_widget_2")
        self.area_comboBox = QtWidgets.QComboBox(self)
        self.area_comboBox.setGeometry(QtCore.QRect(260, 40, 201, 26))
        self.area_comboBox.setObjectName("area_comboBox")
        self.area_comboBox.addItem("中山区")  # 地区排序
        self.area_comboBox.addItem("金州区")
        self.area_comboBox.addItem("西岗区")
        #self.area_comboBox.activated[str].connect(self.sort)
        self.ComRan_comboBox = QtWidgets.QComboBox(self)
        self.ComRan_comboBox.setGeometry(QtCore.QRect(20, 40, 201, 26))
        self.ComRan_comboBox.setObjectName("ComRan_comboBox")
        self.ComRan_comboBox.addItem("综合排序")
        self.ComRan_comboBox.addItem("满意度排序")
        #self.ComRan_comboBox.activated[str].connect(self.sort)
        self.department_comboBox = QtWidgets.QComboBox(self)
        self.department_comboBox.setGeometry(QtCore.QRect(490, 40, 201, 26))
        self.department_comboBox.setObjectName("department_comboBox")
        self.department_comboBox.addItem("外科")#科室排序
        self.department_comboBox.addItem("内科")
        self.department_comboBox.addItem("儿科")
        #self.department_comboBox.activated[str].connect(self.sort)
        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setGeometry(QtCore.QRect(20, 130, 911, 491))
        self.tableView.setObjectName("tableView")

        sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院'
        # 执行SQL语句
        cursor.execute(sql)
        db.close()
        # 获取所有记录列表
        self.results = cursor.fetchall()
        #print(results)
        i = 0
        self.button_list=[]
        # 设置表格有34行5列。
        self.tableView.setColumnCount(6)
        self.tableView.setRowCount(34)
        self.tableView.setHorizontalHeaderLabels(["姓名", "职称", "科室", "医院", "好评率", "选择"])
        # self.tableView.setVerticalHeaderLabels(["第一列", "第二列"])
        self.tableView.setColumnWidth(0, 150)
        self.tableView.setColumnWidth(1, 150)
        self.tableView.setColumnWidth(2, 150)
        self.tableView.setColumnWidth(3, 150)
        self.tableView.setColumnWidth(4, 150)
        self.tableView.setColumnWidth(5, 150)
        while (i < len(self.results)):
            self.tableView.setRowHeight(i, 100)
            self.tableView.setItem(i, 0, QTableWidgetItem(self.results[i][0]))
            self.tableView.setItem(i, 1, QTableWidgetItem(self.results[i][1]))
            self.tableView.setItem(i, 2, QTableWidgetItem(str(self.results[i][2])))
            self.tableView.setItem(i, 3, QTableWidgetItem(str(self.results[i][3])))
            self.tableView.setItem(i, 4, QTableWidgetItem(str(self.results[i][4])))
            button = QPushButton()
            self.button_list.append(button)
            button.setStyleSheet(''' text-align : center;
                                     background-colo
                                     self.retranslateUi()r : LightCoral;
                                     height : 30px;
                                     border-style: outset;
                                     font : 13px; ''')
            #button.clicked.connect(lambda: self.tiaozhuan(results[self.tableView.currentRow()][5]))
            self.tableView.setCellWidget(i, 5, button)
            i = i + 1