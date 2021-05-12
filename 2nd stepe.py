

from xlrd import *
from xlsxwriter import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import sys

def change_theme(self):
    pal = QtWidgets.QApplication.palette()
    #The next line works
    pal.setColor(QtGui.QPalette.Highlight, QtGui.QColor(0, 0, 128))
    #The next line doesnt work. Expected it to change the Tab Widget color
    #using this line.
    pal.setColor(QtGui.QPalette.Button, QtGui.QColor(62, 80, 91))
    QtWidgets.QApplication.setPalette(pal)




























