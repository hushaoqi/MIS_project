# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:43:29 2018

@author: DELL
"""
import socket
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import pymysql
import time
from getip import get_host_ip
from Diagnosis import Diagnosis
from Expertsystem import Expertsystem
from Login import Login
from Patientrequest import Patientrequest
from Prescription import Prescription
from chattingWin import Ui_chattingWin
from Newfile import Newfile
from ui_doctor import Ui_Doctor
import glb # 全局变量

glb._init()  # 用作全局变量的声明，只在主函数声明一次
glb.set_value("MYSQL_IP", "10.28.248.45")

class Doctor(QMainWindow,Ui_Doctor):
    '''
    mainwindows
    '''
    def __init__(self):
        super(Doctor, self).__init__()
        self.setupUi(self)
        jpg=QtGui.QPixmap('source/1.jpg')
        self.label_2.setPixmap(jpg)
        self.newflag=1
    def Open(self,flag):
        self.flag=flag
        if(self.flag==1):
            self.show()
                        

class ChattingWin(QMainWindow,Ui_chattingWin):
    '''
    聊天界面
    '''
    def __init__(self):

        super(ChattingWin,self).__init__()
        self.initUI()   
        self.patient_id=0
        self.newflag = 1
    def Check(self,newflag):
        self.newflag=newflag
        
        
        
        
    def Open(self,patient_id):

        self.show()
        if(self.newflag!=1):
            self.patient_id = patient_id
            print(self.patient_id)
        else:
            self.patient_id=self.newpatient_id
            
        if patient_id is None:
            pass
        else:
            self.patient_id=patient_id
    


if __name__ =="__main__":


    app = QApplication(sys.argv)
    doctor = Doctor()             # 主界面
    diagnosis=Diagnosis()   # 治疗方案
    expertsystem=Expertsystem()   # 专家系统，查看
    newfile=Newfile()             # 查看病历
    patientrequest=Patientrequest()  # 私人医生，查看签约患者
    prescription= Prescription()     # 在线药房，开药
    chattingWin=ChattingWin()  # 聊天
    main=Login()    # 登录

    main.show()

    # 登录界面
    main.pushButton.clicked.connect(main.login)
    main.pushButton.clicked.connect(lambda:doctor.Open(main.login_is_sucess_flag))
    main.pushButton.clicked.connect(lambda:main.Close(main.login_is_sucess_flag))

    # 点击有人咨询
    doctor.pushButton.clicked.connect(lambda:chattingWin.Check(doctor.newflag))
    doctor.pushButton.clicked.connect(lambda:chattingWin.Open("1234567890"))

    # 点击私人医生
    doctor.pushButton_2.clicked.connect(patientrequest.Open) # 显示签约患者信息
    
    # 点击在线药房
    doctor.pushButton_3.clicked.connect(lambda:prescription.Open(None))  # 记得传参数，病人id

    # 治疗方案
    diagnosis.pushButton.clicked.connect(diagnosis.Finish)
    diagnosis.pushButton_2.clicked.connect(diagnosis.close)

    chattingWin.pushButton_2.clicked.connect(lambda:newfile.Open(str(chattingWin.patient_id)))
    chattingWin.pushButton_3.clicked.connect(lambda:prescription.Open(str(chattingWin.patient_id)))
    chattingWin.pushButton_4.clicked.connect(lambda:expertsystem.Open(str(chattingWin.patient_id)))
    chattingWin.pushButton_5.clicked.connect(lambda:diagnosis.Open(str(chattingWin.patient_id)))
    
    
    newfile.pushButton.clicked.connect(newfile.close)
    
    
    prescription.pushButton_2.clicked.connect(prescription.Clear)
    prescription.pushButton_3.clicked.connect(prescription.Clear)
    prescription.pushButton_4.clicked.connect(prescription.Clear)
    prescription.pushButton_6.clicked.connect(prescription.close)
    prescription.pushButton_5.clicked.connect(prescription.Finish)
    prescription.pushButton_7.clicked.connect(prescription.Add)
    
    
    expertsystem.pushButton.clicked.connect(expertsystem.close)
    
    
    
    # 查看签约患者页面，点击第一个患者，进入聊天界面
    patientrequest.pushButton.clicked.connect(lambda:chattingWin.Open(patientrequest.patient_id0))
    patientrequest.pushButton_2.clicked.connect(lambda:chattingWin.Open(patientrequest.patient_id1))
    patientrequest.pushButton_3.clicked.connect(lambda:chattingWin.Open(patientrequest.patient_id2))
    patientrequest.pushButton_4.clicked.connect(patientrequest.close)
    
    
    
    
    sys.exit(app.exec_())