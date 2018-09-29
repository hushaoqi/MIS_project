# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from selectDocWin import selectDocWin
from payingWin import payingWin
from chattingWin import chattingWin
from searchEssayWin import searchEssayWin
from seeMoreEssays import seeMoreEssays
from gradingWin import gradingWin
from illResume import illResume
import pymysql as mc
import time
from PyQt5.QtWidgets import *
class mainWin(QtWidgets.QWidget):
    
    def __init__(self,Dialog,patientID):
        super().__init__()


        self.patientID = patientID
        self.initUI(Dialog)
        self.widget = []

        self.widget.append(Dialog)

        
        
        
        
    #---------------------------------------------------------------#
    #                                                               #
    #              患者填写资料   点击按钮   开始选择医生             #
    #                                                               #
    #---------------------------------------------------------------#    
    def on_click_enterSelectDocWin(self):
        self.widget_illResume.hide()
        ##连接数据库，写入病情描述信息
        self.win_illResume.illDepiction = "家族病史：" +   self.win_illResume.answerEdit[0].text() +\
                            "  艾滋病："   +   self.win_illResume.answerEdit[1].text() +\
                            "  体感："     +   self.win_illResume.answerEdit[2].text() +\
                            "  手术经历："  +   self.win_illResume.answerEdit[3].text() +\
                            "  睡眠，饮食状况：" + self.win_illResume.answerEdit[4].text() +\
                            "  不正常举动："   + self.win_illResume.answerEdit[5].text() +\
                            "  部位症状："   + self.win_illResume.answerEdit[6].text() +\
                            "  大病病史："   + self.win_illResume.answerEdit[7].text() +\
                            "  情绪问题："   + self.win_illResume.answerEdit[8].text() +\
                            "  部位不舒服：" + self.win_illResume.answerEdit[9].text()

                            
#        sql = "INSERT INTO 病历 (患者ID, 存档时间, 主诉) VALUES ('%s','%s','%s')"%\
#                (self.win_illResume.patientID,time.strftime("%Y-%m-%d"),self.win_illResume.illDepiction)
#        print(sql)
#        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="hospital_management")
#        cursor = db.cursor()
#        
#        cursor.execute(sql)
#        
#        db.commit()
        
        
        
        
        self.widget_selectDocWin.show()
        
        
        
        
        
        
        
        
    #---------------------------------------------------------------#
    #                                                               #
    #              查找科普文章   点击列表项   查看文章               #
    #                                                               #
    #---------------------------------------------------------------#
    def on_click_seeMoreEssays(self):
        self.widget_searchEssayWin.hide()
        self.win_searchEssay.selectedEssayID = self.win_searchEssay.searchResult[0][self.win_searchEssay.listWidget.currentRow()][0]
        self.widget_seeMoreEssays = QtWidgets.QWidget(self.widget[0])
        self.widget_seeMoreEssays.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        #self.widget_seeMoreEssays.setObjectName("widget_seeMoreEssays")
        self.win_seeMoreEssays = seeMoreEssays(self.win_searchEssay.selectedEssayID,self.win_selectDoc.selectedDoc,self.widget_seeMoreEssays)                 #在当前页面显示想要查看的文章

        self.win_seeMoreEssays.pushButton_backToSearchEssay.clicked.connect(self.on_click_backToSearchEssay)
        self.widget_seeMoreEssays.show()


    #---------------------------------------------------------------#
    #                                                               #
    #      查看科普文章内容   点击列表项   返回上个界面               #
    #                                                               #
    #---------------------------------------------------------------#
    
    def on_click_backToSearchEssay(self):
        self.widget_seeMoreEssays.close()

        self.widget_searchEssayWin.show()

    
    


    
    #---------------------------------------------------------------#
    #                                                               #
    #              支付窗口   操作其他窗口的 按钮    响应函数         #
    #                                                               #
    #---------------------------------------------------------------#
    def on_click_payCompleted(self):#新建聊天窗口---------------------应该等聊天窗口关闭之后才能继续操作其他窗口
        self.setWindowTitle(self.win_paying.payingMethod)
        self.widget_payingWin.hide()
        self.widget_selectDocWin.show()
        try:  # do some thing you need
            self.widget = chattingWin(self.win_selectDoc.selectedDoc, self.patientID)
            # self.widget = chattingWin(self.win_selectDoc.selectedDoc,self.patientID)       #-------应该传医生ID进去（获取医生各种信息）
            # --------------插入病历-----------------------#
            sql = "INSERT INTO 病历 (患者ID, 存档时间, 主诉,医生ID) VALUES ('%s','%s','%s','%s')" % \
                  (self.patientID, time.strftime("%Y-%m-%d"), self.win_illResume.illDepiction,
                   self.win_selectDoc.selectedDoc)
            print(sql)
            db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
            cursor = db.cursor()

            cursor.execute(sql)

            db.commit()
            self.widget.show()
        except:
            # error: has not attribute
            QMessageBox.warning(self, "警告", "医生端不在线", QMessageBox.Cancel)

    
    
    def on_click_payCanceled(self):
        #----------------cancel data in the database-------------------------------
        #----------------close current window--------------------------------------
        self.widget_payingWin.hide()
        
        self.widget_selectDocWin.show()

    #---------------------------------------------------------------#
    #                                                               #
    #          选择医生窗口   操作其他窗口的 按钮    响应函数         #
    #                                                               #
    #---------------------------------------------------------------#
    
        
    def on_click_readEssay(self):
        #--------------New a Window-----------------------
        #--------------select all essays which are written by --selectedDoc--  -------------
        self.widget_selectDocWin.hide()
        
        self.win_searchEssay = searchEssayWin(self.widget_searchEssayWin,self.win_selectDoc.selectedDoc)
        self.win_searchEssay.pushButton_back.clicked.connect(self.on_click_backto_selectDocWin)
        self.win_searchEssay.listWidget.itemClicked.connect(self.on_click_seeMoreEssays)
        
        self.widget_searchEssayWin.show()
        """
        self.win_paying = payingWin(self.widget_payingWin,self.win_selectDoc.money)
        
        self.widget_payingWin.show()
        """
        
    def on_click_startChatting(self):
        #--------------New Paying Window------------------
        self.widget_selectDocWin.hide()
        
        self.win_paying = payingWin(self.widget_payingWin,self.win_selectDoc.money)
        self.win_paying.pushButton_payCanceled.clicked.connect(self.on_click_backto_selectDocWin)
        self.win_paying.pushButton_payCompleted.clicked.connect(self.on_click_payCompleted)
        #self.win_searchEssay = searchEssayWin(self.widget_searchEssayWin,self.win_selectDoc.doctor)
        self.widget_payingWin.show()
        #self.widget_searchEssayWin.show()


    #---------------------------------------------------------------#
    #                                                               #
    #          回到选择医生窗口   的 按钮  的  响应函数               #
    #                                                               #
    #---------------------------------------------------------------#        
    def on_click_grading(self,doctorID):
    #----------------new grading Window---------------------------
        self.widget = gradingWin(doctorID)    
        
        self.widget_searchEssayWin.hide()
        self.widget.show()
        
        
    def on_click_backto_selectDocWin(self):
        
        self.widget_payingWin.hide()
        
        self.widget_searchEssayWin.hide()
        
        self.widget_selectDocWin.show()
        
        
        
        
        
        
        
    def initUI(self,Dialog):
        self.setObjectName("Form")
        self.resize(1114, 715)
        
        self.widget_selectDocWin = QtWidgets.QWidget(Dialog)
        self.widget_selectDocWin.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_selectDocWin.setObjectName("widget_selecctDocWin")
        self.widget_selectDocWin.hide()
        self.selectDocPic = QtGui.QPixmap("source/19566230_p0.jpg").scaled(self.widget_selectDocWin.rect().size())
        print(123467)
        self.widget_selectDocWin_pic = QtWidgets.QLabel(self.widget_selectDocWin)
        self.widget_selectDocWin_pic.setGeometry(QtCore.QRect(0,0,1101,701))
        self.widget_selectDocWin_pic.setPixmap(self.selectDocPic)
        self.win_selectDoc = selectDocWin(self.widget_selectDocWin)
        self.win_selectDoc.readEssay.clicked.connect(self.on_click_readEssay)
        self.win_selectDoc.startChatting.clicked.connect(self.on_click_startChatting)
        
        
        self.widget_searchEssayWin = QtWidgets.QWidget(Dialog)
        self.widget_searchEssayWin.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_searchEssayWin.setObjectName("widget_searchEssayWin")
        self.widget_searchEssayWin.hide()
        
        
        
        
        self.widget_payingWin = QtWidgets.QWidget(Dialog)
        self.widget_payingWin_pic = QtWidgets.QLabel(self.widget_payingWin)
        self.widget_payingWin_pic.setGeometry(QtCore.QRect(0,0,1101,701))
        self.paying_pic = QtGui.QPixmap("source/web.jpg").scaled(self.widget_payingWin_pic.rect().size())
        self.widget_payingWin_pic.setPixmap(self.paying_pic)
        self.widget_payingWin.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_payingWin.setObjectName("widget_payingWin")
        self.widget_payingWin.hide()
        
        self.widget_seeMoreEssays = QtWidgets.QWidget(Dialog)
        self.widget_seeMoreEssays.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_seeMoreEssays.setObjectName("widget_seeMoreEssays")
        self.widget_seeMoreEssays.hide()


        self.widget_illResume = QtWidgets.QWidget(Dialog)
        self.widget_illResume.setGeometry(QtCore.QRect(10, 10, 1101, 701))
        self.widget_illResume.setObjectName("widget_illResume")
        self.win_illResume = illResume(self.patientID,self.widget_illResume)
        self.win_illResume.pushButton_inputCompleted.clicked.connect(self.on_click_enterSelectDocWin)
        self.widget_illResume.show()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self,Dilog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "电子健康"))


# app = QtWidgets.QApplication(sys.argv)
# mainWin_ex = mainWin()
# mainWin_ex.show()
# sys.exit(app.exec_())
    