# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chating.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import time
import os
import struct

import threading
import datetime
import socket
import sys
from getip import get_host_ip


class Ui_chattingWin(QtWidgets.QWidget):
     
    def __init__(self):
        super().__init__()

        self.widget = QtWidgets.QWidget()

        self.newpatient_id = None


        
        #---------------------患者端---------------------#
        """
        sql = 'SELECT ip FROM DOCTOR\
                WHERE 医生ID = doctorID'
        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="electronicHealth")
        cursor = db.cursor()
        
        cursor.execute(sql)
        
        #self.ip_port = cursor.fetchall()[0][0]
        self.ip_port = ('127.0.0.1',9999)
        self.sk = socket.socket()
        
        self.sk.connect(self.ip_port)
        """



        #--------------------医生端---------------------#
 #       self.hostname=socket.gethostname()
  #      self.ipaddr=socket.gethostbyname(self.hostname)
        self.ip_port = (get_host_ip(),9999)
        
        self.sk = socket.socket()
        self.sk.bind(self.ip_port)
        self.sk.listen(10)
        
        #-----------------医生端/患者端--都要新建线程来接受socket的消息------------------#
        
        t= threading.Thread(target=self.waiting_msg)#创建线程
        t.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
        t.start()#开启线程




        self.initUI()
        
    def endChat(self):
        self.close()
#        
#        self.widget = gradingWin(self.doctorID)
#        
#        self.widget.show()
#        
#        self.close()
    
    
    
    def waiting_msg(self):
        
        #-------------------医生端----------------------------#
        
        
        while True:
            print ('server waiting...')
            self.conn,self.addr = self.sk.accept()

            while True:
                data = self.conn.recv(1024)
                #----------------在大的TextEdit里面显示----------------#
                #print(str(data,encoding='utf-8'))
                
                self.newpatient_id=data[0:9]
                
                
                cursor = self.textEdit_chat.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
        
                cursor.insertHtml(str(data,encoding='utf-8'))
                self.textEdit_chat.verticalScrollBar().setValue(self.textEdit_chat.verticalScrollBar().maximumHeight())
                
                
                
            self.conn.close()
        
        

        
        
        #------------------患者端-----------------------------#
        """
        while True:
            reply_msg = self.sk.recv(1024)
            #-------------------在打的TextEdit里面显示-----------------#
            cursor = self.textEdit_chat.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            Html = "<b>xxx医生</b>   <font color='blue'>%s</font><br><br><h6>%s<\h6><br><br>" %(datetime.datetime.now(),
                                                                                              str(reply_msg,encoding='utf-8'))
        
            cursor.insertHtml(Html)
        """
    #--------按 发送 Button 之后，读取输入框的内容并发送给另一端，同时显示在打的TextEdit中--------#
    def on_click_sendMess(self):
        send_mes = self.textEdit_input.document().toPlainText()
        #------------------患者端-----------------------------#
        """
        cursor = self.textEdit_chat.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        Html = "<b>用户%s</b>   <font color='blue'>%s</font><br><br><h6>%s<\h6><br><br>" %(self.ip_port,datetime.datetime.now(),send_mes)
        
        cursor.insertHtml(Html)
        self.textEdit_input.setText('')
        self.textEdit_input.setFocus(True)
        Html_to = "<b>xxx医生</b>   <font color='blue'>%s</font><br><br><h6>%s<\h6><br><br>" %(datetime.datetime.now(),send_mes)
        """
        #self.sk.sendall(bytes(send_mes,encoding='utf8'))
        #------------------医生端-----------------------------#
        
        cursor = self.textEdit_chat.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        Html = "<b>%s医生</b>   <font color='blue'>%s</font><br><br><h6>%s<\h6><br><br>" %("医生姓名",datetime.datetime.now(),send_mes)
        
        cursor.insertHtml(Html)
        self.textEdit_chat.verticalScrollBar().setValue(self.textEdit_chat.verticalScrollBar().maximumHeight())
        self.textEdit_input.setText('')
        self.textEdit_input.setFocus(True)
        
        self.conn.sendall(bytes(Html,encoding='utf8'))
    """
    def on_click_sendPic(self):
        fileinfo_size = struct.calcsize('128sl')
        buf = self.conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            fn = filename.strip('\00')
            new_filename = os.path.join('./', 'new_' + fn)
            print ('file new name is {0}, filesize if {1}'.format(new_filename,
                                                                 filesize))

            recvd_size = 0  # 定义已接收文件的大小
            fp = open(new_filename, 'wb')
            print ('start receiving...')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = self.conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = self.conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print ('end receive...')
    """
        
    
    
    def initUI(self):
        self.setObjectName("Chatting")
        self.resize(794, 575)
        #self.setWindowTitle("咨询聊天")
        
        
        self.textEdit_chat = QtWidgets.QTextEdit(self)
        self.textEdit_chat.setGeometry(QtCore.QRect(150, 10, 631, 411))
        self.textEdit_chat.setFocus(False)
        self.textEdit_chat.setObjectName("textEdit_chat")

        
        
        self.textEdit_input = QtWidgets.QTextEdit(self)
        self.textEdit_input.setGeometry(QtCore.QRect(150, 470, 631, 101))
        self.textEdit_input.setObjectName("textEdit_2")
        self.textEdit_input.setFocus(True)
        
        #self.pushButton_sendPic = QtWidgets.QPushButton(self)
        #self.pushButton_sendPic.setGeometry(QtCore.QRect(150, 430, 93, 28))
        #self.pushButton_sendPic.setObjectName("pushButton")
        #self.pushButton_sendPic.clicked.connect(self.on_click_sendPic)
        
        self.pushButton_send = QtWidgets.QPushButton(self)
        self.pushButton_send.setGeometry(QtCore.QRect(260, 430, 93, 28))
        self.pushButton_send.setObjectName("pushButton_2")
        self.pushButton_send.clicked.connect(self.on_click_sendMess)
        
        
        
        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 131, 531))
        self.groupBox.setObjectName("groupBox")
        
        self.label_docPic = QtWidgets.QLabel(self.groupBox)
        self.label_docPic.setGeometry(QtCore.QRect(10, 40, 101, 171))
        self.label_docPic.setObjectName("label")
        self.pic = QtGui.QPixmap('55012886_p0_master1200.jpg').scaled(self.label_docPic.rect().size())
        self.label_docPic.setPixmap(self.pic)
        

        
        self.label_docResume = QtWidgets.QLabel(self.groupBox)
        self.label_docResume.setGeometry(QtCore.QRect(20, 260, 81, 191))
        self.label_docResume.setObjectName("label_2")
        
        self.pushButton_endChat = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_endChat.setGeometry(QtCore.QRect(20, 490, 93, 28))
        self.pushButton_endChat.setObjectName("pushButton_3")
        self.pushButton_endChat.clicked.connect(self.endChat)
        
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_3")
        
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 410, 93, 28))
        self.pushButton_3.setObjectName("pushButton_4")
        
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 440, 93, 28))
        self.pushButton_4.setObjectName("pushButton_5")
        
        
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 470, 93, 28))
        self.pushButton_5.setObjectName("pushButton_6")
        
        
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
       # self.setWindowTitle(_translate("Chatting", self.doctorID))
        self.textEdit_input.setHtml(_translate("Chatting", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        #self.pushButton_sendPic.setText(_translate("Chatting", "发送图片"))
        self.pushButton_send.setText(_translate("Chatting", "发送"))
        self.groupBox.setTitle(_translate("Chatting", "医生信息"))
        #self.label_docPic.setText(_translate("Chatting", "pictures here"))
        #self.label_docPic.setPixmap(_translate("Chatting",self.png))
        self.label_docResume.setText(_translate("Chatting", "Resumes Here"))
        self.pushButton_endChat.setText(_translate("Chatting", "结束咨询"))
        self.pushButton_2.setText(_translate("Chatting","查看病历"))
        self.pushButton_3.setText(_translate("Chatting","开药"))
        self.pushButton_4.setText(_translate("Chatting","智能分析"))
        self.pushButton_5.setText(_translate("Chatting","治疗方案"))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ex = Ui_chattingWin()
    ex.show()
    sys.exit(app.exec_())





