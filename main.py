from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)

import json

data = json.load(open('apps.json'))


def btnFunction(num):
    print(num)

count = 0
for i in data:
    print(i)
    button = ttk.Button(frm, text=f"Open {i['name']}",command=lambda :btnFunction(count))
    button.pack()
    count = count + 1

frm.pack()
root.mainloop()