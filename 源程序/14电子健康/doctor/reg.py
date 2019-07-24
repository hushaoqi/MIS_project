from ui_reg import Ui_Reg
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import pymysql
import glb
import re#3.18
class Reg(QMainWindow, Ui_Reg):
    def __init__(self):
        super(Reg, self).__init__()
        self.setupUi(self)
    def reg(self):
        self.passname = self.lineEdit.text()#账号
        #添加正则表达式3.18，匹配user和两位数字，从头开始匹配，匹配失败返回NONE
        pattern = re.compile("[u][s][e][r]\d{2}")  # 查找数字
        result1 = pattern.match(self.passname)
        #-----以上------
        self.password1 = self.lineEdit_2.text()#第一遍输入密码
        self.password2 = self.lineEdit_3.text()#第二遍输入密码
        self.name=self.lineEdit_4.text()#医生名字
        self.work=self.lineEdit_5.text()#医生职位
        self.kid=self.lineEdit_6.text()#科室ID
        self.yid=self.lineEdit_7.text()#医院ID
        if(self.password1!=self.password2):#判断两次密码是否一致
            QMessageBox.information(self,'Title','密码不一致')
        #--------修改--------
        elif len(self.passname) != 5 or result1==None:
            QMessageBox.information(self, 'Title', '请输入5位，user+两位数字')
        #-------修改---------
        else:#数据库操作
            conn = pymysql.connect("localhost", user="root", passwd="12345", db="hospital_management",
                                   port=3306, charset="utf8")
            cur = conn.cursor()
            sql="INSERT INTO 医生(医生ID,医生密码,姓名,职称,科室ID,医院ID) VALUES('%s','%s','%s','%s','%s','%s')" % (self.passname,self.password1,self.name,self.work,self.kid,self.yid)

            try:
                cur.execute(sql)
            except:#数据库出错
                QMessageBox.information(self,'Title','注册失败，用户已存在或者格式不对')
            else:
                conn.commit()
                cur.close()
                QMessageBox.information(self,'Title','注册成功')