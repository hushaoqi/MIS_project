# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'willingToAsk.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql as mc
import sys

class selectDocWin(QtWidgets.QWidget):
    
    def __init__(self,Dialog):
        super().__init__()
        
        
        self.widget = QtWidgets.QWidget()
        self.dialog = Dialog
        self.selectedDoc = "郭鸣轩"
        self.money = 100
        
        self.selectDept = "*"                 #select dept
        self.selectDocLv = "*"                #select docLv
        self.selectedDoc = ''               #selected Doctor
        self.doctorResult = []
        self.initUI(Dialog)
    #-------------------------------------------
    #
    #            选择医生职称
    #
    #-------------------------------------------
    def on_click_selectDocLv(self,selectDocLvBtn):
        if selectDocLvBtn == self.pushButton_allDocLv:
            self.doctorResult = []
            self.selectDocLv = "*"
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_allDocLv.setStyleSheet("background-color:blue;color:white")
            
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDept != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % (self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生"
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
        
        elif selectDocLvBtn == self.pushButton_zhengGao:
            self.doctorResult = []
            self.selectDocLv = "主任医师"
            self.money = 500
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_zhengGao.setStyleSheet("background-color:blue;color:white")
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDept != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'" % (self.selectDocLv)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
        
        elif selectDocLvBtn == self.pushButton_fuGao:
            self.doctorResult = []
            self.selectDocLv = "副主任医师"
            self.money = 400
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_fuGao.setStyleSheet("background-color:blue;color:white")
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDept != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'" % (self.selectDocLv)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
            
        elif selectDocLvBtn == self.pushButton_noDocLv:
            self.doctorResult = []
            self.selectDocLv = "实习生"
            self.money = 300
            
            self.pushButton_allDocLv.setStyleSheet("background-color:white;color:black")
            self.pushButton_zhengGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuGao.setStyleSheet("background-color:white;color:black")
            self.pushButton_noDocLv.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_noDocLv.setStyleSheet("background-color:blue;color:white")
            
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDept != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'" % (self.selectDocLv)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])

        
        
    #-------------------------------------------
    #
    #            选择科室
    #
    #-------------------------------------------
    
    def on_click_selectDept(self,selectDeptBtn):
        if selectDeptBtn == self.pushButton_alldept:
            self.doctorResult = []
            self.selectDept = "*"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_alldept.setStyleSheet("background-color:blue;color:white")
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDocLv != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                       WHERE 职称 = '%s'" % (self.selectDocLv)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生"
                cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
        
        elif selectDeptBtn == self.pushButton_erBiHouKe:
            self.doctorResult = []
            self.selectDept = "儿科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_erBiHouKe.setStyleSheet("background-color:blue;color:white")
            
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDocLv != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % (self.selectDept)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
        elif selectDeptBtn == self.pushButton_fuChanKe:
            self.doctorResult = []
            self.selectDept = "妇产科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_fuChanKe.setStyleSheet("background-color:blue;color:white")
            
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDocLv != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % (self.selectDept)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
        elif selectDeptBtn == self.pushButton_neiKe:
            self.doctorResult = []
            self.selectDept = "内科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_neiKe.setStyleSheet("background-color:blue;color:white")
            
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDocLv != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % (self.selectDept)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
        elif selectDeptBtn == self.pushButton_waiKe:
            self.doctorResult = []
            self.selectDept = "外科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_waiKe.setStyleSheet("background-color:blue;color:white")
            
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDocLv != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % (self.selectDept)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
            
        elif selectDeptBtn == self.pushButton_guKe:
            self.doctorResult = []
            self.selectDept = "骨科"
            
            self.pushButton_alldept.setStyleSheet("background-color:white;color:black")
            self.pushButton_erBiHouKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_fuChanKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_neiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_waiKe.setStyleSheet("background-color:white;color:black")
            self.pushButton_guKe.setStyleSheet("background-color:white;color:black")
            
            self.pushButton_guKe.setStyleSheet("background-color:blue;color:white")
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()
            if self.selectDocLv != '*':
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 职称 = '%s'\
                        AND 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % \
                        (self.selectDocLv,self.selectDept)
            else:
                sql = "SELECT 医生ID,姓名 FROM 医生 \
                        WHERE 科室ID = (SELECT 科室ID FROM 科室 WHERE 科室名 = '%s')" % (self.selectDept)
            cursor.execute(sql)
            self.doctorResult.append(cursor.fetchall())
            self.listWidget.clear()
            for i in self.doctorResult[0]:
                self.listWidget.addItem(i[1])
          
    def listClicked(self):
        #print(self.listWidget.currentRow())
        #print(self.doctorResult)
        self.selectedDoc = self.doctorResult[0][self.listWidget.currentRow()][0]
        print(self.selectedDoc)
    
    def initUI(self,Dialog):
        self.setObjectName("Form")
        self.resize(1100, 684)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        self.setFont(font)
        
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 1031, 131))
        self.groupBox.setObjectName("groupBox")
        
        self.label_dept = QtWidgets.QLabel(self.groupBox)
        self.label_dept.setGeometry(QtCore.QRect(10, 30, 72, 15))
        self.label_dept.setObjectName("label")
        self.label_docLv = QtWidgets.QLabel(self.groupBox)
        self.label_docLv.setGeometry(QtCore.QRect(10, 90, 72, 15))
        self.label_docLv.setObjectName("label_2")
        #----------------------set Search prerequisites-----------------------------------
        self.pushButton_alldept = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_alldept.setGeometry(QtCore.QRect(160, 20, 93, 28))
        self.pushButton_alldept.setObjectName("pushButton")
        self.pushButton_alldept.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_alldept))
        
        self.pushButton_allDocLv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_allDocLv.setGeometry(QtCore.QRect(160, 80, 93, 28))
        self.pushButton_allDocLv.setObjectName("pushButton_2")
        self.pushButton_allDocLv.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_allDocLv))
        
        self.pushButton_zhengGao = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_zhengGao.setGeometry(QtCore.QRect(330, 80, 93, 28))
        self.pushButton_zhengGao.setObjectName("pushButton_3")
        self.pushButton_zhengGao.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_zhengGao))
        
        self.pushButton_neiKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_neiKe.setGeometry(QtCore.QRect(330, 20, 93, 28))
        self.pushButton_neiKe.setObjectName("pushButton_4")
        self.pushButton_neiKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_neiKe))
        
        self.pushButton_waiKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_waiKe.setGeometry(QtCore.QRect(490, 20, 93, 28))
        self.pushButton_waiKe.setObjectName("pushButton_5")
        self.pushButton_waiKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_waiKe))
        
        self.pushButton_fuGao = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fuGao.setGeometry(QtCore.QRect(490, 80, 93, 28))
        self.pushButton_fuGao.setObjectName("pushButton_6")
        self.pushButton_fuGao.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_fuGao))
        
        self.pushButton_erBiHouKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_erBiHouKe.setGeometry(QtCore.QRect(790, 20, 93, 28))
        self.pushButton_erBiHouKe.setObjectName("pushButton_7")
        self.pushButton_erBiHouKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_erBiHouKe))
        
        self.pushButton_guKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_guKe.setGeometry(QtCore.QRect(640, 20, 93, 28))
        self.pushButton_guKe.setObjectName("pushButton_8")
        self.pushButton_guKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_guKe))
        
        self.pushButton_noDocLv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_noDocLv.setGeometry(QtCore.QRect(640, 80, 93, 28))
        self.pushButton_noDocLv.setObjectName("pushButton_10")
        self.pushButton_noDocLv.clicked.connect(lambda:self.on_click_selectDocLv(self.pushButton_noDocLv))
        
        self.pushButton_fuChanKe = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fuChanKe.setGeometry(QtCore.QRect(920, 20, 93, 28))
        self.pushButton_fuChanKe.setObjectName("pushButton_11")
        self.pushButton_fuChanKe.clicked.connect(lambda:self.on_click_selectDept(self.pushButton_fuChanKe))
        #--------------------------Searching Results-----------------------------
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 240, 1031, 401))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.listClicked)
                               #-------------Debug---------------#
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
        cursor = db.cursor()
        sql = "SELECT 医生ID,姓名 FROM 医生"
        cursor.execute(sql)
        self.doctorResult.append(cursor.fetchall())
        #print(self.doctorResult[0][1][0])
        self.listWidget.clear()
        for i in self.doctorResult[0]:
            self.listWidget.addItem(i[1])
        
        
        
        #--------------------------Read Essay Button-----------------------------
        self.readEssay = QtWidgets.QPushButton(Dialog)
        self.readEssay.setGeometry(QtCore.QRect(920, 150, 93, 28))
        self.readEssay.setObjectName("pushButton_11")
        
        #--------------------------Start chatting--------------------------------
        self.startChatting = QtWidgets.QPushButton(Dialog)
        self.startChatting.setGeometry(QtCore.QRect(920, 200, 93, 28))
        self.startChatting.setObjectName("pushButton_11")
        
        
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(480, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "筛选条件"))
        self.label_dept.setText(_translate("Form", "科室："))
        self.label_docLv.setText(_translate("Form", "医生职称："))
        self.pushButton_alldept.setText(_translate("Form", "全部"))
        self.pushButton_allDocLv.setText(_translate("Form", "全部"))
        self.pushButton_zhengGao.setText(_translate("Form", "主任医师"))
        self.pushButton_neiKe.setText(_translate("Form", "内科"))
        self.pushButton_waiKe.setText(_translate("Form", "外科"))
        self.pushButton_fuGao.setText(_translate("Form", "副主任医师"))
        self.pushButton_erBiHouKe.setText(_translate("Form", "儿科"))
        self.pushButton_guKe.setText(_translate("Form", "骨科"))
        self.pushButton_noDocLv.setText(_translate("Form", "实习生"))
        self.pushButton_fuChanKe.setText(_translate("Form", "妇产科"))
        self.label_result.setText(_translate("Form", "查询结果"))
        self.readEssay.setText(_translate("Form","阅读文章 "))
        self.startChatting.setText(_translate("Form","付费咨询 "))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = selectDocWin()
    win.show()
    sys.exit(app.exec_())









