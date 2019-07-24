
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import pymysql
from getip import get_host_ip
from ui_prescription import Ui_Prescription
import glb
import time

class Prescription(QMainWindow, Ui_Prescription):
    '''
    在线药房，
    '''

    def __init__(self):
        super(Prescription, self).__init__()
        self.setupUi(self)
        self.comboBox.clear()
        conn = pymysql.connect(host="localhost", user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        length = cur.execute("SELECT 药品ID,药品名称 FROM 药品 ")
        sql = cur.fetchall()
        for i in range(length):
            self.comboBox.insertItem(sql[i][0], sql[i][1])
        cur.close()
        conn.close()

        self.comboBox.activated[int].connect(self.showw)
        self.medi_id_list = []

    def showw(self, idd):  # idd游标与药品ID不符，需要+1处理
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM 药品 WHERE 药品ID=%s"%str(idd+1))
        nsql = cur.fetchone()
        print("idd:", idd, "药品信息：", nsql)
        self.textEdit_2.setText(str(nsql))

    def Open(self, patient_id):
        print("Prescription.Open(self,patient_id):", patient_id)
        self.show()
        if (patient_id == None):  # 如果从doctor主页进入
            pass
        else:
            self.patient_id = patient_id  # 从聊天界面进入

    def Clear(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")

    def Add(self):
        string = self.textEdit.toPlainText()
        idd = self.comboBox.currentIndex()

        nname = self.comboBox.itemText(idd)
        self.medi_id_list.append(idd+1)

        string = string + str(idd+1) + "   " + nname + "\n"
        self.textEdit.setText(string)

        print("获取idd:", idd, "nname:", nname,"string:",string)
    def Finish(self):
        length = len(self.medi_id_list)
        print("self.medi_id_list内容", self.medi_id_list)
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        try:
            for i in range(length):
                timer = time.strftime('%Y-%m-%d')
                print(timer)
                print("self.medi_id_list[i]内容", self.medi_id_list[i])

                # sql="UPDATE  开药单 SET 患者ID='%s',药品ID='%d',时间) VALUES('%s','%d','%s')" % (self.patient_id, self.medi_id_list[i], timer)
                sql="INSERT INTO 开药单(患者ID,药品ID,时间) VALUES('%s','%d','%s')" % (self.patient_id, self.medi_id_list[i], timer)
                print("执行在线药房sql:",sql)
                cur.execute(sql)
                print("执行_在线药房sql成功")
                conn.commit()
                print("提交_在线药房sql成功")

            # timer = time.strftime('%Y-%m-%d')
            # print(timer)
            #
            # sql="INSERT INTO 开药单(患者ID,药品ID,时间) VALUES('%s','%d','%s')" % (self.patient_id, self.medi_id_list[0], timer)
            # print("执行在线药房sql:",sql)
            # cur.execute(sql)
            # print("执行_在线药房sql成功")
            # conn.commit()
            # print("提交_在线药房sql成功")
        except:
            QMessageBox.information(self,'Title','没有选择患者或者药房已经开过')
        else:
            cur.close()
            conn.close()
            self.Clear()

