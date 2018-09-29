

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
        self.patient_id = patient_id
        conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT 主诉 FROM 病历 WHERE 患者ID=" + patient_id)
        string = cur.fetchone()

        self.textEdit.setText(str(string))
