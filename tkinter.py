from tkinter import *
from tkinter import ttk

root = Tk() #Tk constructor window
button = ttk.Button(root, text = 'Click Me') #Creating a widget
#It's not visible yet though because it doesn't know where to put it
button.pack() #now it will show up
button['text'] #this will return what the text says
#square brackets are whats necessary for this
button['text'] = 'Press Me'
#can also use config
button.config(text = 'Push Me')
str(button) #this will bring back the tk number
#these demonstrate the hierarchy like root will always be '.'
ttk.Label(root, text = ' Hello, Tkinter!').pack()
#adds a label
