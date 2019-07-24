from PyQt5 import QtCore, QtGui, QtWidgets

#竞价界面
class Ui_bidWin(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(600, 350)
        mainwindow.setMinimumSize(QtCore.QSize(600, 350))
        mainwindow.setMaximumSize(QtCore.QSize(600, 350))
        mainwindow.setStyleSheet("QMainWindow #mainwindow{\n"
#"        background-color:#ffffff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setGeometry(QtCore.QRect(40, 0, 500, 50))
        self.frame_top.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_top.setMaximumSize(QtCore.QSize(500, 50))
        self.frame_top.setStyleSheet("#frame_top{\n"
#"        background:#fff;\n"
"        border-bottom:3px solid #a1a4ad;\n"
"}")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.keywords_title = QtWidgets.QLabel(self.frame_top)
        self.keywords_title.setGeometry(QtCore.QRect(0, 10, 300, 40))
        self.keywords_title.setMinimumSize(QtCore.QSize(300, 40))
        self.keywords_title.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.keywords_title.setFont(font)
        self.keywords_title.setStyleSheet(" #keywords_title{\n"
"        color:#000000;\n"
"}")
        self.keywords_title.setObjectName("keywords_title")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(100, 200, 115, 30))
        self.label3.setMinimumSize(QtCore.QSize(115, 30))
        self.label3.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setStyleSheet("QLabel{\n"
"        text-align:center;\n"
"}")
        self.label3.setObjectName("label3")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(200, 200, 35, 30))
        self.lineEdit2.setMinimumSize(QtCore.QSize(50, 30))
        self.lineEdit2.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setStyleSheet("#lineEdit2{\n"
"        border:1px solid #a1a4ad;\n"
"}\n"
"QLineEdit{\n"
"        padding-left:10px;\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(250, 190, 30, 50))
        self.label6.setMinimumSize(QtCore.QSize(30, 50))
        self.label6.setMaximumSize(QtCore.QSize(30, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(100, 150, 115, 30))
        self.label2.setMinimumSize(QtCore.QSize(115, 30))
        self.label2.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setStyleSheet("")
        self.label2.setObjectName("label2")
        self.lineEdit2_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2_2.setGeometry(QtCore.QRect(190, 150, 80, 30))
        self.lineEdit2_2.setMinimumSize(QtCore.QSize(80, 30))
        self.lineEdit2_2.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit2_2.setFont(font)
        self.lineEdit2_2.setStyleSheet("#lineEdit1{\n"
"        border:0px;\n"
"}\n"
"QLineEdit{\n"
"        padding-left:15px;\n"
"}\n"
"\n"
"#lineEdit2_2{\n"
"        border:0px;\n"
"}\n"
"")
        self.lineEdit2_2.setObjectName("lineEdit2_2")
        self.lineEdit2_2.setReadOnly(True)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 100, 115, 30))
        self.label1.setMinimumSize(QtCore.QSize(115, 30))
        self.label1.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setStyleSheet("")
        self.label1.setObjectName("label1")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(190, 100, 80, 30))
        self.lineEdit1.setMinimumSize(QtCore.QSize(80, 30))
        self.lineEdit1.setMaximumSize(QtCore.QSize(60, 30))

        #设置为只读模式
        self.lineEdit1.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setStyleSheet("#lineEdit1{\n"
"        border:0px;\n"
"}\n"
"QLineEdit{\n"
"        padding-left:15px;\n"
"}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(350, 120, 80, 80))
        self.pushButton1.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("#pushButton1{\n"
"        border:1px solid #000;\n"
"        border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background:#a1a4ad;\n"
"        color:white;\n"
"}\n"
"")
        self.pushButton1.setObjectName("pushButton1")

        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)


    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "关键字竞拍系统"))
        self.keywords_title.setText(_translate("mainwindow", "现场竞拍"))
        self.label3.setText(_translate("mainwindow", "加价幅度"))
        self.lineEdit2.setText(_translate("mainwindow", ""))
        self.label6.setText(_translate("mainwindow", "元"))
        self.label2.setText(_translate("mainwindow", "起拍价格"))
        self.lineEdit2_2.setText(_translate("mainwindow", "12"))
        self.label1.setText(_translate("mainwindow", "关键词"))
        self.lineEdit1.setText(_translate("mainwindow", "连衣"))
        self.pushButton1.setText(_translate("mainwindow", "竞价"))






