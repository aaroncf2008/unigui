from tkinter import ttk
import tkinter as tk                    
import subprocess  
import os
root = tk.Tk()
root.title("Tab Widget")

#root.geometry('2000x1000')

bg = '#695f5e'
style = ttk.Style()
style.configure("BW.TLabel", background=bg)


root.configure(bg=bg)
tabControl = ttk.Notebook(root, style="BW.TLabel")

tab1 = ttk.Frame(tabControl, style="BW.TLabel")
tab2 = ttk.Frame(tabControl, style="BW.TLabel")
tabControl.add(tab1, text ='Terminal')
tabControl.add(tab2, text ='NMAP')
tabControl.grid(column=10, row=0)


#ttk.Label(tab1, text ="He has an irl girlfriend").grid(column = 0, row = 0, padx = 30, pady = 30)  
#ttk.Label(tab2, text ="Toaster is my boss at work").grid(column = 0, row = 0, padx = 30, pady = 30)

l = tk.Label(tab2, bg='white', width=40, text='nmap')
l.grid(column=5, row=0)
def print_selection():
    text = 'nmap'
    if (var1.get() == 1):
        text = text + ' -p-'
    else:
        pass
    if (var2.get() == 1):
        text = text + ' -Pn'
    else:
        pass
    if (var3.get() == 1):
        text = text + ' -T4'
    else:
        pass
    if (var4.get() == 1):
        text = text + ' -sV'
    else:
        pass
    if (var5.get() == 1):
        text = text + ' -sC'
    else:
        pass
    text = text + ' ' + e1.get()
    text = text + ' -oA ' + d1.get()

    l.config(text=text)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
c1 = tk.Checkbutton(tab2, text='-p-',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.grid(column=5, row=1)
c2 = tk.Checkbutton(tab2, text='-Pn',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.grid(column=5, row=2)
c3 = tk.Checkbutton(tab2, text='-T4',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.grid(column=5, row=3)
c4 = tk.Checkbutton(tab2, text='-sV',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.grid(column=5, row=4)
c5 = tk.Checkbutton(tab2, text='-sC',variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.grid(column=5, row=5)

label1 = tk.Label(tab2, text = '', bg = bg)
label1.grid(column=5, row=6)

e2 = tk.Label(tab2, text="IP")
e2.grid(column=5, row=7)

e1 = tk.Entry(tab2)
e1.grid(column=5, row=8)

e3 = tk.Button(tab2, text='Sync IP', command=print_selection)
e3.grid(column=5, row=9)

label = tk.Label(tab2, text = '', bg = bg)
label.grid(column=5, row=10)

d2 = tk.Label(tab2, text="Filename")
d2.grid(column=5, row=11)

d1 = tk.Entry(tab2)
d1.grid(column=5, row=12)

d3 = tk.Button(tab2, text='Sync Filename', command=print_selection)
d3.grid(column=5, row=13)

label2 = tk.Label(tab2, text = '', bg = bg)
label2.grid(column=5, row=14)

def cmdrun(string):     
    try:         
        res = subprocess.run(string, shell=True, capture_output=True)                 
        print(res.stdout)
        return res.stdout    
    except:         
        print("no worko")


def sendcommand():
    command = 'nmap'
    if (var1.get() == 1):
        command = command + ' -p-'
    else:
        pass
    if (var2.get() == 1):
        command = command + ' -Pn'
    else:
        pass
    if (var3.get() == 1):
        command = command + ' -T4'
    else:
        pass
    if (var4.get() == 1):
        command = command + ' -sV'
    else:
        pass
    if (var5.get() == 1):
        command = command + ' -sC'
    else:
        pass
    command = command + ' ' + e1.get()
    command = command + ' -oA ' + d1.get()

    cmdrun(command)

#label = tk.Label(tab1, text = '', bg = bg)
#label.grid(column=5,row=0)

h = tk.Message(tab1, bg='white', width=1000, text='Terminal Output')
h.grid(column=7,row=1, padx = 45, pady = 10)

def termcommand():
    command = f1.get()
    textt = cmdrun(command)
    h.config(text=textt)

f1 = tk.Entry(tab1)
f1.grid(column=7, row=2, padx = 40, pady = 10)

f2 = tk.Button(tab1, text='Send Command To Terminal', command=termcommand)
f2.grid(column=7,row=3, padx = 40, pady = 10)

macobutton = tk.Button(tab2, text="Use Command", command=sendcommand)
macobutton.grid(column=5, row=15, padx = 40, pady = 10)

root.mainloop()