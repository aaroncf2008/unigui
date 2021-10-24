from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QListWidget, QHBoxLayout,QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
from PyQt5.uic import loadUi
import subprocess
import xmltodict
import random
import json
import sys

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('untitled.ui', self)
        self.listWidget_2.setSpacing(3)
        self.checkBox.stateChanged.connect(self.allportsclick)
        self.checkBox.setChecked(True)
        self.checkBox_2.stateChanged.connect(self.nopingclick)
        self.checkBox_3.stateChanged.connect(self.t4click)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.stateChanged.connect(self.sVclick)
        self.checkBox_5.stateChanged.connect(self.sCclick)
        self.checkBox_6.stateChanged.connect(self.tacktackopenclick)
        self.checkBox_6.setChecked(True)
        self.enterip.textChanged.connect(self.printuserin)
        self.optionalarg_2.textChanged.connect(self.printuserin2)
        self.enterfile.textChanged.connect(self.printuserin1)
        self.sendterminal.clicked.connect(self.sendterminalcommand)
        self.runnmapbutton.clicked.connect(self.runnmap)
        self.portinfo.currentIndexChanged.connect(self.showportinfo)
        self.button1.clicked.connect(self.button1commandset)
        self.button2.clicked.connect(self.button2commandset)
        self.button3.clicked.connect(self.button3commandset)
        self.button4.clicked.connect(self.button4commandset)
        self.button5.clicked.connect(self.button5commandset)
        l1 = QListWidgetItem("Ferox Buster")
        self.listWidget.insertItem(1, l1)

    global commandhistory
    with open("history.json", "r") as outfile:
        commandhistory = json.load(outfile)
        
    
    
    
    
    
    #nmap
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
    global optionalarg
    optionalarg = ''
    global commandsync
    global command
    command = ''
    global cmdrun
    global comm
    comm = ''
    global portdata
    global commandhistoryload
    global currentcommand

    def commandhistoryload(self):
        x = 0
        if x == 0:
            for i in commandhistory:
                x = x + 1
                if x == 1:
                    self.button1.setText(i)
                    self.button1.setEnabled(True)
                elif x == 2:
                    self.button2.setText(i)
                    self.button2.setEnabled(True)
                elif x == 3:
                    self.button3.setText(i)
                    self.button3.setEnabled(True)
                elif x == 4:
                    self.button4.setText(i)
                    self.button4.setEnabled(True)
                elif x == 5:
                    self.button5.setText(i)
                    self.button5.setEnabled(True)
                else:
                    print('Too many..')
                    pass
        else:
            pass
        print(commandhistory)
        f = open('history.json', 'w')
        
        if len(commandhistory) > 5:
            print(commandhistory)
            commandhistory.pop()
            print(commandhistory)
            f.write(json.dumps(commandhistory))
        else:
            f.write(json.dumps(commandhistory))
        f.close()
    
    
    
    
    
    #nmap
    def button1commandset(self):
        buttontext = self.button1.text()
        self.terminalinput.setText(buttontext)

    def button2commandset(self):
        buttontext = self.button2.text()
        self.terminalinput.setText(buttontext)

    def button3commandset(self):
        buttontext = self.button3.text()
        self.terminalinput.setText(buttontext)

    def button4commandset(self):
        buttontext = self.button4.text()
        self.terminalinput.setText(buttontext)

    def button5commandset(self):
        buttontext = self.button5.text()
        self.terminalinput.setText(buttontext)

    def pushbutton(self):
        listttt = ['a','b','c','d','e']
        g = random.choice(listttt) + random.choice(listttt) + random.choice(listttt) + random.choice(listttt) + random.choice(listttt)
        self.button1.setText(g)

    def commandsync(self):
        global command
        command = f'nmap{sV}{sC}{t4}{tackptack}{tacktackopen}{noping} {ip} -oA {filename} {optionalarg}'
        self.commanddisplay.setText(command)

    def sendterminalcommand(self):
        comm = self.terminalinput.toPlainText()
        commandhistory.insert(0,comm)
        comm = str(comm)
        commhistoryvar = comm
        print(commhistoryvar)
        commandhistoryload(self)
        outpt = cmdrun(comm)
        outpt = outpt.decode("utf-8")
        self.terminalinput.setText('')
        self.terminaloutput.setText(outpt)

    def runnmap(self):
        outpt = cmdrun(command)
        outpt = outpt.decode("utf-8")
        self.nmapoutput.setText(outpt)
        while True:
            if 'Nmap done' in str(outpt):
               portdata(self, filename)
               break
            else:
               pass

    def portdata(self, file):
        with open(f"{file}.xml") as f:
            data_dict = xmltodict.parse(f.read())
        f.close()
        text1 = 'Ports'
        json_data = json.dumps(data_dict)
        json_data = json.loads(json_data)
        try:
            ports = json_data['nmaprun']['host']['ports']['port']
        except:
            text='No Ports Open'
            self.portslist.setText(text)
            return 0
        else:
            pass
        for i in ports:
            portid = i['@portid']
            print(portid)
            text1 = text1 + f'\n {portid}' 
            services = i['service']['@name']
            print(services)
            text1 = text1 + f' {services}'
        self.portslist.setText(text1)
        self.portinfo.clear()
        for i in ports:
            self.portinfo.addItem(i['@portid'])
            self.listWidget_2.addItem(f"{i['@portid']} | {i['service']['@name']}")

    def showportinfo(self):
        with open(f"{filename}.xml") as f:
            data_dict = xmltodict.parse(f.read())
        f.close()
        json_data = json.dumps(data_dict)
        json_data = json.loads(json_data)
        jay = self.portinfo.currentIndex()
        gg = json_data['nmaprun']['host']['ports']['port'][jay]['service']
        global finaltext
        finaltext = ''
        try:
            for g in gg:
                finaltext = finaltext + f'{gg[g]}\n'
        except:
            finaltext = 'There is no advanced port data.'
        else:
            pass
        self.portinfobox.setText(finaltext)
        


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

    def printuserin2(self):
        global optionalarg
        userinput = self.optionalarg_2.toPlainText()
        optionalarg = userinput
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