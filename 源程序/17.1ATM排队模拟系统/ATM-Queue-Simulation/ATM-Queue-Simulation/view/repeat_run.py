# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repeat_run.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RepeatRun(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_RepeatRun, self).__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1540, 578)
        self.tableWidget_avg_wait = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_avg_wait.setGeometry(QtCore.QRect(220, 30, 301, 301))
        self.tableWidget_avg_wait.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_avg_wait.setMidLineWidth(0)
        self.tableWidget_avg_wait.setAlternatingRowColors(True)
        self.tableWidget_avg_wait.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_avg_wait.setObjectName("tableWidget_avg_wait")
        self.tableWidget_avg_wait.setColumnCount(2)
        self.tableWidget_avg_wait.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_avg_wait.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_avg_wait.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_avg_wait.setHorizontalHeaderItem(1, item)
        self.tableWidget_avg_wait.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_avg_wait.horizontalHeader().setSortIndicatorShown(False)
        self.label_repeat_time = QtWidgets.QLabel(Dialog)
        self.label_repeat_time.setGeometry(QtCore.QRect(570, 20, 71, 41))
        self.label_repeat_time.setObjectName("label_repeat_time")
        self.Repetitions = QtWidgets.QLineEdit(Dialog)
        self.Repetitions.setGeometry(QtCore.QRect(672, 30, 101, 21))
        self.Repetitions.setObjectName("Repetitions")
        self.Verify = QtWidgets.QPushButton(Dialog)
        self.Verify.setGeometry(QtCore.QRect(810, 30, 51, 21))
        self.Verify.setObjectName("Verify")
        self.label_lab_data = QtWidgets.QLabel(Dialog)
        self.label_lab_data.setGeometry(QtCore.QRect(580, 90, 72, 15))
        self.label_lab_data.setObjectName("label_lab_data")
        self.NumOfData = QtWidgets.QLineEdit(Dialog)
        self.NumOfData.setEnabled(False)
        self.NumOfData.setGeometry(QtCore.QRect(580, 110, 51, 21))
        self.NumOfData.setReadOnly(True)
        self.NumOfData.setObjectName("NumOfData")
        self.label_avg = QtWidgets.QLabel(Dialog)
        self.label_avg.setGeometry(QtCore.QRect(640, 110, 101, 16))
        self.label_avg.setObjectName("label_avg")
        self.label_min = QtWidgets.QLabel(Dialog)
        self.label_min.setGeometry(QtCore.QRect(680, 150, 72, 15))
        self.label_min.setObjectName("label_min")
        self.label_max = QtWidgets.QLabel(Dialog)
        self.label_max.setGeometry(QtCore.QRect(680, 190, 72, 15))
        self.label_max.setObjectName("label_max")
        self.AverageDate = QtWidgets.QLineEdit(Dialog)
        self.AverageDate.setEnabled(False)
        self.AverageDate.setGeometry(QtCore.QRect(750, 110, 71, 21))
        self.AverageDate.setReadOnly(True)
        self.AverageDate.setObjectName("AverageDate")
        self.MinData = QtWidgets.QLineEdit(Dialog)
        self.MinData.setEnabled(False)
        self.MinData.setGeometry(QtCore.QRect(750, 150, 71, 21))
        self.MinData.setReadOnly(True)
        self.MinData.setObjectName("MinData")
        self.MaxData = QtWidgets.QLineEdit(Dialog)
        self.MaxData.setEnabled(False)
        self.MaxData.setGeometry(QtCore.QRect(750, 190, 71, 21))
        self.MaxData.setReadOnly(True)
        self.MaxData.setObjectName("MaxData")
        self.Reset = QtWidgets.QPushButton(Dialog)
        self.Reset.setGeometry(QtCore.QRect(590, 300, 61, 31))
        self.Reset.setObjectName("Reset")
        self.Finish = QtWidgets.QPushButton(Dialog)
        self.Finish.setGeometry(QtCore.QRect(700, 300, 61, 31))
        self.Finish.setObjectName("Finish")
        self.Help = QtWidgets.QPushButton(Dialog)
        self.Help.setGeometry(QtCore.QRect(810, 300, 61, 31))
        self.Help.setObjectName("Help")
        self.label_last_result = QtWidgets.QLabel(Dialog)
        self.label_last_result.setGeometry(QtCore.QRect(40, 330, 131, 16))
        self.label_last_result.setObjectName("label_last_result")
        self.tableWidget_last_result = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_last_result.setGeometry(QtCore.QRect(30, 350, 1131, 192))
        self.tableWidget_last_result.setObjectName("tableWidget_last_result")
        self.tableWidget_last_result.setColumnCount(9)
        self.tableWidget_last_result.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.tableWidget_last_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_last_result.setHorizontalHeaderItem(8, item)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(560, 100, 20, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(570, 90, 16, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(570, 210, 321, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(640, 70, 251, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(880, 100, 20, 131))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "重复实验"))
        item = self.tableWidget_avg_wait.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "*"))
        item = self.tableWidget_avg_wait.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "实验编号"))
        item = self.tableWidget_avg_wait.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "平均排队时间"))
        self.label_repeat_time.setText(_translate("Dialog", "重复次数："))
        self.Verify.setText(_translate("Dialog", "确定"))
        self.label_lab_data.setText(_translate("Dialog", "实验数据"))
        self.label_avg.setText(_translate("Dialog", "次实验平均值："))
        self.label_min.setText(_translate("Dialog", "最小值："))
        self.label_max.setText(_translate("Dialog", "最大值："))
        self.Reset.setText(_translate("Dialog", "重置"))
        self.Finish.setText(_translate("Dialog", "完成"))
        self.Help.setText(_translate("Dialog", "帮助"))
        self.label_last_result.setText(_translate("Dialog", "最后一次试验结果："))
        item = self.tableWidget_last_result.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "*"))
        item = self.tableWidget_last_result.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "客户编号"))
        item = self.tableWidget_last_result.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "间隔时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "到达时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "服务时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "服务开始时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "等待时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "服务结束时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "客户在系统花费时间"))
        item = self.tableWidget_last_result.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "空闲时间"))
