# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gradeWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql as mc
import sys

class gradingWin(QtWidgets.QWidget):
    
    def __init__(self,doctorID):
        super().__init__()
        
        self.doctorID = doctorID #--------------------对对应的医生进行打分------------------#
        self.grade = 70
        
        self.initUI()
    
    
    def pushButton1_turnBlue(self,QEvent):
        self.pushButton_2.setIcon(self.icon_cancelStar)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIcon(self.icon_cancelStar)
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIcon(self.icon_cancelStar)
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIcon(self.icon_cancelStar)
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_6.setIcon(self.icon_cancelStar)
        self.pushButton_6.setIconSize(self.pushButton_2.rect().size())
        
        
        self.pushButton_2.setIcon(self.icon)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        
        self.grade = 20
    def pushButton2_turnBlue(self,QEvent):
        self.pushButton_2.setIcon(self.icon_cancelStar)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIcon(self.icon_cancelStar)
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIcon(self.icon_cancelStar)
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIcon(self.icon_cancelStar)
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_6.setIcon(self.icon_cancelStar)
        self.pushButton_6.setIconSize(self.pushButton_2.rect().size())
        
        self.pushButton_2.setIcon(self.icon)
        self.pushButton_3.setIcon(self.icon)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        
        
        self.grade = 40
    def pushButton3_turnBlue(self,QEvent):
        self.pushButton_2.setIcon(self.icon_cancelStar)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIcon(self.icon_cancelStar)
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIcon(self.icon_cancelStar)
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIcon(self.icon_cancelStar)
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_6.setIcon(self.icon_cancelStar)
        self.pushButton_6.setIconSize(self.pushButton_2.rect().size())
        
        self.pushButton_2.setIcon(self.icon)
        self.pushButton_3.setIcon(self.icon)
        self.pushButton_4.setIcon(self.icon)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        
        self.grade = 60
    def pushButton4_turnBlue(self,QEvent):
        self.pushButton_2.setIcon(self.icon_cancelStar)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIcon(self.icon_cancelStar)
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIcon(self.icon_cancelStar)
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIcon(self.icon_cancelStar)
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_6.setIcon(self.icon_cancelStar)
        self.pushButton_6.setIconSize(self.pushButton_2.rect().size())
        
        self.pushButton_2.setIcon(self.icon)
        self.pushButton_3.setIcon(self.icon)
        self.pushButton_4.setIcon(self.icon)
        self.pushButton_5.setIcon(self.icon)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        
        self.grade = 80
    def pushButton5_turnBlue(self,QEvent):
        self.pushButton_2.setIcon(self.icon)
        self.pushButton_3.setIcon(self.icon)
        self.pushButton_4.setIcon(self.icon)
        self.pushButton_5.setIcon(self.icon)
        self.pushButton_6.setIcon(self.icon)
        
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_6.setIconSize(self.pushButton_2.rect().size())
        
        self.grade = 100
        
        
    def endGrading(self):
        """
        读取数据库       以1/100的权重将评分统计到数据库
        """
        sql = "SELECT 满意度 FROM 医生 WHERE 医生ID = '%s'" % self.doctorID   
        db = mc.connect(host="localhost", user="root", password="12345", database="hospital_management")
        cursor = db.cursor()
        
        cursor.execute(sql)
        
        curGrade = cursor.fetchall()[0][0]
        
        print(curGrade)
        
        curGrade = (100*curGrade + self.grade)/101.0
        
        print(curGrade)
        
        sql = "UPDATE 医生 SET 满意度=%s WHERE 医生ID = '%s'" % (str(curGrade),self.doctorID)
        
        cursor.execute(sql)
        db.commit()
        self.close()
    
        
        
    def initUI(self):
        self.setObjectName("Form")
        #Form.resize(400, 300)
        self.label_completeGrading = QtWidgets.QLabel(self)
        self.label_completeGrading.setGeometry(QtCore.QRect(50, 180, 93, 120))
        self.completeGrading_pix = QtGui.QPixmap("source/completeGrading.jpg").scaled(self.label_completeGrading.rect().size())
        self.label_completeGrading.setPixmap(self.completeGrading_pix)
        
        
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.endGrading)
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 61, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.enterEvent = self.pushButton1_turnBlue
        self.pixmap_heart = QtGui.QPixmap("source/Heart.jpg").scaled(self.pushButton_2.rect().size())
        self.cancel_stars = QtGui.QPixmap("source/cancelStars.jpg").scaled(self.pushButton_2.rect().size())
        self.icon = QtGui.QIcon(self.pixmap_heart)
        self.icon_cancelStar = QtGui.QIcon(self.cancel_stars)
        
        
        #self.pushButton_2.leaveEvent = self.pushButton1_turnWhite
        
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 100, 61, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.enterEvent = self.pushButton2_turnBlue
        #self.pushButton_3.leaveEvent = self.pushButton2_turnWhite
        
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 100, 61, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.enterEvent = self.pushButton3_turnBlue
        #self.pushButton_4.leaveEvent = self.pushButton3_turnWhite
        
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 100, 61, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.enterEvent = self.pushButton4_turnBlue
        #self.pushButton_5.leaveEvent = self.pushButton4_turnWhite
        
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 100, 61, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.enterEvent = self.pushButton5_turnBlue
        #self.pushButton_6.leaveEvent = self.pushButton5_turnWhite

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "评分界面"))
        self.pushButton.setText(_translate("Form", "完成评分"))
        self.pushButton_2.setIcon(self.icon_cancelStar)
        self.pushButton_2.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_3.setIcon(self.icon_cancelStar)
        self.pushButton_3.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_4.setIcon(self.icon_cancelStar)
        self.pushButton_4.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_5.setIcon(self.icon_cancelStar)
        self.pushButton_5.setIconSize(self.pushButton_2.rect().size())
        self.pushButton_6.setIcon(self.icon_cancelStar)
        self.pushButton_6.setIconSize(self.pushButton_2.rect().size())
#        self.pushButton_2.setText(_translate("Form", "1"))
#        self.pushButton_3.setText(_translate("Form", "2"))
#        self.pushButton_4.setText(_translate("Form", "3"))
#        self.pushButton_5.setText(_translate("Form", "4"))
#        self.pushButton_6.setText(_translate("Form", "5"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = gradingWin("3001")
    ex.show()
    sys.exit(app.exec_())



