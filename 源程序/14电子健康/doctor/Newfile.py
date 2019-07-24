

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql
from getip import get_host_ip
from ui_newfile import Ui_Newfile
import glb

class Newfile(QMainWindow, Ui_Newfile):
    '''
    病历
    '''

    def __init__(self):
        super(Newfile, self).__init__()
        self.setupUi(self)

    def Open(self, patient_id):
        self.show()
        print("main_open 函数")
        print("查看病历")
        self.patient_id = patient_id

        print("患者ID",self.patient_id)
        conn = pymysql.connect(host="localhost", user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        sql = "SELECT 主诉 FROM 病历 WHERE 患者ID='%s' "%self.patient_id
        cur.execute(sql)
        self.string = cur.fetchone()
        print("检索数据库中病历",self.string)
        self.textEdit.setText(str(self.string))
