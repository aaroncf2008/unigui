from tkinter import ttk
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
tabControl.add(tab1, text ='Terminal')
tabControl.add(tab2, text ='NMAP')
tabControl.pack()


#ttk.Label(tab1, text ="He has an irl girlfriend").grid(column = 0, row = 0, padx = 30, pady = 30)  
#ttk.Label(tab2, text ="Toaster is my boss at work").grid(column = 0, row = 0, padx = 30, pady = 30)

l = tk.Label(tab2, bg='white', width=40, text='nmap', justify='center')
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
    if (var6.get() == 1):
        text = text + ' --open'
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
var6 = tk.IntVar()
c1 = tk.Checkbutton(tab2, text='-p-',variable=var1, onvalue=1, offvalue=0, command=print_selection, justify='center')
c1.pack()
c2 = tk.Checkbutton(tab2, text='-Pn',variable=var2, onvalue=1, offvalue=0, command=print_selection, justify='center')
c2.pack()
c3 = tk.Checkbutton(tab2, text='-T4',variable=var3, onvalue=1, offvalue=0, command=print_selection, justify='center')
c3.pack()
c4 = tk.Checkbutton(tab2, text='-sV',variable=var4, onvalue=1, offvalue=0, command=print_selection, justify='center')
c4.pack()
c5 = tk.Checkbutton(tab2, text='-sC',variable=var5, onvalue=1, offvalue=0, command=print_selection, justify='center')
c5.pack()
c5 = tk.Checkbutton(tab2, text='--open',variable=var6, onvalue=1, offvalue=0, command=print_selection, justify='center')
c5.pack()

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

root.mainloop()