from tkinter import *
from tkinter import ttk
import os
import subprocess
import webbrowser
import sys


root = Tk()
frm = ttk.Frame(root, padding=10)

import json

data = json.load(open('apps.json'))


def btnFunction(num):
    # print(num)
    # print(data[num])
    for count in data[num].get("vscodepaths"):
        path = count
        os.system("code . /K cd "+path)
    
    for website in data[num].get("websites"):
        webbrowser.open(website,new=1, autoraise=True)


L = Label(root,text="Project Link Manager")

L.pack()

count = 0
for i in data:
    print(i)
    button = ttk.Button(frm, text=f"Open {i['name']}",command=lambda :btnFunction(count))
    button.pack()
    count + 1

frm.pack()
root.mainloop()