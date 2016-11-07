from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root,width = 30)
entry.pack()
entry.get()

entry.delete(0,1)
