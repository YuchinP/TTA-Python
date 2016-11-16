import os
import shutil
from datetime import *
from tkinter import *
from tkinter import ttk

import tkinterDrill



def folderselect1(self):
    Sel_directory1 = filedialog.askdirectory()
    print(Sel_directory1)
    self.path = Sel_directory1
    file_activator(self)
    execute_activator(self)
    show_source(self)
    
        
def folderselect2(self):
    Sel_directory2 = filedialog.askdirectory()
    print(Sel_directory2)
    self.destination = Sel_directory2
    execute_activator(self)
    show_destination(self)
             
def get_time(self,files):
    os.chdir(self.path)
    mtime = os.path.getmtime(files)
    ntime = datetime.fromtimestamp(mtime)
    now = datetime.now()
    tdelta = now - ntime
    ntimer = tdelta.total_seconds()
    return ntimer

def show_files(self):
    con_prompt(self)
    for files in os.listdir(self.path):
        if files.endswith('.txt'):
            get_time(self,files)
            if get_time(self,files) < 86400:
                print (files)
                output = files
                self.files = ttk.Label(self.window, text = output, justify = CENTER, font = ('Courier', 13, 'bold')).pack()
            else:
                print('Ineligible')

        
def the_mover(self):
    source = self.path
    con_prompt(self)
    for files in os.listdir(self.path):
        if files.endswith('.txt'):
            get_time(self,files)
            if get_time(self,files) < 86400:
                shutil.move(files, self.destination)
                confirmation = 'Text files from', source, 'have been moved to', self.destination
                self.files = ttk.Label(self.window, text = confirmation, justify = CENTER, font = ('Courier', 13, 'bold'),wraplength = 600).pack()
                print('Text files from', source, 'have been moved to', self.destination)
            else:
                print('finished')
        else:
            print('none')

def file_activator(self):
    if self.path != '':
        self.button.config(state='normal')

def execute_activator(self):
    if self.path != '' and self.destination != '':
        self.executer.config(state='normal')
    else:
        self.executer.config(state='disabled')

def con_prompt(self):
    self.window = Toplevel(self.panedwindow)
    self.window.resizable(True,True)
    self.window.geometry('600x600+100+100')

def show_source(self):
    self.field1.config(text = "Source Folder: " + self.path)

def show_destination(self):
    self.field2.config(text = "Destination Folder: " + self.destination)
    

if __name__ == "__main__":
    pass
