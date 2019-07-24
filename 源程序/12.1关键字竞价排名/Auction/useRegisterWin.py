import sys
from registerWin import Ui_RegisterWin
from PyQt5.QtWidgets import QApplication,QMainWindow

class useRegisterWin(QMainWindow, Ui_RegisterWin):
	def __init__(self, parent = None):
		super( useRegisterWin,self).__init__(parent)
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = useRegisterWin()
	ui.show()
	sys.exit(app.exec_())