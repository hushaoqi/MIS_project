from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
class my_record(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.setObjectName("medical_record_widget")
        self.tableView = QtWidgets.QTableWidget(self)
        self.tableView.setGeometry(QtCore.QRect(40, 70, 901, 561))
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(0)
        self.tableView.setRowCount(0)

