from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import tkinter as tk
import time
import shutil
import os
from datetime import datetime, timedelta


def Createwindow():
	
	
	root.sourceText = Entry(root, width = 50,textvariable = src)
	root.sourceText.grid(row = 1, column = 1,pady = 5, padx = 5,columnspan = 2)
	
	source_browseButton = Button(root, text ="Browse",command = SourceBrowse, width = 15)
	source_browseButton.grid(row = 1, column = 0,pady = 5, padx = 5)
	
	
	root.destinationText = Entry(root, width = 50,textvariable = dst)
	root.destinationText.grid(row = 2, column = 1,pady = 5, padx = 5,columnspan = 2)
	
	dest_browseButton = Button(root, text ="Browse",command = DestinationBrowse, width = 15)
	dest_browseButton.grid(row = 2, column = 0,pady = 5, padx = 5)
	
	checkButton = Button(root, text ="Check for Files",command = check, width = 15)
	checkButton.grid(row = 3, column = 0,pady = 5, padx = 5)


SECONDS_IN_DAY = 24 * 60 * 60	



def SourceBrowse():
    	src = filedialog.askdirectory(initialdir ="/")
    	root.sourceText.insert('1', src)
def DestinationBrowse():
        dst  = filedialog.askdirectory(initialdir ="/")
        root.destinationText.insert('1', dst )

def last_mod_time(fname):
    return datetime.fromtimestamp(os.path.getmtime(fname))

def check():
    before = datetime.now() - timedelta(seconds=SECONDS_IN_DAY)
    src_path = src.get()
    dst_path = dst.get()
    
    

    for fname in os.listdir(src_path):
        src_fname = os.path.join(src_path, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(dst_path, fname)
            shutil.move(src_fname, dst_fname)
        

    

        



root = tk.Tk()
root.geometry("830x120")
root.title("Copy-Move GUI")
root.config(background = "lightgray")
src = StringVar()
dst = StringVar()
def submit():
    src_path = src.get()
    dst_path = dst.get()
Createwindow()
root.mainloop()
