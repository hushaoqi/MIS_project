import sys
from bidWin import Ui_bidWin
from PyQt5.QtWidgets import QApplication,QMainWindow
import  pymysql
from PyQt5.QtWidgets import *

#这是使用竞价类
class useBidWin(QMainWindow,Ui_bidWin):
	def __init__(self, parent = None):
		super( useBidWin,self).__init__(parent)
		self.setupUi(self)
		self.button_event()
		#self.add_Price()
		#self.showCompany()
		#self.showKeyWords()


	def showKeyWords(self):
		config = {
			'host': 'localhost',  # 数据库所在主机IP
			'port': 3306,  # MySQL默认端口
			'user': 'root',  # mysql默认用户名
			'password': '12345',
			'db': 'auctiondb',  # 数据库
			'charset': 'utf8mb4',
			'cursorclass': pymysql.cursors.DictCursor,
		}
		db = pymysql.connect(**config)
		#print("数据库连接成功！")
		cursor = db.cursor()
		#print("数据库指针寻找成功！")

		cursor.execute("SELECT * from keyinfo where flag=1")
		self.results = cursor.fetchall()
		# print(self.results)
		cursor.close()
		db.close()
		i = 0
		l = len(self.results)
		# print(l)
		i = 0
		while (i < l):
			keys_keywords = self.results[i]['keywords']
			keys_intialPri= self.results[i]['intialPri']
			i = i + 1
		#print(keys_keywords)
		#print(keys_intialPri)
		self.lineEdit1.setText(keys_keywords)
		self.lineEdit2_2.setText(str(keys_intialPri))


		#self.lineEdit1.setText(keys_keywords)
		#self.lineEdit2.setText(keys_intialPri)

	def showCompany(self):
		config = {
			'host': 'localhost',  # 数据库所在主机IP
			'port': 3306,  # MySQL默认端口
			'user': 'root',  # mysql默认用户名
			'password': '12345',
			'db': 'auctiondb',  # 数据库
			'charset': 'utf8mb4',
			'cursorclass': pymysql.cursors.DictCursor,
		}
		db = pymysql.connect(**config)
		# print("数据库连接成功！")
		cursor = db.cursor()
		# print("数据库指针寻找成功！")

		cursor.execute("SELECT * from company where flag=1")
		self.results = cursor.fetchall()
		# print(self.results)
		cursor.close()
		db.close()
		i = 0
		l = len(self.results)
		#print(l)
		i=0
		while(i<l):
			company_com=self.results[i]['company']
			company_weight=self.results[i]['weight']
			i=i+1
		#print(company_com)
		#print(company_weight)


	def button_event(self):
		self.pushButton1.clicked.connect(self.button_process)

	def button_process(self):
		addPrice=self.lineEdit2.text()
		#print(addPrice)
		if (self.lineEdit2.text() == ""):
			self.message1 = QMessageBox.information(self, "提示", "请输入加价幅度")

		elif(not(addPrice.isdigit())):
			self.message1 = QMessageBox.information(self, "提示", "输入不合法")
		else:

			config = {
				'host': 'localhost',  # 数据库所在主机IP
				'port': 3306,  # MySQL默认端口
				'user': 'root',  # mysql默认用户名
				'password': '12345',
				'db': 'auctiondb',  # 数据库
				'charset': 'utf8mb4',
				'cursorclass': pymysql.cursors.DictCursor,
			}
			db = pymysql.connect(**config)
			# print("数据库连接成功！")
			cursor = db.cursor()
			# print("数据库指针寻找成功！")

			cursor.execute("SELECT * from company where flag=1")
			self.results = cursor.fetchall()
			# print(self.results)
			cursor.close()
			db.close()
			i = 0
			l = len(self.results)
			# print(l)
			i = 0
			while (i < l):
				company_com = self.results[i]['company']
				company_weight = self.results[i]['weight']
				i = i + 1
			# print(company_com)
			# print(company_weight)



			t1=self.lineEdit1.text()
			t2=self.lineEdit2_2.text()
			t3=company_com
			t4=company_weight
			t5=addPrice


			# print(t1)
			# print(t2)
			# print(t3)
			# print(t4)
			# print(t5)
			config = {
				'host': 'localhost',  # 数据库所在主机IP
				'port': 3306,  # MySQL默认端口
				'user': 'root',  # mysql默认用户名
				'password': '12345',
				'db': 'auctiondb',  # 数据库
				'charset': 'utf8mb4',
				'cursorclass': pymysql.cursors.DictCursor,
			}
			db = pymysql.connect(**config)
			#print("数据库连接成功！")
			cursor = db.cursor()
			#print("数据库指针寻找成功！")

			sql = ("select * from auctiont where company = '%s' and keywords = '%s'")%(t3,t1)
			cursor.execute(sql)
			self.results = cursor.fetchall()
			d = float(t2) + float(t5)
			if(len(self.results) != 0):
				#print('更新')
				sql = ("update auctiont set auctionPri = '%f',weightPri = '%f' where company = '%s' and keywords = '%s'")%(d,float(t4) * d,t3,t1)
			else:
				# print(d)
				sql = ("insert into auctiont values('%s','%s',%f,%f)") % (t3, t1, d, float(t4) * d)
			cursor.execute(sql)
			db.commit()
			#print('提交')
			cursor.close()
			db.cursor()
			self.message1 = QMessageBox.information(self, "提示", "恭喜您，竞价成功")
			self.lineEdit2.setText("")





if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = useBidWin()
	ui.show()
	sys.exit(app.exec_())