from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog

import pandas as pd

class CSV_FILECLEANER():
    def __init__(self,master):
        self.master = master
        self.master.title("CSV FILE CLEANER")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.pandascheck = ""
        self.filename = ""
        self.insertfb = Button(self.master,text= "INSERT A CSV FILE",command = self.insertf)
        self.insertfb.pack()

        self.deldupb = Button(self.master,text = "Delete Duplicates",command = self.dropdp)
        self.deldupb.pack()
        
        self.dropnab = Button(self.master,text = "Drop Non Values",command = self.dropnv)
        self.dropnab.pack()
        
        self.fixnab = Button(self.master,text = "Fix Non Values ",command = self.fixnv)
        self.fixnab.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert csv file",accelerator = 'Ctrl+O',command = self.insertf)
        self.file_menu.add_command(label = "Save csv file",accelerator = 'Ctrl+S',command = self.savef)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.edit_menu = Menu(self.menu,tearoff = 0)
        self.edit_menu.add_command(label  = 'Delete duplicates',accelerator = 'Ctrl + D',command = self.dropdp)
        self.edit_menu.add_command(label = 'Drop Non Values',accelerator = 'Ctrl + N',command = self.dropnv)
        self.edit_menu.add_command(label = 'Fix Non Values',accelerator = 'Ctrl + F',command = self.fixnv)
        self.menu.add_cascade(label = 'Edit',menu =self.edit_menu)
                
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        
        self.master.bind('<Control-o>',lambda event: self.insertf())
        self.master.bind('<Control-s>',lambda event: self.savef())
        
        self.master.bind('<Control-d>',lambda event: self.dropdp())
        self.master.bind('<Control-n>',lambda event: self.dropnv())
        self.master.bind('<Control-f>',lambda event: self.fixnv())
        
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        
    def savef(self):
        if (".csv" in self.filename) == False:
            msg.showerror("NO INPORT","NO CSV FILE IMPORTED")
        else:
            filenamesave = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            if ".csv" in filenamesave:
                msg.showinfo("SUCCESS","THE CSV FILE SAVED SUCCESSFULLY")
                self.pandascheck.to_csv(filenamesave,index = False)
    def dropdp(self):
        if (".csv" in self.filename) == False:
            msg.showerror("NO INPORT","NO CSV FILE IMPORTED")
        else:
            self.pandascheck.drop_duplicates(keep=False)
            msg.showinfo("DROP DUPLICATES", "DUPLICATES HAS SUCESSFULLY DROPED" )
            save = msg.askyesno("SAVE FILE","DO YOU WANT TO SAVE A NEW CSV FILE??")
            if save == True:
                filenamesave = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
                if ".csv" in filenamesave:
                    msg.showinfo("SUCCESS","THE CSV FILE SAVED SUCCESSFULLY")
                    self.pandascheck.to_csv(filenamesave,index = False)
                
         
    def dropnv(self):
        if (".csv" in self.filename) == False:
            msg.showerror("NO INPORT","NO CSV FILE IMPORTED")
        else:
            self.pandascheck.dropna
            msg.showinfo("MISSING VALUES","MISSING VALUES HAS SUCCESSFULLY REMOVED")
    
    def fixnv(self):
        if (".csv" in self.filename) == False:
            msg.showerror("NO INPORT","NO CSV FILE IMPORTED")
        else:
            na = self.pandascheck.isna()
            if 'F' in str(na):
                msg.showinfo("NO MISSING VALUES","THERE ARE NO MISSING VALUES")
            else:
                self.pandascheck.fillna(0)
                
    def insertf(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        if ".csv" in self.filename:
            self.pandascheck = pd.read_csv(self.filename)
            msg.showinfo("SUSSESSFULL INSERT","YOUR CSV FILE HAS SUCCESFULLY INSERTED")
        else:
            msg.showerror("INSERT A CSV","YOU HAVE TO INSERT A CSV FILE")
        
    def aboutmenu(self):
        msg.showinfo("About","CSV FILE CLEANER \nVersion 1.0")
        
    def helpmenu(self):
        msg.showinfo("Help" , "\t      HELP \nTHE PURPUSE OF THIS APP IS TO HELP YOU CLEAN YOUR 'MESSY' CSV FILES ")
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
def main():
    root=Tk()
    CC = CSV_FILECLEANER(root)
    root.mainloop()
    
if __name__=='__main__':
    main()