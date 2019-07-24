#from UI文件.login_patient import  Ui_Dialog
#from UI文件.main import Ui_Form
from PyQt5.QtWidgets import *
from general import Ui_Form
from mysql import conn_mysql
from HHP_scrollarea_widget import HHP_scrollarea_widget
from pro_sys_reuslt import pro_sys_result
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
import pymysql
from PyQt5 import QtCore, QtWidgets

from mainWin import mainWin
from privatePharmacy import privatePharmacy
from reDiaMainWin import reDiaMainWin
from chattingWin import chattingWin
class main(QWidget,Ui_Form):
    def __init__(self,patientid):
        super().__init__()
        self.patient_ID=patientid
        self.my_doc_id = ""
        self.time_long = "一小时"
        # third
        self.third_page_widget = QtWidgets.QWidget(self)
        self.third_page_widget.setGeometry(QtCore.QRect(230, 30, 1081, 676))
        self.win_question = mainWin(self.third_page_widget,self.patient_ID)
        # forth
        self.forth_page_widget = QtWidgets.QWidget(self)
        self.forth_page_widget.setGeometry(QtCore.QRect(230, 30, 1081, 676))
        self.win_reDiagnose = reDiaMainWin(self.forth_page_widget,self.patient_ID)
        # sixth
        self.sixth_page_widget = QtWidgets.QWidget(self)
        self.sixth_page_widget.setGeometry(QtCore.QRect(230, 30, 1081, 676))
        self.win_privatePharmacy = privatePharmacy(self.sixth_page_widget,self.patient_ID)



        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏的代码
        self.setupUi(self)
        self.logistic_cn()
        self.proviate_doc=False
        self.pro_sys_info = []
        for i in range(60):
            self.pro_sys_info.append("0")
    def logistic_cn(self):
        #self.my_dialog.login_button.clicked.connect(self.if_patient_login_correct)
        self.close_button.clicked.connect(self.close)
        self.subtract_button.clicked.connect(self.showMinimized)
        self.profile_button.clicked.connect(self.show_profile)
        self.second_page_button.clicked.connect(self.show_second_page)

        self.first_page_button.clicked.connect(self.show_first_page)
        self.forth_page_button.clicked.connect(self.show_forth_page)
        self.fifth_page_button.clicked.connect(self.show_fifth_page)
        self.sixth_page_button.clicked.connect(self.show_sixth_page)
        self.second_page_widget.pushButton.clicked.connect(self.show_pay_widget_regi)#挂号页的提交按钮
        self.second_page_widget.pushButton_2.clicked.connect(self.show_first_page)#挂号页的取消按钮
        self.second_page_widget.comboBox.activated[str].connect(self.paint_department)
        self.second_page_widget.comboBox_2.activated[str].connect(lambda:self.get_department(self.second_page_widget.comboBox_2.currentText()))

        self.third_page_button.clicked.connect(self.on_click_thirdPage)
        self.pay_widget_2.pushButton.clicked.connect(self.com_pay)

        self.fifth_page_widget.no_answer_button.clicked.connect(self.select_all_doctor)#私人医生页的所有医生按钮
        self.profile_widget.medical_record_button.clicked.connect(self.show_my_record)
        #self.fifth_page_widget.pushButton_2.clicked.connect(self.select_relative_doctor)#私人医生页的部分医生按钮！！可能要改，按钮是自动生成的
        #self.select_hot_widget.chose_pushButton.clicked.connect(self.show_sign_doctor)
        self.second_page_widget.comboBox_3.activated[str].connect(self.get_time_long)
        self.select_hot_widget_2.area_comboBox_2.activated[str].connect(self.sort)
        self.select_hot_widget_2.ComRan_comboBox_2.activated[str].connect(self.sort)
        self.second_page_widget.radioButton.toggled.connect(lambda :self.get_re_per("为自己挂号"))
        self.second_page_widget.radioButton_2.toggled.connect(lambda :self.get_re_per("为他人挂号"))
        self.second_page_widget.radioButton_3.toggled.connect(lambda :self.get_doc("推荐医生"))
        self.second_page_widget.radioButton_4.toggled.connect(lambda :self.get_doc("自己选择"))
        for i in range(len(self.select_hot_widget_2.button_list)):
            self.select_hot_widget_2.button_list[i].clicked.connect(lambda: self.show_sign_doctor(
                self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))

        #self.select_all_widget.chose_pushButton.clicked.connect(self.show_sign_doctor)
        #绑定所有按钮
        #绑定不在这里做了,换成combobox的绑定
        self.select_all_widget_2.area_comboBox.activated[str].connect(self.sort_2)
        self.select_all_widget_2.department_comboBox.activated[str].connect(self.sort_2)
        self.select_all_widget_2.ComRan_comboBox.activated[str].connect(self.sort_2)

        # 绑定私人医生新建病情调查选择按钮绑定
        self.new_patient_widget.pushButton.clicked.connect(lambda :self.show_pro_sys(self.pro_sys_info))
        self.new_patient_widget.checkBox00.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox01.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox02.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox03.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox10.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox11.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox12.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox13.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox20.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox21.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox22.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox30.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox31.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox32.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox40.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox41.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox42.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox43.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox44.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox45.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox46.clicked.connect(self.record_pro_sys_info)
        self.new_patient_widget.checkBox47.clicked.connect(self.record_pro_sys_info)

        for i in range(len(self.select_all_widget_2.button_list)):
             self.select_all_widget_2.button_list[i].clicked.connect(lambda :self.show_sign_doctor(
                 self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
        self.sign_doctor_widget.chose_Button.clicked.connect(self.show_pay_widget)#支付
        self.pay_widget.pushButton.clicked.connect(self.show_new_patient)
        self.pro_sys_widget.pushButton.clicked.connect(self.show_com)
    def get_time_long(self,text):
        print("get_time_long :" + text)
        self.time_long=text
    def show_pay_widget_regi(self):
        if self.my_doc_id == "":
            QMessageBox.warning(self, "警告", "请将所有信息填写完整", QMessageBox.Cancel)
        else:
            self.current_widget.close()
            self.pay_widget_2.show()
        # 每个跳转都要有
            self.current_widget = self.pay_widget_2
    def get_re_per(self,text):
        #print(text)
        self.re_per=text#返回注册类型
    def com_pay(self):#完成支付该干些什么
        self.current_widget.close()
        self.first_page_widget.show()
        # 每个跳转都要有
        self.current_widget = self.first_page_widget
        #后台将False设置为True
        #更新挂号信息进入数据库
        regi_ID=str(self.second_page_widget.dateTimeEdit.text())[0:8]+str(self.patient_ID)[0:2]
        pati_ID=self.patient_ID

        docid=self.my_doc_id             #挂号时指定的医生ID
        if self.re_per=="为自己挂号":
            type = 1
        else:
            type=0
        time=self.second_page_widget.dateTimeEdit.text()
        timelong=self.time_long
        res=[regi_ID,pati_ID,docid,type,time,timelong]
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        sql = 'INSERT INTO 挂号单(挂号ID,患者ID, 医生ID, 挂号类型, 挂号开始时间,挂号时长)VALUES (%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql, res)
            db.commit()
            db.close()
        except:
            QMessageBox.warning(self, "警告", "挂号信息重复!!", QMessageBox.Cancel)
            db.close()
        print("挂号完成\n")
    def show_my_record(self):
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        sql = 'select * from 病历  where 患者ID=%s'
        cursor.execute(sql, self.patient_ID)
        db.close()

        results=cursor.fetchall()
        self.my_record_widget.tableView.setColumnCount(7)
        self.my_record_widget.tableView.setRowCount(len(results))
        self.my_record_widget.tableView.setHorizontalHeaderLabels(["病历ID", "患者ID", "存档时间", "主诉", "住院时间", "住院号", "医生ID"])
        self.my_record_widget.tableView.setColumnWidth(0, 150)
        self.my_record_widget.tableView.setColumnWidth(1, 150)
        self.my_record_widget.tableView.setColumnWidth(2, 150)
        self.my_record_widget.tableView.setColumnWidth(3, 150)
        self.my_record_widget.tableView.setColumnWidth(4, 150)
        self.my_record_widget.tableView.setColumnWidth(5, 150)
        self.my_record_widget.tableView.setColumnWidth(6, 150)
        print(results)
        i=0
        if(len(results)!=0):
            while (i < len(results)):
                self.my_record_widget.tableView.setRowHeight(i, 100)
                self.my_record_widget.tableView.setItem(i, 0, QTableWidgetItem(str(results[i][0])))
                self.my_record_widget.tableView.setItem(i, 1, QTableWidgetItem(str(results[i][1])))
                self.my_record_widget.tableView.setItem(i, 2, QTableWidgetItem(str(results[i][2])))
                self.my_record_widget.tableView.setItem(i, 3, QTableWidgetItem(str(results[i][3])))
                self.my_record_widget.tableView.setItem(i, 4, QTableWidgetItem(str(results[i][4])))
                self.my_record_widget.tableView.setItem(i, 5, QTableWidgetItem(str(results[i][5])))
                i = i + 1
        self.current_widget.close()
        self.my_record_widget.show()
        # 每个跳转都要有
        self.current_widget = self.my_record_widget
    def on_click_thirdPage(self):
        self.current_widget.close()
        self.third_page_widget.show()
        # 每个跳转都要有
        self.current_widget = self.third_page_widget
    def show_sixth_page(self):
        self.current_widget.close()
        self.sixth_page_widget.show()
        # 每个跳转都要有
        self.current_widget = self.sixth_page_widget
    def show_forth_page(self):
        self.current_widget.close()
        self.forth_page_widget.show()
        # 每个跳转都要有
        self.current_widget = self.forth_page_widget
    def get_department(self,department):
        self.my_department=department#保存科室信息
    def paint_department(self,hosipital_name):
        #重新绘制科室窗口
        self.hospital_name=hosipital_name#保存医院名
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        sql = 'select  distinct 科室名 from 医院 natural join 医院科室 natural join 科室 where 医院名=%s'
        cursor.execute(sql,hosipital_name)
        db.close()
        results_depa = cursor.fetchall()
        #把原来的去掉
        self.second_page_widget.comboBox_2.clear()
        for i in range(len(results_depa)):
            self.second_page_widget.comboBox_2.addItem(results_depa[i][0])
    def get_doc(self,text):
        #print(text)
        self.my_doc=text
        #刷新界面
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        if(text=="推荐医生"):
            try:# do some thing you need
                print(self.hospital_name)
            except AttributeError as e:
                # error: has not attribute
                print(212)
                self.hospital_name="大连市友谊医院"
            try:# do some thing you need
                print(self.my_department)
            except AttributeError as e:
                # error: has not attribute
                self.my_department="内科"
            print(self.hospital_name,self.my_department)
            if self.hospital_name=="" or self.my_department=="":
                QMessageBox.warning(self, "警告", "请将所有信息填写完整", QMessageBox.Cancel)
            else:
                res=[self.hospital_name,self.my_department]#医院名，科室名
                sql='select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 医院名=%s and 科室名=%s'
                cursor.execute(sql,res)
                db.close()
                results_hosi = cursor.fetchall()
                self.second_page_widget.tableView.setColumnCount(6)
                self.second_page_widget.tableView.setHorizontalHeaderLabels(["姓名", "职称", "科室", "医院", "好评率", "选择"])
                self.second_page_widget.tableView.setColumnWidth(0, 150)
                self.second_page_widget.tableView.setColumnWidth(1, 150)
                self.second_page_widget.tableView.setColumnWidth(2, 150)
                self.second_page_widget.tableView.setColumnWidth(3, 150)
                self.second_page_widget.tableView.setColumnWidth(4, 150)
                self.second_page_widget.tableView.setColumnWidth(5, 150)
                print(results_hosi)
                i=0
                self.second_page_widget.tableView.setRowCount(len(results_hosi))
                self.second_page_widget.tableView.clearContents()
                while (i < len(results_hosi)):
                    self.second_page_widget.tableView.setRowHeight(i, 100)
                    self.second_page_widget.tableView.setItem(i, 0, QTableWidgetItem(results_hosi[i][0]))
                    self.second_page_widget.tableView.setItem(i, 1, QTableWidgetItem(results_hosi[i][1]))
                    self.second_page_widget.tableView.setItem(i, 2, QTableWidgetItem(str(results_hosi[i][2])))
                    self.second_page_widget.tableView.setItem(i, 3, QTableWidgetItem(str(results_hosi[i][3])))
                    self.second_page_widget.tableView.setItem(i, 4, QTableWidgetItem(str(results_hosi[i][4])))
                    button = QPushButton()
                    button.setStyleSheet(''' text-align : center;
                                                             background-colo
                                                             self.retranslateUi()r : LightCoral;
                                                             height : 30px;
                                                             border-style: outset;
                                                             font : 13px; ''')
                    button.clicked.connect(lambda: self.set_doc_id(results_hosi[self.second_page_widget.tableView.currentRow()][5]))
                    self.second_page_widget.tableView.setCellWidget(i, 5, button)
                    i = i + 1
        else:
            try:# do some thing you need
                print(self.hospital_name)
            except AttributeError as e:
                # error: has not attribute
                self.hospital_name="大连市友谊医院"
            try:# do some thing you need
                print(self.my_department)
            except AttributeError as e:
                # error: has not attribute
                self.my_department="内科"
            if self.hospital_name=="" or self.my_department=="":
                QMessageBox.warning(self, "警告", "请将所有信息填写完整", QMessageBox.Cancel)
            else:
                res = [self.hospital_name, self.my_department]  # 医院名，科室名
                sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 医院名=%s and 科室名=%s'
                cursor.execute(sql,res)
                db.close()
                results_hosi = cursor.fetchall()
                self.second_page_widget.tableView.setColumnCount(6)
                self.second_page_widget.tableView.setHorizontalHeaderLabels(["姓名", "职称", "科室", "医院", "好评率", "选择"])
                self.second_page_widget.tableView.setColumnWidth(0, 150)
                self.second_page_widget.tableView.setColumnWidth(1, 150)
                self.second_page_widget.tableView.setColumnWidth(2, 150)
                self.second_page_widget.tableView.setColumnWidth(3, 150)
                self.second_page_widget.tableView.setColumnWidth(4, 150)
                self.second_page_widget.tableView.setColumnWidth(5, 150)
                print(results_hosi)
                i = 0
                self.second_page_widget.tableView.setRowCount(len(results_hosi))
                self.second_page_widget.tableView.clearContents()
                while (i < len(results_hosi)):
                    self.second_page_widget.tableView.setRowHeight(i, 100)
                    self.second_page_widget.tableView.setItem(i, 0, QTableWidgetItem(results_hosi[i][0]))
                    self.second_page_widget.tableView.setItem(i, 1, QTableWidgetItem(results_hosi[i][1]))
                    self.second_page_widget.tableView.setItem(i, 2, QTableWidgetItem(str(results_hosi[i][2])))
                    self.second_page_widget.tableView.setItem(i, 3, QTableWidgetItem(str(results_hosi[i][3])))
                    self.second_page_widget.tableView.setItem(i, 4, QTableWidgetItem(str(results_hosi[i][4])))
                    button = QPushButton()
                    button.setStyleSheet(''' text-align : center;
                                                                         background-colo
                                                                         self.retranslateUi()r : LightCoral;
                                                                         height : 30px;
                                                                         border-style: outset;
                                                                         font : 13px; ''')
                    button.clicked.connect(lambda: self.set_doc_id(results_hosi[self.second_page_widget.tableView.currentRow()][5]))
                    self.second_page_widget.tableView.setCellWidget(i, 5, button)
                    i = i + 1
                pass
    def set_doc_id(self,text):
        self.my_doc_id=text
        self.if_ready=False
        #挂号之后就更新，把if_ready设置为true
    def sort(self,text):

        #根据传过来的科室id来进行绘制列表的工作
        print("text in sort = " + text)
        self.current_widget.close()
        self.select_hot_widget_2.show()
        # 每个跳转都要有
        self.current_widget = self.select_hot_widget_2
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()

        if text == "综合排序":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 科室ID=%s'
            cursor.execute(sql,self.select_hot_widget_2.depa_id)
            db.close()
            self.select_hot_widget_2.results = cursor.fetchall()
            i = 0
            self.select_hot_widget_2.tableView.setRowCount(len(self.select_hot_widget_2.results))
            self.select_hot_widget_2.tableView.clearContents()
            while (i < len(self.select_hot_widget_2.results)):
                self.select_hot_widget_2.tableView.setRowHeight(i, 100)
                self.select_hot_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][0]))
                self.select_hot_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][1]))
                self.select_hot_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][2])))
                self.select_hot_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][3])))
                self.select_hot_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                         background-colo
                                                         self.retranslateUi()r : LightCoral;
                                                         height : 30px;
                                                         border-style: outset;
                                                         font : 13px; ''')
                self.select_hot_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "满意度排序":
            satisfactory = "满意度"
            res=[self.select_hot_widget_2.depa_id,satisfactory]
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 科室ID=%s order by %s DESC '
            cursor.execute(sql, res)
            db.close()
            # 查询出来的没有被排序
            self.select_hot_widget_2.results = cursor.fetchall()
            i = 0
            self.select_hot_widget_2.tableView.setRowCount(len(self.select_hot_widget_2.results))
            self.select_hot_widget_2.tableView.clearContents()
            while (i < len(self.select_hot_widget_2.results)):
                self.select_hot_widget_2.tableView.setRowHeight(i, 100)
                self.select_hot_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][0]))
                self.select_hot_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][1]))
                self.select_hot_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][2])))
                self.select_hot_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][3])))
                self.select_hot_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                     background-colo
                                                                     self.retranslateUi()r : LightCoral;
                                                                     height : 30px;
                                                                     border-style: outset;
                                                                     font : 13px; ''')
                self.select_hot_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "金州区":
            res = [text, self.select_hot_widget_2.depa_id]
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 地区地址=%s and 科室ID=%s'
            cursor.execute(sql, res)
            db.close()
            # 查询出来的没有被排序
            self.select_hot_widget_2.results = cursor.fetchall()
            i = 0
            self.select_hot_widget_2.tableView.setRowCount(len(self.select_hot_widget_2.results))
            self.select_hot_widget_2.tableView.clearContents()
            while (i < len(self.select_hot_widget_2.results)):
                self.select_hot_widget_2.tableView.setRowHeight(i, 100)
                self.select_hot_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][0]))
                self.select_hot_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][1]))
                self.select_hot_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][2])))
                self.select_hot_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][3])))
                self.select_hot_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                 background-colo
                                                                                 self.retranslateUi()r : LightCoral;
                                                                                 height : 30px;
                                                                                 border-style: outset;
                                                                                 font : 13px; ''')
                self.select_hot_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "中山区":
            res = [text, self.select_hot_widget_2.depa_id]
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 地区地址=%s and 科室ID=%s'
            cursor.execute(sql, res)
            db.close()
            # 查询出来的没有被排序
            self.select_hot_widget_2.results = cursor.fetchall()
            i = 0
            self.select_hot_widget_2.tableView.setRowCount(len(self.select_hot_widget_2.results))
            self.select_hot_widget_2.tableView.clearContents()
            while (i < len(self.select_hot_widget_2.results)):
                self.select_hot_widget_2.tableView.setRowHeight(i, 100)
                self.select_hot_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][0]))
                self.select_hot_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][1]))
                self.select_hot_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][2])))
                self.select_hot_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][3])))
                self.select_hot_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                             background-colo
                                                                                             self.retranslateUi()r : LightCoral;
                                                                                             height : 30px;
                                                                                             border-style: outset;
                                                                                             font : 13px; ''')
                self.select_hot_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "西岗区":
            res=[text,self.select_hot_widget_2.depa_id]
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 地区地址=%s and 科室ID=%s'
            cursor.execute(sql, res)
            db.close()
            # 查询出来的没有被排序
            self.select_hot_widget_2.results = cursor.fetchall()
            i = 0
            self.select_hot_widget_2.tableView.setRowCount(len(self.select_hot_widget_2.results))
            self.select_hot_widget_2.tableView.clearContents()
            while (i < len(self.select_hot_widget_2.results)):
                self.select_hot_widget_2.tableView.setRowHeight(i, 100)
                self.select_hot_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][0]))
                self.select_hot_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][1]))
                self.select_hot_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][2])))
                self.select_hot_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][3])))
                self.select_hot_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                             background-colo
                                                                                             self.retranslateUi()r : LightCoral;
                                                                                             height : 30px;
                                                                                             border-style: outset;
                                                                                             font : 13px; ''')
                self.select_hot_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))
                i = i + 1
        else:#说明这个时候是科室ID
            sender = self.sender()
            text = sender.objectName()
            print(text)
            self.select_hot_widget_2.depa_id=text#保存这个科室信息
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 科室ID=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_hot_widget_2.results = cursor.fetchall()
            i = 0
            self.select_hot_widget_2.tableView.setRowCount(len(self.select_hot_widget_2.results))
            self.select_hot_widget_2.tableView.clearContents()
            while (i < len(self.select_hot_widget_2.results)):
                self.select_hot_widget_2.tableView.setRowHeight(i, 100)
                self.select_hot_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][0]))
                self.select_hot_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_hot_widget_2.results[i][1]))
                self.select_hot_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][2])))
                self.select_hot_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][3])))
                self.select_hot_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_hot_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                                         background-colo
                                                                                                         self.retranslateUi()r : LightCoral;
                                                                                                         height : 30px;
                                                                                                         border-style: outset;
                                                                                                         font : 13px; ''')
                self.select_hot_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_hot_widget_2.results[self.select_hot_widget_2.tableView.currentRow()][5]))
                i = i + 1
    def sort_2(self,text):
        #重新绘制表格，一系列的if, else语句
        # k=self.select_all_widget_2.tableView.rowCount()
        # for j in range(k):
        #     self.select_all_widget_2.tableView.removeRow(j+1)
        print("text in sort22 = " + text)
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        if text == "综合排序":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院'
            cursor.execute(sql)
            db.close()
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0, QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1, QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                 background-colo
                                                 self.retranslateUi()r : LightCoral;
                                                 height : 30px;
                                                 border-style: outset;
                                                 font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "满意度排序":
            satisfactory="满意度"
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 order by %s DESC'
            cursor.execute(sql,satisfactory)
            db.close()
            #查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                             background-colo
                                                             self.retranslateUi()r : LightCoral;
                                                             height : 30px;
                                                             border-style: outset;
                                                             font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "金州区":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 地区地址=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                         background-colo
                                                                         self.retranslateUi()r : LightCoral;
                                                                         height : 30px;
                                                                         border-style: outset;
                                                                         font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "中山区":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 地区地址=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                     background-colo
                                                                                     self.retranslateUi()r : LightCoral;
                                                                                     height : 30px;
                                                                                     border-style: outset;
                                                                                     font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "西岗区":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 地区地址=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                     background-colo
                                                                                     self.retranslateUi()r : LightCoral;
                                                                                     height : 30px;
                                                                                     border-style: outset;
                                                                                     font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "内科":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 科室名=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                     background-colo
                                                                                     self.retranslateUi()r : LightCoral;
                                                                                     height : 30px;
                                                                                     border-style: outset;
                                                                                     font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "外科":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 科室名=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                     background-colo
                                                                                     self.retranslateUi()r : LightCoral;
                                                                                     height : 30px;
                                                                                     border-style: outset;
                                                                                     font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
        elif text == "儿科":
            sql = 'select 姓名,职称,科室名,医院名,满意度,医生ID from 医生 natural join 科室 natural join 医院 where 科室名=%s'
            cursor.execute(sql, text)
            db.close()
            # 查询出来的没有被排序
            self.select_all_widget_2.results = cursor.fetchall()
            i = 0
            self.select_all_widget_2.tableView.setRowCount(len(self.select_all_widget_2.results))
            self.select_all_widget_2.tableView.clearContents()
            while (i < len(self.select_all_widget_2.results)):
                self.select_all_widget_2.tableView.setRowHeight(i, 100)
                self.select_all_widget_2.tableView.setItem(i, 0,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][0]))
                self.select_all_widget_2.tableView.setItem(i, 1,
                                                           QTableWidgetItem(self.select_all_widget_2.results[i][1]))
                self.select_all_widget_2.tableView.setItem(i, 2, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][2])))
                self.select_all_widget_2.tableView.setItem(i, 3, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][3])))
                self.select_all_widget_2.tableView.setItem(i, 4, QTableWidgetItem(
                    str(self.select_all_widget_2.results[i][4])))
                button = QPushButton()
                button.setStyleSheet(''' text-align : center;
                                                                                     background-colo
                                                                                     self.retranslateUi()r : LightCoral;
                                                                                     height : 30px;
                                                                                     border-style: outset;
                                                                                     font : 13px; ''')
                self.select_all_widget_2.tableView.setCellWidget(i, 5, button)
                button.clicked.connect(lambda: self.show_sign_doctor(
                    self.select_all_widget_2.results[self.select_all_widget_2.tableView.currentRow()][5]))
                i = i + 1
    def show_first_page(self):
        self.current_widget.close()
        self.first_page_widget.show()
        # 每个跳转都要有
        self.current_widget = self.first_page_widget
    def show_second_page(self):
        self.current_widget.close()
        self.second_page_widget.show()
        #每个跳转都要有
        self.current_widget=self.second_page_widget
    def show_fifth_page(self):
        #如果没有私人医生就进入这个界面
        #有的话就直接进入医生选择界面
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        sql = 'select * from 病人私人医生 where 患者ID=%s'
        cursor.execute(sql, self.patient_ID)
        db.close()
        results = cursor.fetchall()
        print(results)
        if len(results)!=0:
            try:# do some thing you need
                print("尝试连接")
                self.com_widget = chattingWin(results[0][1], results[0][0])
                self.com_widget.show()
            except:
                # error: has not attribute
                QMessageBox.warning(self, "警告", "医生端不在线", QMessageBox.Cancel)
        else:
            self.current_widget.close()
            self.re_ui_scroll_of_selectHHP()
            self.fifth_page_widget.show()
            # 每个跳转都要有
            self.current_widget = self.fifth_page_widget
    def select_all_doctor(self):
        #点击“没有解决我的问题”就会进入这个函数
        #要展示所有的医生进来
        self.current_widget.close()
        self.select_all_widget_2.show()
        # 每个跳转都要有
        self.current_widget = self.select_all_widget_2
    # def select_relative_doctor(self,department_id):
    #     print(department_id)
    #     #根据传过来的科室id来进行绘制列表的工作
    #     self.current_widget.close()
    #
    #     self.select_hot_widget_2.show()
    #     # 每个跳转都要有
    #     self.current_widget = self.select_hot_widget_2
    def show_sign_doctor(self,id):#需要传过来一个医生ID才可以显示界面
        #print(id)
        self.doc_id=id
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql='select 姓名,医院名,职称,年纪,科室名,满意度 from 医生 natural join 科室 natural join 医院 where 医生ID=%s'
        cursor.execute(sql,id)
        result=cursor.fetchall()
        db.close()
        #print(result)
        #在这里设置基本信息，反正是从数据库读
        self.sign_doctor_widget.name_info_label.setText(result[0][0])
        self.sign_doctor_widget.hospital_info_label.setText(result[0][1])
        self.sign_doctor_widget.title_info_label.setText(result[0][2])
        self.sign_doctor_widget.age_info_label.setText(result[0][3])
        self.sign_doctor_widget.department_info_label.setText(result[0][4])
        self.sign_doctor_widget.satisfaction_info_label.setText(str(result[0][5]))
        self.current_widget.close()
        self.sign_doctor_widget.show()
        # 每个跳转都要有
        self.current_widget = self.sign_doctor_widget
    def show_pay_widget(self):
        self.current_widget.close()
        self.pay_widget.show()
        # 每个跳转都要有
        self.current_widget = self.pay_widget
    def show_new_patient(self):
        self.current_widget.close()
        self.new_patient_widget.show()
        # 每个跳转都要有
        self.current_widget = self.new_patient_widget
    def show_pro_sys(self,str_list):

        # 读取self.pro_sys_info，使用专家系统函数，诊断疾病
        result = pro_sys_result(self.pro_sys_info)
        res=[self.patient_ID,result]
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        cursor = db.cursor()
        sql = 'INSERT INTO 专家系统结果(患者ID, 专家系统诊断结果)VALUES (%s,%s)'
        cursor.execute(sql, res)
        db.commit()
        db.close()




        self.pro_sys_widget.descrip_textBrowser.setText(result)
        self.current_widget.close()
        self.pro_sys_widget.show()
        # 每个跳转都要有
        self.current_widget = self.pro_sys_widget
    def show_com(self):
        self.com_widget = chattingWin(self.doc_id,self.patient_ID)
        self.current_widget.close()
        self.com_widget.show()
        # 每个跳转都要有
        self.current_widget = self.first_page_widget#显示第一页
    def show_profile(self):
        #显示用户个人信息
        #self.first_page_widget.close()
        db = pymysql.connect("localhost", "root",
                             "12345", "hospital_management", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql='select*from 患者 where 患者ID=%s'
        cursor.execute(sql,self.patient_ID)
        results=cursor.fetchall()
        db.close()
        print(results)

        self.profile_widget.register_id_output.setText(results[0][0])
        self.profile_widget.register_name_output.setText(results[0][2])
        self.profile_widget.register_password_output.setText(results[0][1])
        self.profile_widget.register_idcard_output.setText(results[0][3])
        self.profile_widget.register_age_output.setText(str(results[0][4]))
        self.profile_widget.register_address_output.setText(results[0][5])



        self.current_widget.close()
        self.profile_widget.show()
        # 每个跳转都要有
        self.current_widget=self.profile_widget#设置当前显示widget
    #鼠标拖拽
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
    # 弹窗 显示字符串str
    def show_model_dialog(self,str):
        '''
        # 弹窗 显示字符串str
        :param str: str 想要显示的信息
        :return: None
        '''
    #重绘滚动条ui
    def re_ui_scroll_of_selectHHP(self):
        '''
        重绘滑动条部分ui
        :return: None
        '''
        self.widget_list = []
        with conn_mysql(dict_or_tuple = 1) as cursor:
            rows = cursor.execute("select * from 热点健康问题")
            result = cursor.fetchall()
            for i in range(rows):
                wgo = HHP_scrollarea_widget(parent=self.fifth_page_widget.scrollAreaWidgetContents,
                                            y=i*150,departmentID=result[i][1])
                wgo.pushButton.clicked.connect(lambda :self.sort("argv"))
                self.widget_list.append(wgo)

                self.widget_list[i].setTextBrowser(result[i][2])


        self.fifth_page_widget.scrollAreaWidgetContents.setMinimumSize(0, 150*len(self.widget_list))
    # 私人医生--新建病情调查页面，记录病人信息，为专家系统提供信息
    def record_pro_sys_info(self):
        #  身体全身
        if (self.new_patient_widget.checkBox00.checkState() == Qt.Checked):
            self.pro_sys_info[1] = "1"
        elif (self.new_patient_widget.checkBox00.checkState() == Qt.Unchecked):
            self.pro_sys_info[1] = "0"
        if (self.new_patient_widget.checkBox01.checkState() == Qt.Checked):
            self.pro_sys_info[2] = "1"
        elif (self.new_patient_widget.checkBox01.checkState() == Qt.Unchecked):
            self.pro_sys_info[2] = "0"
        if (self.new_patient_widget.checkBox02.checkState() == Qt.Checked):
            self.pro_sys_info[3] = "1"
        elif (self.new_patient_widget.checkBox02.checkState() == Qt.Unchecked):
            self.pro_sys_info[3] = "0"
        if (self.new_patient_widget.checkBox03.checkState() == Qt.Checked):
            self.pro_sys_info[4] = "1"
        elif (self.new_patient_widget.checkBox03.checkState() == Qt.Unchecked):
            self.pro_sys_info[4] = "0"
        # 头部
        if (self.new_patient_widget.checkBox10.checkState() == Qt.Checked):
            self.pro_sys_info[13] = "1"
        elif (self.new_patient_widget.checkBox10.checkState() == Qt.Unchecked):
            self.pro_sys_info[13] = "0"
        if (self.new_patient_widget.checkBox11.checkState() == Qt.Checked):
            self.pro_sys_info[14] = "1"
        elif (self.new_patient_widget.checkBox11.checkState() == Qt.Unchecked):
            self.pro_sys_info[14] = "0"
        if (self.new_patient_widget.checkBox12.checkState() == Qt.Checked):
            self.pro_sys_info[15] = "1"
        elif (self.new_patient_widget.checkBox12.checkState() == Qt.Unchecked):
            self.pro_sys_info[15] = "0"
        if (self.new_patient_widget.checkBox13.checkState() == Qt.Checked):
            self.pro_sys_info[16] = "1"
        elif (self.new_patient_widget.checkBox13.checkState() == Qt.Unchecked):
            self.pro_sys_info[16] = "0"
        # 颈部
        if (self.new_patient_widget.checkBox20.checkState() == Qt.Checked):
            self.pro_sys_info[25] = "1"
        elif (self.new_patient_widget.checkBox20.checkState() == Qt.Unchecked):
            self.pro_sys_info[25] = "0"
        if (self.new_patient_widget.checkBox21.checkState() == Qt.Checked):
            self.pro_sys_info[26] = "1"
        elif (self.new_patient_widget.checkBox21.checkState() == Qt.Unchecked):
            self.pro_sys_info[26] = "0"
        if (self.new_patient_widget.checkBox22.checkState() == Qt.Checked):
            self.pro_sys_info[27] = "1"
        elif (self.new_patient_widget.checkBox22.checkState() == Qt.Unchecked):
            self.pro_sys_info[27] = "0"
        # 胸部
        if (self.new_patient_widget.checkBox30.checkState() == Qt.Checked):
            self.pro_sys_info[37] = "1"
        elif (self.new_patient_widget.checkBox30.checkState() == Qt.Unchecked):
            self.pro_sys_info[37] = "0"
        if (self.new_patient_widget.checkBox31.checkState() == Qt.Checked):
            self.pro_sys_info[38] = "1"
        elif (self.new_patient_widget.checkBox31.checkState() == Qt.Unchecked):
            self.pro_sys_info[38] = "0"
        if (self.new_patient_widget.checkBox32.checkState() == Qt.Checked):
            self.pro_sys_info[39] = "1"
        elif (self.new_patient_widget.checkBox32.checkState() == Qt.Unchecked):
            self.pro_sys_info[39] = "0"

        # 腹部
        if (self.new_patient_widget.checkBox40.checkState() == Qt.Checked):
            self.pro_sys_info[49] = "1"
        elif (self.new_patient_widget.checkBox40.checkState() == Qt.Unchecked):
            self.pro_sys_info[49] = "0"
        if (self.new_patient_widget.checkBox41.checkState() == Qt.Checked):
            self.pro_sys_info[50] = "1"
        elif (self.new_patient_widget.checkBox41.checkState() == Qt.Unchecked):
            self.pro_sys_info[50] = "0"
        if (self.new_patient_widget.checkBox42.checkState() == Qt.Checked):
            self.pro_sys_info[51] = "1"
        elif (self.new_patient_widget.checkBox42.checkState() == Qt.Unchecked):
            self.pro_sys_info[51] = "0"
        if (self.new_patient_widget.checkBox43.checkState() == Qt.Checked):
            self.pro_sys_info[52] = "1"
        elif (self.new_patient_widget.checkBox43.checkState() == Qt.Unchecked):
            self.pro_sys_info[52] = "0"
        if (self.new_patient_widget.checkBox44.checkState() == Qt.Checked):
            self.pro_sys_info[53] = "1"
        elif (self.new_patient_widget.checkBox44.checkState() == Qt.Unchecked):
            self.pro_sys_info[53] = "0"
        if (self.new_patient_widget.checkBox45.checkState() == Qt.Checked):
            self.pro_sys_info[54] = "1"
        elif (self.new_patient_widget.checkBox45.checkState() == Qt.Unchecked):
            self.pro_sys_info[54] = "0"
        if (self.new_patient_widget.checkBox46.checkState() == Qt.Checked):
            self.pro_sys_info[55] = "1"
        elif (self.new_patient_widget.checkBox46.checkState() == Qt.Unchecked):
            self.pro_sys_info[55] = "0"
        if (self.new_patient_widget.checkBox47.checkState() == Qt.Checked):
            self.pro_sys_info[56] = "1"
        elif (self.new_patient_widget.checkBox47.checkState() == Qt.Unchecked):
            self.pro_sys_info[56] = "0"


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#
#
#
#     m=main()
#     sys.exit(app.exec_())

