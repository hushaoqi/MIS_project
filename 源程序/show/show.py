#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
from main import Ui_MainWindow
from child import Ui_Child
import sys
 
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
 
class Child(QMainWindow,Ui_Child):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
 
if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = Main()
    ch = Child()
    main.show()
    main.pushButton.clicked.connect(ch.OPEN)
    main.pushButton.clicked.connect(main.close)
    sys.exit(app.exec_())