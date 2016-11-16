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
    
        
def folderselect2(self):
    Sel_directory2 = filedialog.askdirectory()
    print(Sel_directory2)
    destination = Sel_directory2
             
def get_time(self,files):
    os.chdir(self.path)
    mtime = os.path.getmtime(files)
    ntime = datetime.fromtimestamp(mtime)
    now = datetime.now()
    tdelta = now - ntime
    ntimer = tdelta.total_seconds()
    return ntimer

def show_files(self):
    source = self.path
    for files in os.listdir(self.path):
        if files.endswith('.txt'):
            get_time(self,files)
            if get_time(self,files) > 86400:
                print (files)
            else:
               print('ineligible')
        

def the_mover(src, dest):
    source = path
    for files in path:
        if files.endswith('.txt'):
            get_time(files)
            if get_time(files) > 86400:
                shutil.move(files, destination)
                print('Text files from', source, 'have been moved to', destination)
            else:
                print('finished')
        else:
            print('none')



if __name__ == "__main__":
    pass
