# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(280, 20, 291, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(100, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_EngName = QtWidgets.QLabel(self.centralwidget)
        self.label_EngName.setGeometry(QtCore.QRect(83, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_EngName.setFont(font)
        self.label_EngName.setObjectName("label_EngName")
        self.label_country = QtWidgets.QLabel(self.centralwidget)
        self.label_country.setGeometry(QtCore.QRect(100, 120, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_country.setFont(font)
        self.label_country.setObjectName("label_country")
        self.label_sex = QtWidgets.QLabel(self.centralwidget)
        self.label_sex.setGeometry(QtCore.QRect(100, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sex.setFont(font)
        self.label_sex.setObjectName("label_sex")
        self.label_nation = QtWidgets.QLabel(self.centralwidget)
        self.label_nation.setGeometry(QtCore.QRect(100, 180, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nation.setFont(font)
        self.label_nation.setObjectName("label_nation")
        self.label_IDtype = QtWidgets.QLabel(self.centralwidget)
        self.label_IDtype.setGeometry(QtCore.QRect(67, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_IDtype.setFont(font)
        self.label_IDtype.setObjectName("label_IDtype")
        self.label_birthdata = QtWidgets.QLabel(self.centralwidget)
        self.label_birthdata.setGeometry(QtCore.QRect(70, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_birthdata.setFont(font)
        self.label_birthdata.setObjectName("label_birthdata")
        self.label_isAcademician = QtWidgets.QLabel(self.centralwidget)
        self.label_isAcademician.setGeometry(QtCore.QRect(70, 300, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_isAcademician.setFont(font)
        self.label_isAcademician.setObjectName("label_isAcademician")
        self.label_isDocent = QtWidgets.QLabel(self.centralwidget)
        self.label_isDocent.setGeometry(QtCore.QRect(70, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_isDocent.setFont(font)
        self.label_isDocent.setObjectName("label_isDocent")
        self.label_jobTitle = QtWidgets.QLabel(self.centralwidget)
        self.label_jobTitle.setGeometry(QtCore.QRect(103, 360, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_jobTitle.setFont(font)
        self.label_jobTitle.setObjectName("label_jobTitle")
        self.label_education = QtWidgets.QLabel(self.centralwidget)
        self.label_education.setGeometry(QtCore.QRect(70, 390, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_education.setFont(font)
        self.label_education.setObjectName("label_education")
        self.label_degree = QtWidgets.QLabel(self.centralwidget)
        self.label_degree.setGeometry(QtCore.QRect(70, 420, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_degree.setFont(font)
        self.label_degree.setObjectName("label_degree")
        self.label_SchoolTag = QtWidgets.QLabel(self.centralwidget)
        self.label_SchoolTag.setGeometry(QtCore.QRect(70, 450, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SchoolTag.setFont(font)
        self.label_SchoolTag.setObjectName("label_SchoolTag")
        self.label_GraduateYear = QtWidgets.QLabel(self.centralwidget)
        self.label_GraduateYear.setGeometry(QtCore.QRect(70, 500, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_GraduateYear.setFont(font)
        self.label_GraduateYear.setObjectName("label_GraduateYear")
        self.label_major = QtWidgets.QLabel(self.centralwidget)
        self.label_major.setGeometry(QtCore.QRect(70, 540, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_major.setFont(font)
        self.label_major.setObjectName("label_major")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(160, 60, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit_name.setMaxLength(30)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.editingFinished.connect(self.getname)
        self.lineEdit_EngName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_EngName.setGeometry(QtCore.QRect(160, 90, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_EngName.setFont(font)
        self.lineEdit_EngName.setStyleSheet("font: 12pt \"Arial\";")
        #设置验证器：最大长度为18个字符，只允许输入’a-z'和‘A-Z’以及空格
        Ereg = QRegExp("[a-zA-Z ]+$")
        EValidator = QRegExpValidator(self)
        EValidator.setRegExp(Ereg)
        self.lineEdit_EngName.setValidator(EValidator)
        self.lineEdit_EngName.setMaxLength(18)

        self.lineEdit_EngName.setObjectName("lineEdit_EngName")
        self.lineEdit_EngName.editingFinished.connect(self.getEngName)

        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(160, 240, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setStyleSheet("font: 12pt \"Arial\";")
        #设置验证器：最大长度为18个字符，只允许输入’0-9'和‘X’
        IDreg = QRegExp("[0-9X]+$")
        IDValidator = QRegExpValidator(self)
        IDValidator.setRegExp(IDreg)
        self.lineEdit_ID.setValidator(IDValidator)
        self.lineEdit_ID.setMaxLength(18)

        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_ID.editingFinished.connect(self.getID)

        self.lineEdit_birthdata = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_birthdata.setGeometry(QtCore.QRect(160, 270, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_birthdata.setFont(font)
        self.lineEdit_birthdata.setStyleSheet("font: 12pt \"Arial\";")
        #设置验证器：最大长度为7个字符，只允许输入’0-9'
        self.lineEdit_birthdata.setInputMask("0000-00")
        self.lineEdit_birthdata.setMaxLength(7)
        self.lineEdit_birthdata.setObjectName("lineEdit_birthdata")
        self.lineEdit_birthdata.editingFinished.connect(self.getbirth)
        self.lineEdit_GraduateYear = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_GraduateYear.setGeometry(QtCore.QRect(160, 500, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_GraduateYear.setFont(font)
        self.lineEdit_GraduateYear.setStyleSheet("font: 12pt \"Arial\";")
        #设置验证器：最大长度为4个字符，只允许输入’0-9'
        Greg = QRegExp("[0-9]+$")
        GValidator = QRegExpValidator(self)
        GValidator.setRegExp(Greg)
        self.lineEdit_GraduateYear.setValidator(GValidator)
        self.lineEdit_GraduateYear.setMaxLength(4)

        self.lineEdit_GraduateYear.setObjectName("lineEdit_GraduateYear")
        self.lineEdit_GraduateYear.editingFinished.connect(self.getgraduateYear)

        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(67, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ID.setFont(font)
        self.label_ID.setObjectName("label_ID")
        self.label_asteriskName = QtWidgets.QLabel(self.centralwidget)
        self.label_asteriskName.setGeometry(QtCore.QRect(315, 63, 21, 16))
        self.label_asteriskName.setScaledContents(False)
        self.label_asteriskName.setObjectName("label_asteriskName")
        self.comboBox_country = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_country.setGeometry(QtCore.QRect(160, 120, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_country.setFont(font)
        self.comboBox_country.setObjectName("comboBox_country")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_nation = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_nation.setGeometry(QtCore.QRect(160, 180, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_nation.setFont(font)
        self.comboBox_nation.setObjectName("comboBox_nation")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.setItemText(0, "**请选择**")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_nation.addItem("")
        self.comboBox_IDtype = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_IDtype.setGeometry(QtCore.QRect(160, 210, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_IDtype.setFont(font)
        self.comboBox_IDtype.setObjectName("comboBox_IDtype")
        self.comboBox_IDtype.addItem("")
        self.comboBox_IDtype.setItemText(0, "**请选择**")
        self.comboBox_IDtype.addItem("")
        self.comboBox_IDtype.addItem("")
        self.comboBox_IDtype.addItem("")
        self.comboBox_IDtype.addItem("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 150, 151, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_sex = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_sex.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_sex.setObjectName("horizontalLayout_sex")
        self.radioButton_man = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_man.setFont(font)
        self.radioButton_man.setChecked(True)
        self.radioButton_man.setObjectName("radioButton_man")
        self.horizontalLayout_sex.addWidget(self.radioButton_man)
        self.radioButton_woman = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.horizontalLayout_sex.addWidget(self.radioButton_woman)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(160, 330, 141, 24))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout__doctor = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout__doctor.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout__doctor.setObjectName("horizontalLayout__doctor")
        self.radioButton_Ydoc = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_Ydoc.setFont(font)
        self.radioButton_Ydoc.setObjectName("radioButton_Ydoc")
        self.horizontalLayout__doctor.addWidget(self.radioButton_Ydoc)
        self.radioButton_Ndoc = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_Ndoc.setFont(font)
        self.radioButton_Ndoc.setChecked(True)
        self.radioButton_Ndoc.setObjectName("radioButton_Ndoc")
        self.horizontalLayout__doctor.addWidget(self.radioButton_Ndoc)
        self.label_asteriskID = QtWidgets.QLabel(self.centralwidget)
        self.label_asteriskID.setGeometry(QtCore.QRect(382, 243, 21, 16))
        self.label_asteriskID.setScaledContents(False)
        self.label_asteriskID.setObjectName("label_asteriskID")
        self.label_asteriskIDtype = QtWidgets.QLabel(self.centralwidget)
        self.label_asteriskIDtype.setGeometry(QtCore.QRect(313, 214, 21, 16))
        self.label_asteriskIDtype.setScaledContents(False)
        self.label_asteriskIDtype.setObjectName("label_asteriskIDtype")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(160, 290, 449, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_Academician = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_Academician.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Academician.setObjectName("horizontalLayout_Academician")
        self.radioButton_AS = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_AS.setObjectName("radioButton_AS")
        self.horizontalLayout_Academician.addWidget(self.radioButton_AS)
        self.radioButton_S = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_S.setObjectName("radioButton_S")
        self.horizontalLayout_Academician.addWidget(self.radioButton_S)
        self.radioButton_E = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_E.setObjectName("radioButton_E")
        self.horizontalLayout_Academician.addWidget(self.radioButton_E)
        self.radioButton_N = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_N.setChecked(True)
        self.radioButton_N.setObjectName("radioButton_N")
        self.horizontalLayout_Academician.addWidget(self.radioButton_N)
        self.comboBox_jobTitle = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_jobTitle.setGeometry(QtCore.QRect(160, 360, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_jobTitle.setFont(font)
        self.comboBox_jobTitle.setObjectName("comboBox_jobTitle")
        self.comboBox_jobTitle.addItem("")
        self.comboBox_jobTitle.setItemText(0, "**请选择**")
        self.comboBox_jobTitle.addItem("")
        self.comboBox_jobTitle.addItem("")
        self.comboBox_jobTitle.addItem("")
        self.comboBox_jobTitle.addItem("")
        self.comboBox_education = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_education.setGeometry(QtCore.QRect(160, 390, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_education.setFont(font)
        self.comboBox_education.setObjectName("comboBox_education")
        self.comboBox_education.addItem("")
        self.comboBox_education.addItem("")
        self.comboBox_education.addItem("")
        self.comboBox_education.addItem("")
        self.comboBox_education.addItem("")
        self.comboBox_education.addItem("")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(160, 410, 261, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_degree = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_degree.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_degree.setObjectName("horizontalLayout_degree")
        self.radioButton_D = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_D.setObjectName("radioButton_D")
        self.horizontalLayout_degree.addWidget(self.radioButton_D)
        self.radioButton_G = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_G.setObjectName("radioButton_G")
        self.horizontalLayout_degree.addWidget(self.radioButton_G)
        self.radioButton_B = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_B.setObjectName("radioButton_B")
        self.horizontalLayout_degree.addWidget(self.radioButton_B)
        self.radioButton_O = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_O.setChecked(True)
        self.radioButton_O.setObjectName("radioButton_O")
        self.horizontalLayout_degree.addWidget(self.radioButton_O)
        self.textEdit_school = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_school.setGeometry(QtCore.QRect(160, 450, 381, 41))
        self.textEdit_school.setStyleSheet("font: 12pt \"Arial\";")
        self.textEdit_school.setObjectName("textEdit_school")


        self.textEdit_major = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_major.setGeometry(QtCore.QRect(160, 530, 381, 41))
        self.textEdit_major.setStyleSheet("font: 12pt \"Arial\";")
        self.textEdit_major.setObjectName("textEdit_major")

        self.label_asteriskMajor = QtWidgets.QLabel(self.centralwidget)
        self.label_asteriskMajor.setGeometry(QtCore.QRect(545, 536, 21, 31))
        self.label_asteriskMajor.setScaledContents(False)
        self.label_asteriskMajor.setObjectName("label_asteriskMajor")
        self.label_asteriskJobTitle = QtWidgets.QLabel(self.centralwidget)
        self.label_asteriskJobTitle.setGeometry(QtCore.QRect(313, 364, 21, 16))
        self.label_asteriskJobTitle.setScaledContents(False)
        self.label_asteriskJobTitle.setObjectName("label_asteriskJobTitle")
        self.label_Notice = QtWidgets.QLabel(self.centralwidget)
        self.label_Notice.setGeometry(QtCore.QRect(160, 580, 171, 31))
        self.label_Notice.setScaledContents(False)
        self.label_Notice.setObjectName("label_Notice")
        self.pushButton_showCode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_showCode.setGeometry(QtCore.QRect(50, 612, 81, 31))
        self.pushButton_showCode.setDefault(False)
        self.pushButton_showCode.setObjectName("pushButton_showCode")
        self.pushButton_showDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_showDB.setGeometry(QtCore.QRect(164, 612, 101, 31))
        self.pushButton_showDB.setObjectName("pushButton_showDB")
        self.pushButton_Help = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Help.setGeometry(QtCore.QRect(294, 612, 71, 31))
        self.pushButton_Help.setObjectName("pushButton_Help")
        self.pushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Save.setGeometry(QtCore.QRect(404, 612, 71, 31))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(514, 612, 81, 31))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.label_birthDataNotice = QtWidgets.QLabel(self.centralwidget)
        self.label_birthDataNotice.setGeometry(QtCore.QRect(340, 270, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.label_birthDataNotice.setFont(font)
        self.label_birthDataNotice.setObjectName("label_birthDataNotice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_showCode.clicked.connect(MainWindow.showCode)
        self.pushButton_showDB.clicked.connect(MainWindow.showDatabase)
        self.pushButton_Help.clicked.connect(MainWindow.showHelpPage)
        self.pushButton_Save.clicked.connect(MainWindow.checkAndSaveData)
        self.pushButton_Exit.clicked.connect(MainWindow.Exit)
        self.comboBox_country.activated[str].connect(MainWindow.getCountry)
        self.comboBox_nation.activated[str].connect(MainWindow.getNation)
        self.comboBox_IDtype.activated[str].connect(MainWindow.getIDtype)
        self.comboBox_jobTitle.activated[str].connect(MainWindow.getJobTitle)
        self.comboBox_education.activated[str].connect(MainWindow.getEducation)

        self.radioButton_man.toggled.connect(lambda :MainWindow.selectSex("男"))
        self.radioButton_woman.toggled.connect(lambda :MainWindow.selectSex("女"))

        self.radioButton_Ydoc.toggled.connect(lambda :MainWindow.selectDoc("是"))
        self.radioButton_Ndoc.toggled.connect(lambda :MainWindow.selectDoc("否"))

        self.radioButton_AS.toggled.connect(lambda :MainWindow.selectAS("两院院士"))
        self.radioButton_S.toggled.connect(lambda: MainWindow.selectAS("科学院院士"))
        self.radioButton_E.toggled.connect(lambda: MainWindow.selectAS("工程院院士"))
        self.radioButton_N.toggled.connect(lambda: MainWindow.selectAS("否"))

        self.radioButton_D.toggled.connect(lambda :MainWindow.selectDegree("博士"))
        self.radioButton_G.toggled.connect(lambda :MainWindow.selectDegree("硕士"))
        self.radioButton_B.toggled.connect(lambda :MainWindow.selectDegree("学士"))
        self.radioButton_O.toggled.connect(lambda :MainWindow.selectDegree("其他"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_name, self.lineEdit_EngName)
        MainWindow.setTabOrder(self.lineEdit_EngName, self.comboBox_country)
        MainWindow.setTabOrder(self.comboBox_country, self.radioButton_man)
        MainWindow.setTabOrder(self.radioButton_man, self.radioButton_woman)
        MainWindow.setTabOrder(self.radioButton_woman, self.comboBox_nation)
        MainWindow.setTabOrder(self.comboBox_nation, self.comboBox_IDtype)
        MainWindow.setTabOrder(self.comboBox_IDtype, self.lineEdit_ID)
        MainWindow.setTabOrder(self.lineEdit_ID, self.lineEdit_birthdata)
        MainWindow.setTabOrder(self.lineEdit_birthdata, self.radioButton_AS)
        MainWindow.setTabOrder(self.radioButton_AS, self.radioButton_S)
        MainWindow.setTabOrder(self.radioButton_S, self.radioButton_E)
        MainWindow.setTabOrder(self.radioButton_E, self.radioButton_N)
        MainWindow.setTabOrder(self.radioButton_N, self.radioButton_Ydoc)
        MainWindow.setTabOrder(self.radioButton_Ydoc, self.radioButton_Ndoc)
        MainWindow.setTabOrder(self.radioButton_Ndoc, self.comboBox_jobTitle)
        MainWindow.setTabOrder(self.comboBox_jobTitle, self.comboBox_education)
        MainWindow.setTabOrder(self.comboBox_education, self.radioButton_D)
        MainWindow.setTabOrder(self.radioButton_D, self.radioButton_G)
        MainWindow.setTabOrder(self.radioButton_G, self.radioButton_B)
        MainWindow.setTabOrder(self.radioButton_B, self.radioButton_O)
        MainWindow.setTabOrder(self.radioButton_O, self.textEdit_school)
        MainWindow.setTabOrder(self.textEdit_school, self.lineEdit_GraduateYear)
        MainWindow.setTabOrder(self.lineEdit_GraduateYear, self.textEdit_major)
        MainWindow.setTabOrder(self.textEdit_major, self.pushButton_showCode)
        MainWindow.setTabOrder(self.pushButton_showCode, self.pushButton_showDB)
        MainWindow.setTabOrder(self.pushButton_showDB, self.pushButton_Help)
        MainWindow.setTabOrder(self.pushButton_Help, self.pushButton_Save)
        MainWindow.setTabOrder(self.pushButton_Save, self.pushButton_Exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Title.setText(_translate("MainWindow", "专家个人信息维护"))
        self.label_name.setText(_translate("MainWindow", "姓名："))
        self.label_EngName.setText(_translate("MainWindow", "英文名："))
        self.label_country.setText(_translate("MainWindow", "国籍："))
        self.label_sex.setText(_translate("MainWindow", "性别："))
        self.label_nation.setText(_translate("MainWindow", "名族："))
        self.label_IDtype.setText(_translate("MainWindow", "证件类型："))
        self.label_birthdata.setText(_translate("MainWindow", "出生年月："))
        self.label_isAcademician.setText(_translate("MainWindow", "是否院士："))
        self.label_isDocent.setText(_translate("MainWindow", "是否博导："))
        self.label_jobTitle.setText(_translate("MainWindow", "职称："))
        self.label_education.setText(_translate("MainWindow", "最高学历："))
        self.label_degree.setText(_translate("MainWindow", "最高学位："))
        self.label_SchoolTag.setText(_translate("MainWindow", "毕业院校："))
        self.label_GraduateYear.setText(_translate("MainWindow", "毕业年份："))
        self.label_major.setText(_translate("MainWindow", "所学专业："))
        self.lineEdit_name.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">请输入中文字符</span></p></body></html>"))
        self.lineEdit_name.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "请输入中文字符"))
        self.lineEdit_EngName.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">请输入英文字符</span></p></body></html>"))
        self.lineEdit_EngName.setPlaceholderText(_translate("MainWindow", "请输入英文字符"))
        self.lineEdit_ID.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">请输入所选证件的证件号</span></p></body></html>"))
        self.lineEdit_ID.setPlaceholderText(_translate("MainWindow", "请输入18位证件号码"))
        self.lineEdit_birthdata.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">输入格式请参考示例</span></p></body></html>"))
        #self.lineEdit_birthdata.setPlaceholderText(_translate("MainWindow", "YYYYmm"))
        self.lineEdit_GraduateYear.setPlaceholderText(_translate("MainWindow", "YYYY"))
        self.label_ID.setText(_translate("MainWindow", "证件号码："))
        self.label_asteriskName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*</span></p></body></html>"))
        self.comboBox_country.setItemText(0, _translate("MainWindow", "**请选择**"))
        self.comboBox_country.setItemText(1, _translate("MainWindow", "中国"))
        self.comboBox_country.setItemText(2, _translate("MainWindow", "日本"))
        self.comboBox_country.setItemText(3, _translate("MainWindow", "英国"))
        self.comboBox_country.setItemText(4, _translate("MainWindow", "美国"))
        self.comboBox_nation.setItemText(1, _translate("MainWindow", "汉族"))
        self.comboBox_nation.setItemText(2, _translate("MainWindow", "满族"))
        self.comboBox_nation.setItemText(3, _translate("MainWindow", "回族"))
        self.comboBox_nation.setItemText(4, _translate("MainWindow", "壮族"))
        self.comboBox_nation.setItemText(5, _translate("MainWindow", "苗族"))
        self.comboBox_nation.setItemText(6, _translate("MainWindow", "维吾尔族"))
        self.comboBox_nation.setItemText(7, _translate("MainWindow", "土家族"))
        self.comboBox_nation.setItemText(8, _translate("MainWindow", "蒙古族"))
        self.comboBox_nation.setItemText(9, _translate("MainWindow", "藏族"))
        self.comboBox_nation.setItemText(10, _translate("MainWindow", "布依族"))
        self.comboBox_nation.setItemText(11, _translate("MainWindow", "朝鲜族"))
        self.comboBox_nation.setItemText(12, _translate("MainWindow", "侗族"))
        self.comboBox_nation.setItemText(13, _translate("MainWindow", "瑶族"))
        self.comboBox_IDtype.setItemText(1, _translate("MainWindow", "身份证"))
        self.comboBox_IDtype.setItemText(2, _translate("MainWindow", "护照"))
        self.comboBox_IDtype.setItemText(3, _translate("MainWindow", "军官证"))
        self.comboBox_IDtype.setItemText(4, _translate("MainWindow", "其他"))
        self.radioButton_man.setText(_translate("MainWindow", "男"))
        self.radioButton_woman.setText(_translate("MainWindow", "女"))
        self.radioButton_Ydoc.setText(_translate("MainWindow", "是"))
        self.radioButton_Ndoc.setText(_translate("MainWindow", "否"))
        self.label_asteriskID.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label_asteriskIDtype.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*</span></p></body></html>"))
        self.radioButton_AS.setText(_translate("MainWindow", "两院院士"))
        self.radioButton_S.setText(_translate("MainWindow", "科学院院士"))
        self.radioButton_E.setText(_translate("MainWindow", "工程院院士"))
        self.radioButton_N.setText(_translate("MainWindow", "否"))
        self.comboBox_jobTitle.setItemText(1, _translate("MainWindow", "正高级"))
        self.comboBox_jobTitle.setItemText(2, _translate("MainWindow", "副高级"))
        self.comboBox_jobTitle.setItemText(3, _translate("MainWindow", "中级"))
        self.comboBox_jobTitle.setItemText(4, _translate("MainWindow", "其他"))
        self.comboBox_education.setItemText(0, _translate("MainWindow", "**请选择**"))
        self.comboBox_education.setItemText(1, _translate("MainWindow", "研究生"))
        self.comboBox_education.setItemText(2, _translate("MainWindow", "本科"))
        self.comboBox_education.setItemText(3, _translate("MainWindow", "专科"))
        self.comboBox_education.setItemText(4, _translate("MainWindow", "高中"))
        self.comboBox_education.setItemText(5, _translate("MainWindow", "其他"))
        self.radioButton_D.setText(_translate("MainWindow", "博士"))
        self.radioButton_G.setText(_translate("MainWindow", "硕士"))
        self.radioButton_B.setText(_translate("MainWindow", "学士"))
        self.radioButton_O.setText(_translate("MainWindow", "其他"))
        self.textEdit_school.setPlaceholderText(_translate("MainWindow", "依次列出毕业院校"))
        self.textEdit_major.setPlaceholderText(_translate("MainWindow", "输入专业信息"))
        self.label_asteriskMajor.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label_asteriskJobTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">*</span></p></body></html>"))
        self.label_Notice.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">注：</span><span style=\" font-size:18pt; color:#ff0000; vertical-align:sub;\">*</span><span style=\" font-size:14pt; color:#000000;\">为必填项</span><span style=\" font-size:14pt; font-weight:400; color:#000000;\">!</span></p></body></html>"))
        self.pushButton_showCode.setText(_translate("MainWindow", "显示源码"))
        self.pushButton_showDB.setText(_translate("MainWindow", "显示数据库"))
        self.pushButton_Help.setText(_translate("MainWindow", "帮助"))
        self.pushButton_Save.setText(_translate("MainWindow", "保存"))
        self.pushButton_Exit.setText(_translate("MainWindow", "退出"))
        self.label_birthDataNotice.setText(_translate("MainWindow", "格式：yyyy-mm ; 示例：2018-08"))

