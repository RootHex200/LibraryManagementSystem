from xlrd import *
from xlsxwriter import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import sys

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(80, 10, 861, 501))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(360, 30, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(570, 30, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(694, 30, 141, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 851, 361))
        self.tableWidget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)


        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 30, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(530, 30, 47, 21))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 861, 471))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(622, 90, 171, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(632, 320, 161, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 170, 291, 181))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(630, 150, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(630, 210, 161, 22))
        self.comboBox_4.setObjectName("comboBox_4")


        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 370, 75, 31))
        self.pushButton_7.setObjectName("pushButton_7")


        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(530, 90, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(530, 160, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(530, 210, 91, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(530, 320, 91, 31))
        self.label_7.setObjectName("label_7")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_5.setGeometry(QtCore.QRect(630, 270, 161, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(530, 270, 91, 21))
        self.label_8.setObjectName("label_8")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(60, 50, 91, 31))
        self.label_15.setObjectName("label_15")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 50, 181, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(60, 120, 91, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 120, 181, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(50, 180, 291, 181))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(520, 90, 91, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(610, 90, 171, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(520, 150, 91, 21))
        self.label_18.setObjectName("label_18")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_9.setGeometry(QtCore.QRect(620, 150, 161, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(620, 210, 161, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(620, 270, 161, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(610, 330, 171, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(520, 210, 91, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(520, 270, 91, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(520, 330, 91, 31))
        self.label_21.setObjectName("label_21")

        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 50, 101, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 390, 101, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(530, 390, 101, 31))
        self.pushButton_11.setObjectName("pushButton_11")

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 401, 421))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(170, 70, 191, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_13.setGeometry(QtCore.QRect(170, 140, 191, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_14.setGeometry(QtCore.QRect(170, 210, 191, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setGeometry(QtCore.QRect(170, 280, 191, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(60, 75, 111, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(60, 150, 111, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(60, 215, 111, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(60, 284, 111, 34))
        self.label_25.setObjectName("label_25")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(140, 360, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 30, 401, 421))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(170, 160, 191, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(170, 220, 191, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(170, 280, 191, 31))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(170, 340, 191, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(50, 160, 111, 31))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(50, 230, 111, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(50, 290, 111, 21))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(40, 340, 121, 31))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(40, 30, 111, 31))
        self.label_30.setObjectName("label_30")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(160, 30, 191, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(40, 75, 111, 21))
        self.label_31.setObjectName("label_31")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(160, 70, 191, 31))
        self.lineEdit_21.setObjectName("lineEdit_21")

        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 110, 75, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(134, 380, 141, 31))
        self.pushButton_14.setObjectName("pushButton_14")

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_8)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 861, 471))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 150, 851, 271))
        self.tableWidget_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_22.setGeometry(QtCore.QRect(190, 70, 221, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")

        self.pushButton_15 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_15.setGeometry(QtCore.QRect(530, 70, 161, 31))
        self.pushButton_15.setObjectName("pushButton_15")

        self.label_32 = QtWidgets.QLabel(self.tab_9)
        self.label_32.setGeometry(QtCore.QRect(30, 75, 151, 21))
        self.label_32.setObjectName("label_32")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_11)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 150, 851, 271))
        self.tableWidget_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.label_33 = QtWidgets.QLabel(self.tab_11)
        self.label_33.setGeometry(QtCore.QRect(60, 50, 151, 31))
        self.label_33.setObjectName("label_33")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_23.setGeometry(QtCore.QRect(240, 50, 221, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_16.setGeometry(QtCore.QRect(600, 50, 161, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_10)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 150, 851, 271))
        self.tableWidget_4.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.label_34 = QtWidgets.QLabel(self.tab_10)
        self.label_34.setGeometry(QtCore.QRect(80, 60, 161, 31))
        self.label_34.setObjectName("label_34")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_24.setGeometry(QtCore.QRect(240, 60, 221, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_17.setGeometry(QtCore.QRect(580, 60, 161, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_3.setGeometry(QtCore.QRect(150, 30, 571, 411))
        self.groupBox_3.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_18.setGeometry(QtCore.QRect(90, 110, 141, 121))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_19.setGeometry(QtCore.QRect(370, 100, 141, 121))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_20.setGeometry(QtCore.QRect(90, 280, 141, 121))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_21.setGeometry(QtCore.QRect(370, 280, 141, 121))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(80, 55, 151, 21))
        self.label_35.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.tabWidget.addTab(self.tab_12, "")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 50, 75, 71))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/today.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 130, 75, 71))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/books.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 210, 75, 71))
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/users.png);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 290, 75, 71))
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/settings.png);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 370, 75, 71))
        self.pushButton_5.setStyleSheet("border-image: url(:/newPrefix/settings.png);\n"
"border-image: url(:/newPrefix/themes.png);")
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_category()
        self.show_author()
        self.show_publisher()
        self.add_category_comobox()
        self.edit_category_comobox()
        self.author_comobox()
        self.edit_author_comobox()
        self.publisher_comobox()
        self.edit_publisher_comobox()
        self.show_all_data_ui()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Book Title name"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Retrieve"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Rent"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "10"))
        self.pushButton_6.setText(_translate("MainWindow", "Export Excel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book Category"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Book Author"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Book Publisher"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Book Description"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Book Price"))
        self.label.setText(_translate("MainWindow", "Type"))
        self.label_2.setText(_translate("MainWindow", "Day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))

        self.pushButton_7.setText(_translate("MainWindow", "Save"))
        self.pushButton_7.clicked.connect(self.add_newbook)

        self.label_3.setText(_translate("MainWindow", "Book Title"))
        self.label_4.setText(_translate("MainWindow", "Book Code"))
        self.label_5.setText(_translate("MainWindow", "Category"))

        self.label_6.setText(_translate("MainWindow", "Author"))
        self.label_7.setText(_translate("MainWindow", "Book Price"))
        self.label_8.setText(_translate("MainWindow", "Publisher"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Add New Book"))
        self.label_15.setText(_translate("MainWindow", "Book Title"))
        self.label_16.setText(_translate("MainWindow", "Book Title"))
        self.label_17.setText(_translate("MainWindow", "Book Code"))
        self.label_18.setText(_translate("MainWindow", "Category"))
        self.label_19.setText(_translate("MainWindow", "Author"))
        self.label_20.setText(_translate("MainWindow", "Publisher"))
        self.label_21.setText(_translate("MainWindow", "Book Price"))

        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.pushButton_9.clicked.connect(self.search_book)

        self.pushButton_10.setText(_translate("MainWindow", "Delete"))
        self.pushButton_10.clicked.connect(self.delete_book)
        self.pushButton_11.setText(_translate("MainWindow", "Save"))
        self.pushButton_11.clicked.connect(self.edit_book)

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Edit or Delete a Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.groupBox.setTitle(_translate("MainWindow", "Add New User"))
        self.label_22.setText(_translate("MainWindow", "User Name"))
        self.label_23.setText(_translate("MainWindow", "Email"))
        self.label_24.setText(_translate("MainWindow", "Password"))
        self.label_25.setText(_translate("MainWindow", "Again Password"))
        self.pushButton_12.setText(_translate("MainWindow", "Add User"))
        self.pushButton_12.clicked.connect(self.add_newuser)
        self.groupBox_2.setTitle(_translate("MainWindow", "Edit User Information"))
        self.label_26.setText(_translate("MainWindow", "User Name"))
        self.label_27.setText(_translate("MainWindow", "Email"))
        self.label_28.setText(_translate("MainWindow", "Password"))
        self.label_29.setText(_translate("MainWindow", "Again Password"))
        self.label_30.setText(_translate("MainWindow", "User Name"))
        self.label_31.setText(_translate("MainWindow", "Password"))

        self.pushButton_13.setText(_translate("MainWindow", "Login"))
        self.pushButton_13.clicked.connect(self.login)

        self.pushButton_14.setText(_translate("MainWindow", "Edit User Data"))
        self.pushButton_14.clicked.connect(self.edit_user)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Tab3"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category Name"))

        self.pushButton_15.setText(_translate("MainWindow", "Add New Categoriy"))
        self.pushButton_15.clicked.connect(self.add_category)

        self.label_32.setText(_translate("MainWindow", "New Categori Name"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Categoris"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author Name"))
        self.label_33.setText(_translate("MainWindow", "New Author Name"))

        self.pushButton_16.setText(_translate("MainWindow", "Add New Author"))
        self.pushButton_16.clicked.connect(self.add_author)

        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Author"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Publisher Name"))
        self.label_34.setText(_translate("MainWindow", "New Publisher Name"))

        self.pushButton_17.setText(_translate("MainWindow", "Add New Publisher"))
        self.pushButton_17.clicked.connect(self.add_publisher)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "Publisher"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Tab 4"))

        self.pushButton_18.setText(_translate("MainWindow", "darkblue"))
        self.pushButton_18.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_19.setText(_translate("MainWindow", "darkgray"))
        self.pushButton_19.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_20.setText(_translate("MainWindow", "darkorange"))
        self.pushButton_20.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_21.setText(_translate("MainWindow", "qdark"))
        self.pushButton_21.clicked.connect(self.QDark_Theme)

        self.label_35.setText(_translate("MainWindow", "Apply Your themes:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Tab 5"))

        ##########   start open ctab connction
        self.pushButton.setText(_translate("MainWindow", "HOME"))
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.setText(_translate("MainWindow", "BOOK"))
        self.pushButton_2.clicked.connect(self.book)
        self.pushButton_3.setText(_translate("MainWindow", "USER"))
        self.pushButton_3.clicked.connect(self.user)
        self.pushButton_4.setText(_translate("MainWindow", "SETTING"))
        self.pushButton_4.clicked.connect(self.setting)
        self.pushButton_5.setText(_translate("MainWindow", "Theam"))
        self.pushButton_5.clicked.connect(self.theme)

        self.pushButton_6.clicked.connect(self.Export_Day_Operations)
    ####  conncton of tabwidget
    def home(self):
        self.tabWidget.setCurrentIndex(0)
    def book(self):
        self.tabWidget.setCurrentIndex(1)
    def user(self):
        self.tabWidget.setCurrentIndex(2)
    def setting(self):
        self.tabWidget.setCurrentIndex(3)
    def theme(self):
        self.tabWidget.setCurrentIndex(4)
#########  END TABOPEN CONNECTION
    #############  start book ###
    def add_newbook(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            book_title=self.lineEdit_2.text()
            book_code=self.lineEdit_3.text()
            book_category = self.comboBox_3.currentText()
            book_author = self.comboBox_4.currentText()
            book_publisher = self.comboBox_5.currentText()
            book_price = self.lineEdit_4.text()
            book_description=self.plainTextEdit.toPlainText()
            self.cur.execute('''
                INSERT INTO books(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
                VALUES (%s , %s , %s , %s , %s , %s , %s)
            ''' ,(book_title,book_description  , book_code , book_category , book_author , book_publisher , book_price,))

            self.db.commit()
            self.show_all_data_ui()
        except:
            print('e')
    def show_all_data_ui(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT book_code,book_name,book_category,book_author,book_publisher,book_description,book_price FROM books''')
            data = self.cur.fetchall()

            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
        except:
            print('e')





############  start seach_book
    def search_book(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            book_title = self.lineEdit_8.text()

            sql = ''' SELECT * FROM books WHERE book_name = %s'''
            self.cur.execute(sql , [(book_title)])

            data = self.cur.fetchone()
            print(data)
            title=data[1]
            print(title)
            self.lineEdit_9.setText(title)
            code=data[3]
            print(code)
            self.lineEdit_10.setText(code)
            price=data[7]
            print(price)
            self.lineEdit_11.setText(price)
            category=data[4]
            print(category)
            self.comboBox_9.addItem(category)
            author=data[5]
            print(author)
            self.comboBox_10.addItem(author)
            publisher=data[6]
            print(publisher)
            self.comboBox_11.addItem(publisher)
            des=data[2]
            self.plainTextEdit_3.setPlainText(des)
        except:
            print('e')
            #############  end search book###########
################   start edit book
    def edit_book(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            book_title = self.lineEdit_9.text()
            book_description = self.plainTextEdit_3.toPlainText()
            book_code = self.lineEdit_10.text()
            book_category = self.comboBox_9.currentText()
            book_author = self.comboBox_10.currentText()
            book_publisher = self.comboBox_11.currentText()
            book_price = self.lineEdit_11.text()

            search_book_title = self.lineEdit_8.text()

            self.cur.execute('''
                 UPDATE books SET book_name=%s ,book_description=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name = %s            
             ''', (book_title, book_description, book_code, book_category, book_author, book_publisher, book_price,
                   search_book_title))

            self.db.commit()
            print('done')
            self.statusBar().showMessage('book updated')
            self.show_all_data_ui()
        except:
            print('e')
#################  end edit book#############
    def delete_book(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            book_title = self.lineEdit_8.text()

            warning = QMessageBox.warning(self , 'Delete Book' , "are you sure you want to delete this book" , QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes :
                sql = ''' DELETE FROM books WHERE book_name = %s '''
                self.cur.execute(sql , [(book_title)])
                self.db.commit()
                print('done')

                self.show_all_data_ui()
        except:
            print('e')
###########  end delete book
###########  end book#######
    ########  user #######
    def add_newuser(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            username = self.lineEdit_12.text()
            email = self.lineEdit_13.text()
            password = self.lineEdit_14.text()
            password2 = self.lineEdit_15.text()

            if password == password2 :
                self.cur.execute(''' 
                    INSERT INTO user(user_name , user_email , user_password)
                    VALUES (%s , %s , %s)
                ''' , (username , email , password,))

                self.db.commit()
                print('done')
        except:
            print('this is a wrong')
    def login(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            username = self.lineEdit_20.text()
            password = self.lineEdit_21.text()

            sql = ''' SELECT * FROM user'''

            self.cur.execute(sql)
            data = self.cur.fetchall()
            for row in data:
                if username == row[1] and password == row[3]:
                    print('user match')

                    self.lineEdit_16.setText(row[1])
                    self.lineEdit_17.setText(row[2])
                    self.lineEdit_18.setText(row[3])
        except:
            print('e')

    def edit_user(self):
        try:
            username = self.lineEdit_16.text()
            email = self.lineEdit_17.text()
            password = self.lineEdit_18.text()
            password2 = self.lineEdit_18.text()

            original_name = self.lineEdit_20.text()

            if password == password2 :
                self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
                self.cur = self.db.cursor()

                print(username)
                print(email)
                print(password)

                self.cur.execute('''
                    UPDATE user SET user_name=%s , user_email=%s , user_password=%s WHERE user_name=%s
                ''', (username , email , password , original_name))

                self.db.commit()
                print('done')

            else:
                print('make sure you entered you password correctly')
        except:
            print('e')
    ##########  end user
#######  setting ######
    def add_category(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            category_name=self.lineEdit_22.text()

            self.cur.execute('''
                INSERT INTO category (category_name) VALUES (%s)
            ''' , (category_name,))

            self.db.commit()
            self.lineEdit_22.setText('')
            self.statusBar().showMessage('New Category Addedd ')
            self.show_category()
        except:
            print('e')
    def show_category(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT category_name FROM category''')
            data = self.cur.fetchall()
            print(data)

            if data :
                self.tableWidget_2.setRowCount(0)
                self.tableWidget_2.insertRow(0)
                for row , form in enumerate(data):
                    for column , item in enumerate(form) :
                        self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                        column += 1

                    row_position = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(row_position)
        except:
            print('e')
############   end of a add category

    def add_author(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            author_name=self.lineEdit_23.text()

            self.cur.execute('''
                INSERT INTO author (author_name) VALUES (%s)
            ''' , (author_name,))

            self.db.commit()
            self.statusBar().showMessage('New Category Addedd ')
            self.show_author()
        except:
            print('e')
    def show_author(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT author_name FROM author''')
            data = self.cur.fetchall()
            print(data)

            if data :
                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)
                for row , form in enumerate(data):
                    for column , item in enumerate(form) :
                        self.tableWidget_3.setItem(row , column , QTableWidgetItem(str(item)))
                        column += 1

                    row_position = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(row_position)
        except:
            print('e')
###########   end of show author


    def add_publisher(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            publisher_name=self.lineEdit_24.text()

            self.cur.execute('''
                INSERT INTO publisher (publisher_name) VALUES (%s)
            ''' , (publisher_name,))

            self.db.commit()
            self.statusBar().showMessage('New Category Addedd ')
            self.show_publisher()
        except:
            print('s')
    def show_publisher(self):
        try:

            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT publisher_name FROM publisher''')
            data = self.cur.fetchall()
            print(data)

            if data:
                self.tableWidget_4.setRowCount(0)
                self.tableWidget_4.insertRow(0)
                for row, form in enumerate(data):
                    for column, item in enumerate(form):
                        self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1

                    row_position = self.tableWidget_4.rowCount()
                    self.tableWidget_4.insertRow(row_position)
        except:
            print('e')
    ###########   end of show author

############   change them  #######

    def Dark_Blue_Theme(self):

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(3, 18, 14))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.blue)
        palette.setColor(QtGui.QPalette.Background,QtCore.Qt.black)
        app.setPalette(palette)

    def Dark_Gray_Theme(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.Foreground,Qt.black)
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Background,Qt.black)
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
        dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
        dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
        dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        QApplication.setPalette(dark_palette)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

################  end of theme work
    ########  start show category comobox
    def add_category_comobox(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT category_name FROM category''')
            data = self.cur.fetchall()
            for category in data:
                print(category[0])
                self.comboBox_9.addItem(category[0])
        except:
            print('d')
    def edit_category_comobox(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT category_name FROM category''')
            data = self.cur.fetchall()
            for category in data:
                print(category[0])
                self.comboBox_3.addItem(category[0])
        except:
            print('d')
    def author_comobox(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT author_name FROM author''')
            data = self.cur.fetchall()
            print(data)

            for category in data:
                print(category[0])
                self.comboBox_4.addItem(category[0])
        except:
            print('w')
    def edit_author_comobox(self):
        try:
            self.db = pymysql.connect(host='localhost' , user='root' , password ='12345678' , db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT author_name FROM author''')
            data = self.cur.fetchall()
            print(data)
            for category in data:
                print(category[0])
                self.comboBox_10.addItem(category[0])
        except:
            print('e')
    def publisher_comobox(self):
        try:

            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT publisher_name FROM publisher''')
            data = self.cur.fetchall()
            print(data)

            for category in data:
                print(category[0])
                self.comboBox_5.addItem(category[0])
        except:
            print('w')
    def edit_publisher_comobox(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' SELECT publisher_name FROM publisher''')
            data = self.cur.fetchall()
            print(data)

            for category in data:
                print(category[0])
                self.comboBox_11.addItem(category[0])
        except:
            print('w')
########   start of edilt button work




################   this is a searchbook

    ######### Export Data #################
    def Export_Day_Operations(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='12345678', db='library')
            self.cur = self.db.cursor()

            self.cur.execute(''' 
                SELECT book_code , book_name , book_category ,book_author, book_publisher,book_description,book_price FROM books
            ''')

            data = self.cur.fetchall()

            wb = Workbook('excell.xlsx')
            sheet1  = wb.add_worksheet()

            sheet1.write(0,0,'book_code')
            sheet1.write(0,1,'book_name')
            sheet1.write(0,2,'book_category')
            sheet1.write(0,3,'book_author')
            sheet1.write(0,4,'book_publisher')
            sheet1.write(0,5,'book_description')
            sheet1.write(0,6,'book_price')


            row_number = 1
            for row in data :
                column_number = 0
                for item in row :
                    sheet1.write(row_number , column_number , str(item))
                    column_number += 1
                row_number += 1

            wb.close()
            self.statusBar().showMessage('Report Created Successfully')
        except:
            print('this is a wrong')

#######################  end export data###############










import name_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
