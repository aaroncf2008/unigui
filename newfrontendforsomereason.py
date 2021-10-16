from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('untitled.ui', self)

    def retrieveText(self):
        words = self.plainTextEdit.c



app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())