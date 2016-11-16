from tkinter import *
from tkinter import ttk

import tkinterDrillFunc


class ShutilUI(Frame):
    
    def __init__(self,root):

        Frame.__init__(self,root)

        #   Title of the UI
        label = ttk.Label(root, text = "File Moving UI", justify = CENTER, font = ('Courier', 13, 'bold'))
        label.pack()

        #   Creation of the paned window
        panedwindow = ttk.Panedwindow(root, orient = VERTICAL)
        panedwindow.pack(fill = BOTH, expand = True)
        frame1 = ttk.Frame(panedwindow, width = 600, height = 400, relief = SUNKEN)
        frame2 = ttk.Frame(panedwindow, width = 600, height = 200, relief = SUNKEN)
        panedwindow.add(frame1, weight = 1)
        panedwindow.add(frame2, weight = 4)
        
        #   Define buttons
        browse = ttk.Button(frame2, text = "Browse Initial Folder", command = lambda:tkinterDrillFunc.folderselect1(self))
        browse2 = ttk.Button(frame2, text = "Browse Destination Folder", command = lambda:tkinterDrillFunc.folderselect2(self))
        button = ttk.Button(frame2, text = "Show Eligible Files", command = lambda:tkinterDrillFunc.show_files(self))
        executer = ttk.Button(frame2, text = "Execute File Transfer", command = lambda:tkinterDrillFunc.the_mover(self))


        #   Placing buttons down on grid
        browse.grid(row = 0, column = 1, padx = 40)
        browse2.grid(row = 0, column = 2, padx = 40)
        button.grid(row = 0, column = 3, padx = 40)
        executer.grid(row = 0, column = 4, padx = 40)

        
        path = ''

        
if __name__=='__main__':
    root = Tk()
    ShutilUI(root).pack()
    root.mainloop()

