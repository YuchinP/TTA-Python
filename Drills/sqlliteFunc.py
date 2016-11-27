import os
import shutil
from datetime import *
from tkinter import *
from tkinter import ttk
import sqlite3

#   The UI and Main Python
import sqlliteDrill

#   Create the Database if it doesn't already exist for the timestamps
def create_db(self):
    conn = sqlite3.connect('timestamp.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_timestamp( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    tsp TIMESTAMP \
    );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('timestamp.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_timestamp (tsp) VALUES (?)""",('Never',))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_timestamp""")
    count = cur.fetchone()[0]
    return cur,count

def timer(self):
    conn = sqlite3.connect('timestamp.db')
    with conn:
        cursor = conn.cursor()
        recent = cursor.execute("SELECT tsp FROM tbl_timestamp ORDER BY tsp DESC LIMIT 1").fetchone()[0]
        print (str(recent))
        self.LbStamp.config(text = "Last File Check at : " + str(recent))
        conn.commit()
    conn.close()    



#   Defines the browsing and selecting for the folders
def folderselect1(self):
    Sel_directory1 = filedialog.askdirectory()
    print(Sel_directory1)
    self.path = Sel_directory1
    file_activator(self) #Activates the Eligible Files button
    execute_activator(self) #Checks one of two requirements to activate the execute files button
    show_source(self) # Displays the Source path    
        
def folderselect2(self): 
    Sel_directory2 = filedialog.askdirectory()
    print(Sel_directory2)
    self.destination = Sel_directory2
    execute_activator(self)
    show_destination(self)

#   Gets the converted time of last modification on files             
def get_time(self,files):
    files = os.path.join(self.path, files)
    mtime = os.path.getmtime(files)
    ntime = datetime.fromtimestamp(mtime)
    now = datetime.now()
    tdelta = now - ntime
    ntimer = tdelta.total_seconds()
    return ntimer

#   This defines and will show the files modified within the last 24 hours
def show_files(self):
    con_prompt(self) #Opens a prompt that tells the files eligible
    for files in os.listdir(self.path):
        if files.endswith('.txt'):
            get_time(self,files)
            if get_time(self,files) < 86400:
                print (files)
                output = files
                self.files = ttk.Label(self.window, text = output, justify = CENTER, font = ('Courier', 13, 'bold')).pack()
            else:
                print('Ineligible')

#   The main file mover         
def the_mover(self):
    source = self.path
    con_prompt(self)
    for files in os.listdir(self.path):
        files = os.path.join(source, files)
        if files.endswith('.txt'):
            get_time(self,files)
            if get_time(self,files) < 86400:
                shutil.move(files, self.destination)
                confirmation = 'Text files from', source, 'have been moved to', self.destination
                self.files = ttk.Label(self.window, text = confirmation, justify = CENTER, font = ('Courier', 13, 'bold'),wraplength = 600).pack()
                print('Text files from', source, 'have been moved to', self.destination)
                timestamp = str(datetime.now()) 
                conn = sqlite3.connect('timestamp.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO tbl_timestamp (tsp) VALUES (?)", (datetime.now(),))
                    cursor.execute("DELETE FROM tbl_timestamp WHERE tsp = 'Never'")
                    recent2 = cursor.execute("SELECT tsp FROM tbl_timestamp ORDER BY tsp DESC LIMIT 1").fetchone()
                    print (str(recent2))
                    self.LbStamp.config(text = "Last File Check at : " + str(recent2))
                    conn.commit()
                conn.close()                             
            else:
                print('finished')

#   Activates the Eligible files button if a initial folder is selected
def file_activator(self):
    if self.path != '':
        self.button.config(state='normal')

#   Activates the execute button if both folders are selected
def execute_activator(self):
    if self.path != '' and self.destination != '':
        self.executer.config(state='normal')
    else:
        self.executer.config(state='disabled')

#   Creates a popup
def con_prompt(self):
    self.window = Toplevel(self.panedwindow)
    self.window.resizable(True,True)
    self.window.geometry('600x600+100+100')

#   Shows the paths to the selected folders
def show_source(self):
    self.field1.config(text = "Source Folder: " + self.path)

def show_destination(self):
    self.field2.config(text = "Destination Folder: " + self.destination)
    

if __name__ == "__main__":
    pass
