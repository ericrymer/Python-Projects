from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width= True, height = True)
        self.master.geometry('{}x{}'.format(600,300))
        self.master.title('Check File!')
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()
    
        
        self.btnBrowse = Button(self.master, text="Browse", width = 15, height = 1, command=self.openFile)
        self.btnBrowse.grid(row=0, column =0, padx=(20,0), pady=(30,0))

        self.btnBrowse1 = Button(self.master, text="Browse", width = 15, height = 1, command=self.openFile)
        self.btnBrowse1.grid(row=1, column =0, padx=(20,0), pady=(30,0))


        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica",16), fg = 'black', bg='white')
        self.txtFName.grid(row=0, column =1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica",16), fg = 'black', bg='white')
        self.txtLName.grid(row=1, column =1, padx=(30,0), pady=(30,0))
       
        self.btnClose = Button(self.master, text="Close Program", width = 15, height = 1, command=self.cancel)
        self.btnClose.grid(row=2, column =1, padx=(20,0), pady=(30,0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for Files", width = 15, height = 1, command=self.check)
        self.btnCheck.grid(row=2, column =0, padx=(20,0), pady=(30,0), sticky=W)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        
    def cancel(self):
       self.master.destroy()

           
    def check(self):
       self.master.destroy()
  
       
    # open a file box window 
    # when we want to select a file
    
    def openFile(self):
        self.filename= fd.askopenfilename()
        showinfo(
        title='Selected File',
        message=self.filename)
       




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
