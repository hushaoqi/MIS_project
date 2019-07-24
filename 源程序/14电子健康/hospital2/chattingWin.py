# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chating.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gradingWin import gradingWin
import pymysql as mc

import threading

import datetime
import socket
import sys








class chattingWin(QtWidgets.QWidget):
    def __init__(self,doctorID,patientID):
        print("进入聊天")
        super().__init__()
        self.doctorID = doctorID
        self.patientID = patientID
        print(self.doctorID,self.patientID)
        self.widget = QtWidgets.QWidget()
        self.ip_port = []
        self.docName = []
        self.patName = []
        #---------------------患者端---------------------#

        sql = "SELECT IP地址,端口号,姓名 FROM 医生 WHERE 医生ID = '%s' "%self.doctorID
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
        cursor = db.cursor()
        
        cursor.execute(sql)
        self.doctor_res = cursor.fetchall()
        print("检索医生数据",self.doctor_res)

        self.ip_port.append(self.doctor_res[0][0])
        self.ip_port.append(self.doctor_res[0][1])
        self.docName.append(self.doctor_res[0][2])
        print("医生ip_port",self.ip_port)
        sql = "SELECT 姓名 FROM 患者 WHERE 患者ID = '%s' "%self.patientID
        cursor.execute(sql)

        self.patName.append(cursor.fetchall()[0])

        print(self.ip_port[0])
        self.sk = socket.socket()
        print(self.ip_port[1])
        self.sk.connect((self.ip_port[0], self.ip_port[1]))
        
        
        #--------------------医生端---------------------#
        """
        self.ip_port = ('10.6.94.3',9999)

        self.sk = socket.socket()
        self.sk.bind(self.ip_port)
        self.sk.listen(10)
        """
        #-----------------医生端/患者端--都要新建线程来接受socket的消息------------------#
        
        t= threading.Thread(target=self.waiting_msg)#创建线程
        t.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
        t.start()#开启线程
        
        
        
        
        self.initUI()
        
    def endChat(self):
        
        self.widget = gradingWin(self.doctorID)
        
        self.widget.show()
        
        self.close()
    """
    def on_click_sendPic(self):
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选择文件路径",  
                                    "H:/",  
                                    "All Files (*);;png Files (*.png);;jpg Files (*.jpg)")
        if os.path.isfile(fileName):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl', os.path.basename(fileName),
                                os.stat(bytes(fileName,encoding='utf8')).st_size)
            self.conn.send(fhead)
            print ('client fileName: {0}'.format(fileName))

            fp = open(fileName, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(fileName))
                    break
                self.sk.send(data)
    """
    def waiting_msg(self):
        
        #-------------------医生端----------------------------#
        """
        while True:
            print ('server waiting...')
            self.conn,self.addr = self.sk.accept()

            while True:
                data = conn.recv(1024)
                #----------------在大的TextEdit里面显示----------------#
                print(str(data,encoding='utf-8'))
        
            conn.close()
        """
        #------------------患者端-----------------------------#
        
        while True:
            reply_msg = self.sk.recv(1024)
            #-------------------在大的TextEdit里面显示-----------------#
            cursor = self.textEdit_chat.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
        
            cursor.insertHtml(str(reply_msg,encoding='utf-8'))
            self.textEdit_chat.verticalScrollBar().setValue(self.textEdit_chat.verticalScrollBar().maximumHeight())
    
    #--------按 发送 Button 之后，读取输入框的内容并发送给另一端，同时显示在打的TextEdit中--------#
    def on_click_sendMess(self):
        send_mes = self.textEdit_input.document().toPlainText()
        #------------------患者端-----------------------------#
        
        cursor = self.textEdit_chat.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        Html = "<b>%s:%s</b>   <font color='blue'>%s</font><br><br><h6>%s<\h6><br><br>" %(self.patientID,self.patName[0][0],datetime.datetime.now(),send_mes)
        
        cursor.insertHtml(Html)
        self.textEdit_chat.verticalScrollBar().setValue(self.textEdit_chat.verticalScrollBar().maximumHeight())
        self.textEdit_input.setText('')
        self.textEdit_input.setFocus(True)
        
        self.sk.sendall(bytes(Html,encoding='utf8'))
        #------------------医生端-----------------------------#
        """
        cursor = self.textEdit_chat.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        Html = "<b>xxx医生</b>   <font color='blue'>%s</font><br><br><h6>%s<\h6><br><br>" %(datetime.datetime.now(),send_mes)
        
        cursor.insertHtml(Html)
        self.textEdit_input.setText('')
        self.textEdit_input.setFocus(True)
        
        self.conn.sendall(bytes(Html_to,encoding='utf8'))
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
        self.pic = QtGui.QPixmap('source/55012886_p0_master1200.jpg').scaled(self.label_docPic.rect().size())
        self.label_docPic.setPixmap(self.pic)
        

        
        self.label_docResume = QtWidgets.QLabel(self.groupBox)
        self.label_docResume.setGeometry(QtCore.QRect(20, 260, 81, 191))
        self.label_docResume.setObjectName("label_2")
        
        self.pushButton_endChat = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_endChat.setGeometry(QtCore.QRect(20, 490, 93, 28))
        self.pushButton_endChat.setObjectName("pushButton_3")
        self.pushButton_endChat.clicked.connect(self.endChat)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Chatting", self.doctorID))
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ex = chattingWin()
    ex.show()
    sys.exit(app.exec_())





