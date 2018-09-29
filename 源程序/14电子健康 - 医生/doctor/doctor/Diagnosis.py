from ui_diagnosis import Ui_Diagnosis
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql
from getip import get_host_ip
import glb

class Diagnosis(QMainWindow,Ui_Diagnosis):
    '''
    治疗方案
    '''
    def __init__(self):
        super(Diagnosis,self).__init__()
        self.setupUi(self)

    def Open(self,patient_id):
        self.show()
        self.doctor_id = glb.get_value("DOCTOR_ID")
        self.patient_id=patient_id
    def Finish(self):
        string1=self.textEdit.toPlainText()
        string2=self.textEdit_2.toPlainText()
        string3=self.textEdit_3.toPlainText()
        string4=self.textEdit_4.toPlainText()
        string5=self.textEdit_5.toPlainText()
        string6=self.textEdit_6.toPlainText()
        string="姓名:"+string1+"  "+"时间:"+string2+"  "+"诊断:"+string3+"  "+"注意:"+string4+"  "+"禁忌"+string5+\
               "  "+"备注"+string6
        conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user = "root", passwd="12345",
                               db="hospital_management", port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute("INSERT INTO 治疗方案(患者ID,医生ID,方案) VALUES ('%s','%s','%s') "
                    % (self.patient_id,self.doctor_id,string))
        conn.commit()
        cur.close()
        conn.close()