import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('1000x1000')
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

vardic = {
    'var1': '-p-',
    'var2': '-Pn',
    'var3': '-T4',
    'var4': '-T5',
    }
    
command = 'nmap'
def print_selection():
    for i in vardic:

        var = vardic.get(i)
        print(var)
        if var == 1:
            command = command + f' {var}'
            print(command)
        else:
            pass
        
c1 = tk.Checkbutton(window, text='-p-',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='-Pn',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='-T4',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='-T5',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()

window.mainloop()