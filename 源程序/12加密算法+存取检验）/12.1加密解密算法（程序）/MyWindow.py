from PyQt5 import QtWidgets
from encrypt import Ui_Form
from Tip import Ui_Tip
import re

class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def encrypt(self):
        Plaintext=self.textEdit.toPlainText()
        mis=self.textEdit_5.toPlainText()#偏移量

        #检查偏移量是否含有英文
        my_re = re.compile(r'[A-Za-z]', re.S)
        res = re.findall(my_re, mis)
        if len(res):
            QtWidgets.QMessageBox.warning(self, "error", "偏移量中含有字符",QtWidgets.QMessageBox.Cancel)
        else:
            Ciphertext = ""
            mis_direction=self.comboBox.currentText()
            if mis_direction=="向左偏移":
                for i in range(len(Plaintext)):
                    Ciphertext = Ciphertext + chr((ord(Plaintext[i]) - ord("a") - int(mis)
                                                   ) % 26 + ord("a"))
            else:
                for i in range(len(Plaintext)):
                    Ciphertext = Ciphertext + chr((ord(Plaintext[i]) - ord("a") + int(mis)) % 26 + ord("a"))

            self.textBrowser.setText(Ciphertext)

    def Tipshow(self):
        self.Tipwindow=Tip_Window()
        self.Tipwindow.show()


    def decrypt(self):
        Ciphertext=self.textEdit_2.toPlainText()
        mis = self.textEdit_6.toPlainText()

        my_re = re.compile(r'[A-Za-z]', re.S)
        res = re.findall(my_re, mis)
        if len(res):
            QtWidgets.QMessageBox.warning(self, "error", "偏移量中含有字符",QtWidgets.QMessageBox.Cancel)
        else:
            Plaintext = ""
            mis_direction = self.comboBox_2.currentText()
            if mis_direction == "向左偏移":
                for i in range(len(Ciphertext)):
                    Plaintext = Plaintext + chr((ord(Ciphertext[i]) - ord("a") - int(mis)) % 26 + ord("a"))
            else:
                for i in range(len(Ciphertext)):
                    Plaintext = Plaintext + chr((ord(Ciphertext[i]) - ord("a") + int(mis)) % 26 + ord("a"))
            self.textBrowser_2.setText(Plaintext)

class Tip_Window(QtWidgets.QMainWindow,Ui_Tip):
    def __init__(self):
        super(Tip_Window, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())