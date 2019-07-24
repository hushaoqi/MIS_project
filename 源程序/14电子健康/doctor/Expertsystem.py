from ui_expertsystem import Ui_Expertsystem
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql
from getip import get_host_ip
import glb
class Expertsystem(QMainWindow ,Ui_Expertsystem):
    '''
    专家系统
    '''
    def __init__(self):
        super(Expertsystem ,self).__init__()
        self.setupUi(self)
    def Open(self ,patient_id):
        self.show()
        print("expert_system_open函数")
        self.patient_id =patient_id
        conn = pymysql.connect(host="localhost", user="root", passwd="12345", db="hospital_management", port=3306, charset="utf8")
        cur = conn.cursor()
        sql = "SELECT 专家系统诊断结果 FROM 专家系统结果 WHERE 患者ID= %s "%str(self.patient_id)
        cur.execute(sql)
        string =cur.fetchone()
        print("expert_system_open函数_数据库",string[0])
        self.textEdit.setText(string[0])
