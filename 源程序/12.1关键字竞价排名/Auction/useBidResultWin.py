import sys
from bidResultWin import Ui_BidResultWin
from PyQt5.QtWidgets import QApplication,QMainWindow
import pymysql

#这是结果类
class useBidResultWin(QMainWindow, Ui_BidResultWin):
	def __init__(self, parent = None):
		super(useBidResultWin,self).__init__(parent)
		self.setupUi(self)

































if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = useBidResultWin()
	ui.show()
	sys.exit(app.exec_())