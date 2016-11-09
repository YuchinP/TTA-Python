##Python: Ver 3.4
##Author: Yuchin Pan
##Scenario: Your employer wants a program to move all his .txt files from one folder to another
##with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
##the second Folder B. Create 4 random .txt files & put them in Folder A.

##Plan:
##- Move the files from Folder A to Folder B.
##- Print out each file path that got moved onto the shell.
##- Upon viewing Folder A after the execution, the moved files should not be there

import shutil
import os


path = os.listdir('C:\\Users\\Student\\Desktop\\Folder A')
destination = 'C:\\Users\\Student\\Desktop\\Folder B'

os.chdir('C:\\Users\\Student\\Desktop\\Folder A')

def the_mover(src, dest):
    source = 'C:\\Users\\Student\\Desktop\\Folder A'
    for files in path:
        if files.endswith(".txt"):
            shutil.move(files, destination)
            print('Text files from', source, 'have been moved to', destination)

the_mover(path, destination)
