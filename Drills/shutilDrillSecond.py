import os
import shutil
from datetime import *


path = os.listdir('C:\\Users\\Student\\Desktop\\Folder A')
destination = 'C:\\Users\\Student\\Desktop\\Folder B'

os.chdir('C:\\Users\\Student\\Desktop\\Folder A')

        
def get_time(files):
    mtime = os.path.getmtime(files)
    ntime = datetime.fromtimestamp(mtime)
    now = datetime.now()
    tdelta = now - ntime
    ntimer = tdelta.total_seconds()
    return ntimer


def the_mover(src, dest):
    source = 'C:\\Users\\Student\\Desktop\\Folder A'
    for files in path:
        if files.endswith('.txt'):
            get_time(files)
            if get_time(files) < 86400:
                shutil.move(files, destination)
                print('Text files from', source, 'have been moved to', destination)
            else:
                print('finished')
        else:
            print('none')
the_mover(path, destination)



