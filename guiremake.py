from tkinter import ttk
from bs4 import BeautifulSoup
import xmltodict
import lxml
import json
import tkinter as tk                    
import subprocess  
import os
root = tk.Tk()
root.title("Tab Widget")

#root.geometry('782x739')
fontfont = ('Verdana', 14)
bg = '#0E0E0E'
style = ttk.Style()
style.configure("BW.TLabel", background=bg)

root.configure(bg=bg)
tabControl = ttk.Notebook(root, style="BW.TLabel")

tab1 = ttk.Frame(tabControl, style="BW.TLabel")
tab2 = ttk.Frame(tabControl, style="BW.TLabel")
tab3 = ttk.Frame(tabControl, style="BW.TLabel")
tabControl.add(tab1, text ='Terminal')
tabControl.add(tab2, text ='NMAP')
tabControl.add(tab3, text ='NMAP Output')
tabControl.pack()


#ttk.Label(tab1, text ="He has an irl girlfriend").grid(column = 0, row = 0, padx = 30, pady = 30)  
#ttk.Label(tab2, text ="Toaster is my boss at work").grid(column = 0, row = 0, padx = 30, pady = 30)

l = tk.Label(tab2, bg='white', width=40, text='nmap', justify='center')
l.pack()

def print_selection():
    text = 'nmap'
    if (allport_nmap_var.get() == 1):
        text = text + ' -p-'
    else:
        pass
    if (pn_nmap_var.get() == 1):
        text = text + ' -Pn'
    else:
        pass
    if (t4_nmap_var.get() == 1):
        text = text + ' -T4'
    else:
        pass
    if (sV_nmap_var.get() == 1):
        text = text + ' -sV'
    else:
        pass
    if (sC_nmap_var.get() == 1):
        text = text + ' -sC'
    else:
        pass
    if (open_nmap_var.get() == 1):
        text = text + ' --open'
    else:
        pass
    text = text + ' ' + e1.get()
    text = text + ' -oA ' + d1.get()

    l.config(text=text)

allport_nmap_var = tk.IntVar()
pn_nmap_var = tk.IntVar()
t4_nmap_var = tk.IntVar()
sV_nmap_var = tk.IntVar()
sC_nmap_var = tk.IntVar()
open_nmap_var = tk.IntVar()

allport_nmap = tk.Checkbutton(tab2, text='-p-',variable=allport_nmap_var, onvalue=1, offvalue=0, command=print_selection, justify='center')
allport_nmap.pack()
pn_nmap = tk.Checkbutton(tab2, text='-Pn',variable=pn_nmap_var, onvalue=1, offvalue=0, command=print_selection, justify='center')
pn_nmap.pack()
t4_nmap = tk.Checkbutton(tab2, text='-T4',variable=t4_nmap_var, onvalue=1, offvalue=0, command=print_selection, justify='center')
t4_nmap.pack()
sV_nmap = tk.Checkbutton(tab2, text='-sV',variable=sV_nmap_var, onvalue=1, offvalue=0, command=print_selection, justify='center')
sV_nmap.pack()
sC_nmap = tk.Checkbutton(tab2, text='-sC',variable=sC_nmap_var, onvalue=1, offvalue=0, command=print_selection, justify='center')
sC_nmap.pack()
open_nmap = tk.Checkbutton(tab2, text='--open',variable=open_nmap_var, onvalue=1, offvalue=0, command=print_selection, justify='center')
open_nmap.pack()

label1 = tk.Label(tab2, text = '', bg = bg, justify='center')
label1.pack()

e2 = tk.Label(tab2, text="IP", justify='center')
e2.pack()

e1 = tk.Entry(tab2, justify='center')
e1.pack()

e3 = tk.Button(tab2, text='Sync IP', command=print_selection, justify='center')
e3.pack()

label = tk.Label(tab2, text = '', bg = bg, justify='center')
label.pack()

d2 = tk.Label(tab2, text="Filename", justify='center')
d2.pack()

d1 = tk.Entry(tab2)
d1.pack()

d3 = tk.Button(tab2, text='Sync Filename', command=print_selection, justify='center')
d3.pack()

label2 = tk.Label(tab2, text = '', bg = bg, justify='center')
label2.pack()

#button for window size
#def size():
#	print(f'{root.winfo_height()}x{root.winfo_width()}')

#d5 = tk.Button(tab2, text='SIZE', command=size, justify='center')
#d5.pack()

h3 = tk.Message(tab2, bg='white', width=250, text='NMAP Scan Output', justify='center')
h3.pack(fill='both', expand=True)

def cmdrun(string):     
    try:         
        res = subprocess.run(string, shell=True, capture_output=True)                 
        print(res.stdout)
        return res.stdout    
    except:         
        print("no worko")


def sendcommand():
    command = 'nmap'
    if (allport_nmap_var.get() == 1):
        command = command + ' -p-'
    else:
        pass
    if (pn_nmap_var.get() == 1):
        command = command + ' -Pn'
    else:
        pass
    if (t4_nmap_var.get() == 1):
        command = command + ' -T4'
    else:
        pass
    if (sV_nmap_var.get() == 1):
        command = command + ' -sV'
    else:
        pass
    if (sC_nmap_var.get() == 1):
        command = command + ' -sC'
    else:
        pass
    if (open_nmap_var.get() == 1):
        command = command + ' --open'
    else:
        pass
    command = command + ' ' + e1.get()
    command = command + ' -oA ' + d1.get()
    outpt = cmdrun(command)
    h3.config(text=outpt)

#label = tk.Label(tab1, text = '', bg = bg)
#label.grid(column=5,row=0)

label2 = tk.Label(tab2, text = '', bg = bg, justify='center')
label2.pack()

frame12 = tk.Frame(tab1)
frame12.pack(anchor="n")

h = tk.Message(frame12, bg='white', width=1000, text='Terminal Output', justify='center')
h.pack(fill=tk.BOTH)
def termcommand():
    command = f1.get()
    textt = cmdrun(command)
    h.config(text=textt)

#f1 = tk.Entry(tab1, justify='left')
#f1.pack(side=tk.LEFT)

f1 = tk.Entry(tab1, justify='left', font=fontfont)
f1.pack(side=tk.LEFT, anchor='sw')

f2 = tk.Button(tab1, text='Send Command To Terminal', command=termcommand, justify='center')
f2.pack(side=tk.RIGHT, anchor='se')

macobutton = tk.Button(tab2, text="Use Command", command=sendcommand, justify='center')
macobutton.pack()

#--------------------------------------------------------------------------------------------------

#def portdata():
#    with open("scan.xml") as f:
#        data_dict = xmltodict.parse(f.read())
#    f.close()
#    text1 = 'Ports'
#    json_data = json.dumps(data_dict)
#    json_data = json.loads(json_data)
#    ports = json_data['nmaprun']['host']['ports']['port']
#    for i in ports:
#        portid = i['@portid']
#        print(portid)
#        text1 = text1 + f'\n {portid}'
#        for g in i['service']:
#            services = i['service'][g]
#            print(services)
#            text1 = text1 + f' {services}'
#    y3.config(text=text1)

def portdata():
    with open("scan.xml") as f:
        data_dict = xmltodict.parse(f.read())
    f.close()
    text1 = 'Ports'
    json_data = json.dumps(data_dict)
    json_data = json.loads(json_data)
    ports = json_data['nmaprun']['host']['ports']['port']
    for i in ports:
        portid = i['@portid']
        print(portid)
        text1 = text1 + f'\n {portid}'
        services = i['service']['@name']
        print(services)
        text1 = text1 + f' {services}'
    y3.config(text=text1)

y3 = tk.Message(tab3, text='Ports', justify='left', width=1000)
y3.pack(side=tk.LEFT, anchor='nw')

y4 = tk.Button(tab3, text='Sync Port Data', command=portdata, justify='center')
y4.pack(side=tk.LEFT, anchor='nw')

root.mainloop()