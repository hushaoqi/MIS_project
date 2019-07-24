
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import pymysql
from getip import get_host_ip
from ui_patientrequest import Ui_Patientrequest
import glb

class Patientrequest(QMainWindow, Ui_Patientrequest):
    '''
    病人请求，私人医生
    '''

    def __init__(self):
        super(Patientrequest, self).__init__()
        self.setupUi(self)

    def Open(self):
        self.show()
        # 暂定选择医生3001的所有签约患者ID
        conn = pymysql.connect(host="localhost", user="root", passwd="12345", db="hospital_management",
                               port=3306, charset="utf8")
        cur = conn.cursor()
        docid=glb.get_value("DOCTOR_ID")
        sql="SELECT 患者ID FROM 病人私人医生 WHERE 医生ID='%s'" % (docid)
        cur.execute(sql)  # 找出患者ID
        sql = cur.fetchall()
        # 根据患者ID，找出患者所有信息
        for i in range(3):
            cur.execute("SELECT * FROM 患者 WHERE 患者ID=" + sql[i][0])
            string = cur.fetchone()
            if (i == 0):
                self.textEdit.setText(str(string))
            if (i == 1):
                self.textEdit_2.setText(str(string))
            if (i == 2):
                self.textEdit_3.setText(str(string))
        # 暂定记录三个患者ID
        self.patient_id0 = sql[0][0]
        self.patient_id1 = sql[1][0]
        self.patient_id2 = sql[2][0]
        print(self.patient_id0, "  ", self.patient_id1, "  ", self.patient_id2)
        cur.close()
        conn.close()

