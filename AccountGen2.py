import json
from json import *
from PyQt5 import QtCore, QtGui, QtWidgets
import string
import random
import tkinter
from tkinter import messagebox
import requests
from user_agent import generate_user_agent
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 292)
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setTabletTracking(False)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 271, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setToolTipDuration(0)
        self.pushButton.setStyleSheet("color:rgb(255, 0, 0);background-color:rgb(0, 0, 0)rgb(255, 255, 255)")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 20, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 70, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 120, 181, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):


        def click():
            letters = string.ascii_lowercase
            li = 0
            self.textEdit.setText(( ''.join(random.choice(letters) for i in range(8))))
            self.textEdit_2.setText(( ''.join(random.choice(letters) for i in range(13))+"@gmail.com"))
            self.textEdit_3.setText("qwertqwert123")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("7snhacker", "AccountGen v0.2"))
        self.pushButton.setText(_translate("Form", "generate"))
        self.pushButton.clicked.connect(click)
        self.label.setText(_translate("Form", "username"))
        self.label_2.setText(_translate("Form", "email"))
        self.label_3.setText(_translate("Form", "password"))
        def registry():
            text = self.textEdit.toPlainText()
            text2 = self.textEdit_2.toPlainText()
            text3 = self.textEdit_3.toPlainText()
            #print(text,"\n",text2,"\n",text3)
            regurl = "https://www.instagram.com/accounts/web_create_ajax/"
            date = {
            'email': text2,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:qwertqwert123',
            'username': text,
            'first_name': 'AccountReg V0.1',
            'month': '6',
            'day': '4',
            'year': '1991',
            'client_id': 'YKO7zAALAAEHgitI_xa4QMENkQfn',
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': 'vKOxrL5D'
            }
            head = {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "es-ES,es;q=0.9,en;q=0.8",
            'content-length': "241",
            'origin': "https://www.instagram.com",
            'referer': "https://www.instagram.com/",
            'user-agent': f"{generate_user_agent()}",
            'x-csrftoken': "95RsiHDyX9J6AcVz9jtCIySbwf75QhvG",
            'x-instagram-ajax': "c7e210fa2eb7",
            'x-requested-with': "XMLHttpRequest",
            'Cache-Control': "no-cache"
            }
            response = requests.request("POST", regurl, data=date, headers=head)
            if ('"message": "checkpoint required"') in response:
                print(response.text)
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo("7snhacker",f"Done Registry \nusername:{text}\nemail:{text2}\npassword:{text3}")
            else:
                print(response.text)
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo("7snhacker", f"Registry Failed \nusername:{text}\nemail:{text2}\npassword:{text3}")


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(50, 240, 271, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setToolTipDuration(0)
        self.pushButton.setStyleSheet("color:rgb(255, 0, 0);background-color:rgb(0, 0, 0)rgb(255, 255, 255)")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton2")
        self.pushButton.setText("registry")
        self.pushButton.clicked.connect(registry)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 20, 181, 31))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("7snhacker","AccountGen V0.2 \nby @7snhacker")
    sys.exit(app.exec_())



