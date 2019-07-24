from PyQt5 import QtWidgets
from login import Ui_Form
from login_success import Ui_Form_success
from login_failure import Ui_Form_failure

import table



class MyWindow(QtWidgets.QMainWindow, Ui_Form):


    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


    def login_definite(self):
        account=self.lineEdit.text()
        password=self.lineEdit_2.text()

        self.success_show = success_Window()
        self.failure_show = failure_Window()

        if account in table.user_account:
            index=table.user_account.index(account)#找到下标
            if table.user_password[index]==password:
                filename= self.comboBox.currentText()#获取下拉菜单的标注
                global account_
                account_= account
                global file_
                file_ = filename
                if filename=="文件A":
                    num=0
                elif filename=="文件B":
                    num=1
                elif filename=="文件C":
                    num=2
                elif filename=="文件D":
                    num=3
                elif filename=="文件E":
                    num=4
                elif filename=="文件F":
                    num=5

                if self.radioButton.isChecked()==True:#查找权限判断
                    if table.user_table[index][num]>=1:
                        global type_
                        type_ = "查询"
                        self.success_show.textBrowser.setText(account_)
                        self.success_show.textBrowser_2.setText(file_)
                        self.success_show.textBrowser_3.setText(type_)
                        self.success_show.show()
                    else:
                        self.failure_show.show()
                elif self.radioButton_2.isChecked()==True:#修改权限判断
                    if table.user_table[index][num]>=2:
                        type_ = "更新修改"
                        self.success_show.textBrowser.setText(account_)
                        self.success_show.textBrowser_2.setText(file_)
                        self.success_show.textBrowser_3.setText(type_)
                        self.success_show.show()
                    else:
                        self.failure_show.show()
            else:
                self.failure_show.show()
        else:
            self.failure_show.show()

class success_Window(QtWidgets.QMainWindow,Ui_Form_success):
    def __init__(self):
        super(success_Window, self).__init__()
        self.setupUi(self)



class failure_Window(QtWidgets.QMainWindow,Ui_Form_failure):
    def __init__(self):
        super(failure_Window, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())