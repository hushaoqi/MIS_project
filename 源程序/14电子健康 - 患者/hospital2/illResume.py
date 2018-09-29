# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'illResume.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

import pymysql as mc


class illResume(QtWidgets.QWidget):
    
    def __init__(self,patientID,Dialog):
        super().__init__()
        
        self.illDepiction = ""
        self.patientID = patientID      #患者ID
        
        self.initUI(Dialog)
    
    
        
        
    
    
    
    
    
    
    def drawQuestion(self,widgetArray):
        iterator = 0
        while iterator < len(widgetArray):
            widgetArray[iterator].setGeometry(QtCore.QRect(10, iterator*200, 500, 250))
            iterator += 1
    
    
    
    
    def initUI(self, Dialog):
        self.setObjectName("Form")
        
        self.resume = QtWidgets.QWidget(Dialog)
        self.resume.setGeometry(QtCore.QRect(210, 10, 831, 671))
        self.resume.setMinimumSize(831, 2600)
        
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidget(self.resume)
        
        
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)

        #self.scrollArea.setWidget(Dialog)
        #Dialog.setMinimumSize(QtCore.QRect(210, 10, 831, 671))
        self.scrollArea.setGeometry(QtCore.QRect(210, 10, 831, 671))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 829, 669))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setMinimumSize( 829, 2000)
        self.scrollBackGround = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.scrollBackGround.setGeometry(QtCore.QRect(0, 0, 829, 2000))
        self.scrollGIF = QtGui.QMovie("source/guo.gif")
        self.scrollBackGround.setMovie(self.scrollGIF)
        self.scrollGIF.start()
        
        self.questions = ['1. 有过家族病史吗？',
                          '2. 上次得艾滋病是什么时候？',
                          '3. 觉得自己心脏还在跳吗？',
                          '4. 有没有嗜睡反应？',
                          '5. 睡眠和食欲状况怎么样？',
                          '6. 觉得自己最近最反常举动是什么？',
                          '7. 最近容易生气吗？',
                          '8. 不舒服的部位的症状是什么样？',
                          '9. 以前得过什么大病吗？',
                          '10. 有没有做手术或注射过疫苗？']



        self.questionWidgets = []
        self.questionLabel = []
        self.answerEdit = []
        i = 0
        while i < 10:
            widgetTemp = QtWidgets.QWidget(self.scrollAreaWidgetContents)
            self.questionWidgets.append(widgetTemp)
            labelTemp = QtWidgets.QLabel(self.questionWidgets[i])
            self.questionLabel.append(labelTemp)
            self.questionLabel[i].setGeometry(QtCore.QRect(0, 0, 400, 30))
            self.questionLabel[i].setText(self.questions[i])
            textEditTemp = QtWidgets.QLineEdit(self.questionWidgets[i])
            self.answerEdit.append(textEditTemp)
            self.answerEdit[i].setGeometry(QtCore.QRect(0, 40, 400, 120))
            i += 1
        
        
        self.drawQuestion(self.questionWidgets)
        
        
        self.pushButton_inputCompleted = QtWidgets.QPushButton(Dialog)
        self.pushButton_inputCompleted.setGeometry(QtCore.QRect(10, 590, 181, 71))
        self.pushButton_inputCompleted.setObjectName("pushButton")
        #self.pushButton_inputCompleted.clicked.connect(self.on_click_submit)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 161, 221))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 280, 171, 281))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_inputCompleted.setText(_translate("Form", "提交"))
        self.label.setText(_translate("Form", "用户头像"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  请用户根据自身真实</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      情况填写</p></body></html>"))

