import sys
from mainWin import Ui_MainWindow
from useRegisterWin import useRegisterWin
from useBidWin import  useBidWin
from useBidResultWin import useBidResultWin
from PyQt5.QtWidgets import QApplication,QMainWindow
import pymysql

import flag



#这是使用主函数类
class useMainWin(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super(useMainWin,self).__init__(parent)
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = useMainWin()
	ui.show()
	sys.exit(app.exec_())