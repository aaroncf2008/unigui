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
        self.plainTextEdit.triggered.connect(self.printuserin)
    
    def printuserin(self):
        userinput = self.plainTextEdit.toPlainText()
        print(userinput)
    
    def allportsclick(self, checked):
        if checked:
            print('-p-')
        else:
            print('no -p-')

    def nopingclick(self, checked):
        if checked:
            print('-Pn')
        else:
            print('no -Pn')

    def t4click(self, checked):
        if checked:
            print('-T4')
        else:
            print('no -T4')
    
    def sVclick(self, checked):
        if checked:
            print('-sV')
        else:
            print('no -sV')
    
    def sCclick(self, checked):
        if checked:
            print('-sC')
        else:
            print('no -sC')

    def tacktackopenclick(self, checked):
        if checked:
            print('--open')
        else:
            print('no --open')



app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())