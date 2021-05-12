# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from nanas import Ui_MainWindow
class Ui_Dialog(object):
    def openwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
        self.cur = self.db.cursor()

        username = self.email.text()
        password = self.password.text()

        sql = ''' SELECT * FROM user'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:

                self.window.show()
            else:
                print('this is a wrong')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 50, 121, 71))
        self.label.setStyleSheet("color:rgb(225, 225, 225); font-size:28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 101, 31))
        self.label_2.setStyleSheet("font-size:15pt; color:rgb(255, 0, 127)")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(170, 150, 241, 51))
        self.email.setStyleSheet("font-size:14pt; color:rgb(243, 243, 243)")
        self.email.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(170, 260, 241, 51))
        self.password.setStyleSheet("font-size:14pt; color:rgb(243, 243, 243)")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 111, 31))
        self.label_3.setStyleSheet("font-size:15pt; color:rgb(255, 0, 127)")
        self.label_3.setObjectName("label_3")
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(270, 390, 141, 41))
        self.loginbutton.setStyleSheet("background-color: rgb(167, 168, 167); font-size:14pt; color:rgb(255, 255, 255)")
        self.loginbutton.setObjectName("loginbutton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 350, 171, 16))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.createaccbutton = QtWidgets.QPushButton(Dialog)
        self.createaccbutton.setGeometry(QtCore.QRect(320, 340, 93, 28))
        self.createaccbutton.setStyleSheet("color:rgb(255, 255, 255)")
        self.createaccbutton.setObjectName("createaccbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.loginbutton.setText(_translate("Dialog", "Login"))
        self.loginbutton.clicked.connect(self.openwindow)
        self.label_4.setText(_translate("Dialog", "Don\'t have an account?"))
        self.createaccbutton.setText(_translate("Dialog", "Create Account"))











if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())