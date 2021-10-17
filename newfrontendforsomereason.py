from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('untitled.ui', self)
        self.checkBox.stateChanged.connect(self.allportsclick)
        self.checkBox_2.stateChanged.connect(self.nopingclick)
        self.checkBox_3.stateChanged.connect(self.t4click)
        self.checkBox_4.stateChanged.connect(self.sVclick)
        self.checkBox_5.stateChanged.connect(self.sCclick)
        self.checkBox_6.stateChanged.connect(self.tacktackopenclick)
        self.enterip.textChanged.connect(self.printuserin)
        self.enterfile.textChanged.connect(self.printuserin1)
    
    def printuserin(self):
        userinput = self.enterip.toPlainText()
        return userinput

    def printuserin1(self):
        userinput1 = self.enterfile.toPlainText()
        return userinput1

    def allportsclick(self, checked):
        if checked:
            print('-p-')
            return 1
        else:
            print('no -p-')
            return 0

    def nopingclick(self, checked):
        if checked:
            print('-Pn')
            return 1
        else:
            print('no -Pn')
            return 0

    def t4click(self, checked):
        if checked:
            print('-T4')
            return 1
        else:
            print('no -T4')
            return 0
    
    def sVclick(self, checked):
        if checked:
            print('-sV')
            return 1
        else:
            print('no -sV')
            return 0
    
    def sCclick(self, checked):
        if checked:
            print('-sC')
            return 1
        else:
            print('no -sC')
            return 0

    def tacktackopenclick(self, checked):
        if checked:
            print('--open')
            return 1
        else:
            print('no --open')
            return 0



app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())