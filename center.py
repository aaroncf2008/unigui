import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
    
button1 = tk.Label(text='Hey', justify='center')
canvas1.create_window(200, 180, window=button1)


root.mainloop()