from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import subprocess
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
        self.sendterminal.clicked.connect(self.sendterminalcommand)
        self.runnmapbutton.clicked.connect(self.runnmap)
    
    global ip
    ip = ''
    global filename
    filename = ''
    global tackptack
    tackptack = ''
    global noping
    noping = ''
    global t4
    t4 = ''
    global sV
    sV = ''
    global sC
    sC = ''
    global tacktackopen
    tacktackopen = ''
    global commandsync
    global command
    command = ''
    global cmdrun
    
    def commandsync(self):
        global command
        command = f'nmap{sV}{sC}{t4}{tackptack}{tacktackopen}{noping} {ip} -oA {filename}'
        self.commanddisplay.setText(command)

    def sendterminalcommand(self):
        comm = self.terminalinput.toPlainText()
        comm = str(comm)
        outpt = cmdrun(comm)
        outpt = outpt.decode("utf-8")
        self.terminaloutput.setText(outpt)

    def runnmap(self):
        outpt = cmdrun(command)
        outpt = outpt.decode("utf-8")
        self.nmapoutput.setText(outpt)
        #while True:
        #    if 'Nmap done' in str(outpt):
        #       portdata(filename)
        #      break
        #    else:
        #       pass



    def cmdrun(string):     
        try:         
            res = subprocess.run(string, shell=True, capture_output=True)                 
            print(res.stdout)
            return res.stdout    
        except:         
            print("no worko")


    def printuserin(self):
        userinput = self.enterip.toPlainText()
        global ip 
        ip = userinput
        commandsync(self)

    def printuserin1(self):
        global filename
        userinput = self.enterfile.toPlainText()
        filename = userinput
        commandsync(self)

    def allportsclick(self, checked):
        global tackptack
        if checked:
            tackptack = ' -p-'
        else:
            tackptack = ''
        commandsync(self)

    def nopingclick(self, checked):
        global noping
        if checked:
            noping = ' -Pn'
        else:
            noping = ''
        commandsync(self)

    def t4click(self, checked):
        global t4
        if checked:
            t4 = ' -T4'
        else:
            t4 = ''
        commandsync(self)
    
    def sVclick(self, checked):
        global sV
        if checked:
            sV = ' -sV'
        else:
            sV = ''
        commandsync(self)
    
    def sCclick(self, checked):
        global sC
        if checked:
            sC = ' -sC'
        else:
            sC = ''
        commandsync(self)

    def tacktackopenclick(self, checked):
        global tacktackopen
        if checked:
            tacktackopen = ' --open'
        else:
            tacktackopen = ''
        commandsync(self)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())