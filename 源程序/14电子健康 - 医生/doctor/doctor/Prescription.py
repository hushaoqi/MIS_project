
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
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
        conn = pymysql.connect("localhost", user="root", passwd="12345", db="hospital_management",
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

    def showw(self, idd):
        conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM 药品 WHERE 药品名称=" + str(idd))
        nsql = cur.fetchone()
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
        self.medi_id_list.append(idd)

        string = string + str(idd) + "   " + nname + "\n"
        self.textEdit.setText(string)

    def Finish(self):
        length = len(self.medi_id_list)
        conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()

        for i in range(length):
            timer = time.strftime('%Y-%m-%d')
            cur.execute(
                "INSERT INTO 开药单(患者ID,药品ID,时间) VALUES('%s','%d','%s')" % (self.patient_id, self.medi_id_list[i], timer))
            conn.commit()
        cur.close()
        conn.close()
        self.Clear()

