#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import tkinter as tk
import xmltodict
import lxml
import json

root = tk.Tk()
root.title('INFO')
root.geometry('500x500')
bg = '#0E0E0E'
root.configure(bg=bg)

with open('scan.xml') as f:
    data_dict = xmltodict.parse(f.read())

f.close()

json_data = json.dumps(data_dict)

json_data = json.loads(json_data)

ports = json_data['nmaprun']['host']['ports']['port']

variable = tk.IntVar()
portid22 = {
    'indexnum': 0,
    'portid': 22,
}
def setportinfo(self):
    print(variable.get())
    gg = json_data['nmaprun']['host']['ports']['port'][int(variable.get())]['service']
    text6 = ''

    try:
        for i in gg:
            text6 = text6 + f'{[i]} : {gg[i]}\n'
            print(text6)
    except:
        text4 = 'There is no more port data'
    else:
        pass

    h.config(text=text6)

w = tk.OptionMenu(root, variable, portid22, 1, 2, command=setportinfo)
w.pack()
h = tk.Label(root, text='INFO HERE')
h.pack()
#for i in ports:
#    # print(i['@portid'])
#    for g in i['service']:
#        # print(i['service'][g])
#        pass
#   # print('\n\n')

root.mainloop()