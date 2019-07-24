import sys
#from UI文件.login_patient import  Ui_Dialog
#from UI文件.main import Ui_Form
from login_gerneral import Ui_Dialog
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
import pymysql
from PyQt5 import QtWidgets
from 账户密码错误 import model_dialog_show_str
from main import main
class dialog(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 按钮绑定
        self.logistic_connect()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏的代码
        self.show()
        self.patient_register_widget.close()
    def logistic_connect(self):
        #self.login_button.clicked.connect(self.if_patient_login_correct)
        self.register_button.clicked.connect(self.register_button_clicked)
        self.register_cancle_button.clicked.connect(self.cancle_button_clicked)
        self.register_submit_button.clicked.connect(self.register_submit)
        self.subtrack_button.clicked.connect(self.showMinimized)
        self.close_button.clicked.connect(QCoreApplication.instance().quit)
        self.login_button.clicked.connect(self.if_patient_login_correct)
    '''在这些就得不到main的对象了
    def if_patient_login_correct(self):#登录按钮
        print(123)
        self.close()
    '''
    def register_button_clicked(self):#注册按钮
        self.login_Dialog.close()
        self.patient_register_widget.show()
    def cancle_button_clicked(self):#返回按钮
        self.patient_register_widget.close()
        self.login_Dialog.show()
    def judge_age(self,age):
        if len(age) == 0 or len(age) > 3:
            return True
        if len(age) == 1 and (age[0] <'0' or age[0] > '9'):
            return True
        if len(age) == 2 and (age[0] <'0' or age[0] > '9') and (age[1] <'0' or age[1] > '9'):
            return True
        if len(age) == 3 and (age[0] <'0' or age[0] > '9') and (age[1] <'0' or age[1] > '9') and (age[2] <'0' or age[2] > '9'):
            return True
        return False
    def register_submit(self):#提交按钮
        id=self.registerid_input.text()
        psw=self.register_password_input.text()
        name=self.register_name_input.text()
        idcard=self.register_idcard_input.text()
        add=self.register_address_input.text()
        age=self.register_age_input.text()
        print(self.judge_age(age))
        if self.judge_age(age):
            QMessageBox.warning(self, "警告", "信息数据格式错误!!", QMessageBox.Cancel)
        else:
            if(id!='' and psw!=''and name!=''and idcard!=''and add!=''and age!=''):
                db = pymysql.connect("localhost", "root",
                                     "12345", "hospital_management", charset='utf8')
                # 使用cursor()方法获取操作游标
                cursor = db.cursor()
                res=[id,psw,name,idcard,add,age]
                flag = 1#标志是否注册成功
                sql="insert into 患者(患者ID,登录密码,姓名,身份证号码,地址,年龄)values(%s,%s,%s,%s,%s,%s)"
                try:
                    cursor.execute(sql,res)
                    db.commit()
                except:
                    QMessageBox.warning(self, "警告", "注册信息id重复!!", QMessageBox.Cancel)
                    flag = 0
                db.close()
                #弹窗
                if flag:
                    dialog = model_dialog_show_str(str="注册成功")
                    dialog.exec_()

            else:
                #弹窗
                dialog = model_dialog_show_str(str="请输入正确的信息")
                dialog.exec_()

                print(12345)
    #鼠标拖拽
    def if_patient_login_correct(self):  # 登录按钮
        # 获取登录信息
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        #self.patient_ID = self.my_dialog.patient_ID_input.text()

        # self.win_reDiagnose.patientID=self.patient_ID
        # self.win_question.patientID=self.patient_ID
        # self.win_privatePharmacy.win_medicineList.patientID=self.patient_ID
        patient_psw = self.patient_password_input.text()
        sql = "select 登录密码 from 患者 where 患者ID=%s"
        cursor.execute(sql, self.patient_ID_input.text())
        psw = cursor.fetchone()
        db.close()
        # print(psw)
        # print(str('(\'')+patient_psw+str('\',)'))
        if str(psw) == str('(\'') + patient_psw + str('\',)'):
            m=main(self.patient_ID_input.text())
            m.show()
            self.close()
            #m.my_dialog.close()
            # ----------------------在此处填写代码，其他widget要关掉-----------------------
            # self.first_page_widget.close()
            m.profile_widget.close()
            m.second_page_widget.close()
            m.fifth_page_widget.close()
            m.select_hot_widget_2.close()
            m.select_all_widget_2.close()
            m.sign_doctor_widget.close()
            m.pay_widget.close()
            m.new_patient_widget.close()
            m.pro_sys_widget.close()
            #m.com_widget.close()
            m.third_page_widget.close()
            m.sixth_page_widget.close()
            m.forth_page_widget.close()
            m.pay_widget_2.close()
            m.my_record_widget.close()
            # 每个跳转都要有
            m.current_widget = m.first_page_widget  # 设置当前显示widget
        else:
            dialog = model_dialog_show_str(str="用户名或密码错误")
            dialog.exec_()
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_dialog=dialog()
    sys.exit(app.exec_())