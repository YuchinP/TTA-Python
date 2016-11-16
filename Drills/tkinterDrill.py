from tkinter import *
from tkinter import ttk

import tkinterDrillFunc


class ShutilUI(Frame):
    
    def __init__(self,root):

        Frame.__init__(self,root)

        #   Title of the UI
        self.label = ttk.Label(root, text = "File Moving UI", justify = CENTER, font = ('Courier', 13, 'bold'))
        self.label.pack()

        #   Creation of the paned window
        self.panedwindow = ttk.Panedwindow(root, orient = VERTICAL)
        self.panedwindow.pack(expand = False)
        self.frame1 = ttk.Frame(self.panedwindow, width = 600, height = 400)
        self.frame2 = ttk.Frame(self.panedwindow, width = 600, height = 200)
        self.frame3 = ttk.Frame(self.panedwindow, width = 600, height = 50, relief = SUNKEN)
        self.frame4 = ttk.Frame(self.panedwindow, width = 600, height = 50, relief = SUNKEN)
        self.panedwindow.add(self.frame1, weight = 1)
        self.panedwindow.add(self.frame2, weight = 4)
        self.panedwindow.add(self.frame3, weight = 4)
        self.panedwindow.add(self.frame4, weight = 4)

        #   Frame1 instructions
        self.instructions = ttk.Label(self.frame1, text = "In order to execute the file transfer for files modified within the last 24 hours, please select an initial and destination folder. You may check eligible files for the file transfer with the 'Show Eligible Files' button after selecting an initial folder", justify = CENTER, font = ('Courier', 12))
        self.instructions.config(wraplength = 600)
        self.instructions.pack()

        #   Source/Destinations
        self.field1 = ttk.Label(self.frame3, text = "Source Folder:")
        self.field2 = ttk.Label(self.frame4, text = "Destination Folder:")
        self.field1.grid()
        self.field2.grid()
        
        #   Define buttons
        self.browse = ttk.Button(self.frame2, text = "Browse Initial Folder", command = lambda:tkinterDrillFunc.folderselect1(self))
        self.browse2 = ttk.Button(self.frame2, text = "Browse Destination Folder", command = lambda:tkinterDrillFunc.folderselect2(self))
        self.button = ttk.Button(self.frame2, text = "Show Eligible Files", command = lambda:tkinterDrillFunc.show_files(self), state = 'disabled')
        self.executer = ttk.Button(self.frame2, text = "Execute File Transfer", command = lambda:tkinterDrillFunc.the_mover(self), state = 'disabled')

        #   Placing buttons down on grid
        self.browse.grid(row = 0, column = 1, padx = 40)
        self.browse2.grid(row = 0, column = 2, padx = 40)
        self.button.grid(row = 0, column = 3, padx = 40)
        self.executer.grid(row = 0, column = 4, padx = 40)
        
        self.path = ''      
        self.destination = ''
        
if __name__=='__main__':
    root = Tk()
    ShutilUI(root).pack()
    root.mainloop()

