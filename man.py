#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import subprocess
import os
window = tk.Tk()
window.title('Nmap Scan')
window.geometry('1000x1000')
bg = '#695f5e'
window.configure(bg=bg)
l = tk.Label(window, bg='white', width=40, text='nmap')
l.pack()
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
c1 = tk.Checkbutton(window, text='-p-',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='-Pn',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='-T4',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='-sV',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
c5 = tk.Checkbutton(window, text='-sC',variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.pack()

label1 = tk.Label(window, text = '', bg = bg)
label1.pack()

e2 = tk.Label(window, text="IP")
e2.pack()

e1 = tk.Entry(window)
e1.pack()

e3 = tk.Button(window, text='Sync IP', command=print_selection)
e3.pack()

label = tk.Label(window, text = '', bg = bg)
label.pack()

d2 = tk.Label(window, text="Filename")
d2.pack()

d1 = tk.Entry(window)
d1.pack()

d3 = tk.Button(window, text='Sync Filename', command=print_selection)
d3.pack()

label2 = tk.Label(window, text = '', bg = bg)
label2.pack()

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

macobutton = tk.Button(window, text="Use Command", command=sendcommand)
macobutton.pack()

label = tk.Label(window, text = '', bg = bg)
label.pack()

h = tk.Message(window, bg='white', width=1000, text='Terminal Output')
h.pack()

def termcommand():
    command = f1.get()
    textt = cmdrun(command)
    h.config(text=textt)


f1 = tk.Entry(window)
f1.pack()

f2 = tk.Button(window, text='Send Command To Terminal', command=termcommand)
f2.pack()


window.mainloop()