
import tkinter
from tkinter import *

import webbrowser
new=2;


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width= False, height = False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Website Demo')
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()
    
        
        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica",16), fg = 'black', bg='lightgray')
        self.lblFName.grid(row=0, column =0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica",16), fg = 'black', bg='lightgray')
        self.lblLName.grid(row=1, column =0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica",16), fg = 'black', bg='lightgray')
        self.lblDisplay.grid(row=3, column =1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica",16), fg = 'black', bg='lightblue')
        self.txtFName.grid(row=0, column =1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica",16), fg = 'black', bg='lightblue')
        self.txtLName.grid(row=1, column =1, padx=(30,0), pady=(30,0))
       
        self.btnSubmit = Button(self.master, text="Submit", width = 10, height = 2, command=self.submit)
        self.btnSubmit.grid(row=2, column =1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width = 10, height = 2, command=self.cancel)
        self.btnCancel.grid(row=2, column =1, padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        webbrowser.open("demofile2.html",new=new);
        f = open("demofile2.html", "w")
        f.write("Hey {} {},Stay tuned for our amazing summer sale!".format(fn,ln))
        f.close()

    #open and read the file after the appending:
      
    def cancel(self):
       self.master.destroy()    



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
