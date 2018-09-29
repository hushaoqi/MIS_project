#各个页面综合后放在这里
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
from profile_test import profile_widget
from first_page import first_page
from refistered import second_page_widget
from hot_healthy_probelem import fifth_page_widget
from select_from_all_2 import chosePMD_from_AP_widget_2
from sign_doctor import PMD_detail_widget
from pay import pay
from pay2 import pay_2
from new_patient import new_patient
from pro_sys import expert_sys_widget
from select_from_host_2 import chosePMD_from_HHP_widget_2
from my_record import my_record
# from python文件.mainWin import mainWin
# from python文件.privatePharmacy import privatePharmacy
# from python文件.reDiaMainWin import reDiaMainWin
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1350, 720)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 611))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.first_page_button = QtWidgets.QPushButton(self.layoutWidget)
        self.first_page_button.setMinimumSize(QtCore.QSize(0, 70))
        self.first_page_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.first_page_button.setObjectName("first_page_button")
        self.verticalLayout.addWidget(self.first_page_button)
        self.second_page_button = QtWidgets.QPushButton(self.layoutWidget)
        self.second_page_button.setMinimumSize(QtCore.QSize(0, 70))
        self.second_page_button.setObjectName("second_page_button")
        self.verticalLayout.addWidget(self.second_page_button)
        self.third_page_button = QtWidgets.QPushButton(self.layoutWidget)
        self.third_page_button.setMinimumSize(QtCore.QSize(0, 70))
        self.third_page_button.setObjectName("third_page_button")
        self.verticalLayout.addWidget(self.third_page_button)
        self.forth_page_button = QtWidgets.QPushButton(self.layoutWidget)
        self.forth_page_button.setMinimumSize(QtCore.QSize(0, 70))
        self.forth_page_button.setObjectName("forth_page_button")
        self.verticalLayout.addWidget(self.forth_page_button)
        self.fifth_page_button = QtWidgets.QPushButton(self.layoutWidget)
        self.fifth_page_button.setMinimumSize(QtCore.QSize(0, 70))
        self.fifth_page_button.setObjectName("fifth_page_button")
        self.verticalLayout.addWidget(self.fifth_page_button)
        self.sixth_page_button = QtWidgets.QPushButton(self.layoutWidget)
        self.sixth_page_button.setMinimumSize(QtCore.QSize(0, 70))
        self.sixth_page_button.setObjectName("sixth_page_button")
        self.verticalLayout.addWidget(self.sixth_page_button)
        self.left_menu_label = QtWidgets.QLabel(Form)
        self.left_menu_label.setGeometry(QtCore.QRect(-10, 30, 221, 691))
        self.left_menu_label.setObjectName("left_menu_label")
        self.gif = QMovie('source/载入动态图2.gif')




        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(230, 30, 20, 691))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.top_menu_label = QtWidgets.QLabel(Form)
        self.top_menu_label.setGeometry(QtCore.QRect(-10, 0, 1500, 31))
        self.top_menu_label.setObjectName("top_menu_label")

        self.top_menu_label.setMovie(self.gif)
        self.left_menu_label.setMovie(self.gif)
        self.gif.start()
        self.subtract_button = QtWidgets.QPushButton(Form)
        self.subtract_button.setGeometry(QtCore.QRect(1280, 0, 30, 30))
        self.subtract_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/subtract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subtract_button.setIcon(icon)
        self.subtract_button.setObjectName("subtract_button")
        self.close_button = QtWidgets.QPushButton(Form)
        self.close_button.setGeometry(QtCore.QRect(1320, 0, 30, 30))
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("source/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setObjectName("close_button")
        self.profile_button = QtWidgets.QPushButton(Form)
        self.profile_button.setGeometry(QtCore.QRect(1240, 0, 30, 30))
        self.profile_button.setToolTip("")
        self.profile_button.setWhatsThis("")
        self.profile_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("source/我的.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_button.setIcon(icon2)
        self.profile_button.setObjectName("profile_button")
        self.my_record_widget=my_record(Form)

        #第一页的widget，
        self.first_page_widget=first_page(Form)
        #profile的widget
        self.profile_widget=profile_widget(Form)
        #second
        self.second_page_widget=second_page_widget(Form)
        #third
        # self.third_page_widget=QtWidgets.QWidget(Form)
        # self.third_page_widget.setGeometry(QtCore.QRect(230, 30, 1081, 676))
        # self.win_question = mainWin(self.third_page_widget)
        #forth
        # self.forth_page_widget = QtWidgets.QWidget(Form)
        # self.forth_page_widget.setGeometry(QtCore.QRect(230, 30, 1081, 676))
        # self.win_reDiagnose = reDiaMainWin(self.forth_page_widget)
        #fifth
        self.fifth_page_widget=fifth_page_widget(Form)
        #sixth
        # self.sixth_page_widget = QtWidgets.QWidget(Form)
        # self.sixth_page_widget.setGeometry(QtCore.QRect(230, 30, 1081, 676))
        # self.win_privatePharmacy = privatePharmacy(self.sixth_page_widget)
        #self.select_hot_widget=chosePMD_from_HHP_widget(Form)
        self.select_hot_widget_2=chosePMD_from_HHP_widget_2(Form)
        #self.select_all_widget=chosePMD_from_AP_widget(Form)
        self.select_all_widget_2=chosePMD_from_AP_widget_2(Form)#----------------------
        self.sign_doctor_widget=PMD_detail_widget(Form)
        self.pay_widget=pay(Form)
        self.pay_widget_2=pay_2(Form)
        self.new_patient_widget=new_patient(Form)
        self.pro_sys_widget=expert_sys_widget(Form)
        # self.com_widget=conmunication_widget(Form)


        self.left_menu_label.raise_()
        self.layoutWidget.raise_()
        self.first_page_widget.raise_()
        self.line.raise_()
        self.top_menu_label.raise_()
        self.subtract_button.raise_()
        self.close_button.raise_()
        self.profile_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.first_page_button.setText(_translate("Form", "首页"))
        self.second_page_button.setText(_translate("Form", "挂号"))
        self.third_page_button.setText(_translate("Form", "咨询"))
        self.forth_page_button.setText(_translate("Form", "复诊"))
        self.fifth_page_button.setText(_translate("Form", "私人医生"))
        self.sixth_page_button.setText(_translate("Form", "在线药房"))
