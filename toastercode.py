#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid() 
ttk.Label(frm, text="Hello World!").grid(column=0, row=0) 
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0) 
term = ttk.Entry(frm, text="terminal", width=10) 
term.grid(column=0, row=99) 
term.insert(0, "EPIC") 
tt = term.get() 
print(tt) 
root.mainloop()
