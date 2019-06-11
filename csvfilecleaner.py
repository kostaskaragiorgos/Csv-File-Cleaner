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
        self.insertfb = Button(self.master,text= "INSERT A CSV FILE",command = self.insertf)
        self.insertfb.pack()

        self.deldupb = Button(self.master,text = "Delete Duplicates",command = self.dropdp)
        self.deldupb.pack()
        self.deldupb.configure(state = "disable")
        
        self.dropnab = Button(self.master,text = "Drop Non Values",command = self.dropnv)
        self.dropnab.pack()
        self.dropnab.configure(state="disable")
        
        self.fixnab = Button(self.master,text = "Fix Non Values ",command = self.fixnv)
        self.fixnab.pack()
        self.fixnab.configure(state = "disable")
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Insert csv file",accelerator = 'Ctrl+O',command = self.insertf)
        self.file_menu.add_command(label = "Save csv file",accelerator = 'Ctrl+S',command = self.savef)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.edit_menu = Menu(self.menu,tearoff = 0)
        self.edit_menu.add_command(label  = 'Delete duplicates',accelerator = 'Ctrl + D',command = self.dropdp)
        self.edit_menu.add_command(label = 'Drop Non Values',accelerator = 'Ctrl + N',command = self.dropnv)
        self.edit_menu.add_command(label = 'Fix Non Values ',accelerator = 'Ctrl + F',command = self.fixnv)
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
        pass
    
    def dropdp(self):
        self.pandascheck.drop_duplicates(keep=False)
        msg.showinfo("DROP DUPLICATES", "DUPLICATES HAS SUCESSFULLY DROPED" )
        
    def dropnv(self):
        pass
    
    def fixnv(self):
        pass
    
    def insertf(self):
        filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        if ".csv" in filename:
            self.pandascheck = pd.read_csv(filename)
            msg.showinfo("SUSSESSFULL INSERT","YOUR CSV FILE HAS SUCCESFULLY INSERTED")
            self.fixnab.configure(state = "normal")
            self.dropnab.configure(state= "normal")
            self.deldupb.configure(state = "normal")
            self.insertfb.configure(state = "disable")
        else:
            msg.showerror("INSERT A CSV","YOU HAVE TO INSERT A CSV FILE")
        
    def aboutmenu(self):
        msg.showinfo("About","CSV FILE CLEANER \nVersion 1.0")
        
    def helpmenu(self):
        pass
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
def main():
    root=Tk()
    CC = CSV_FILECLEANER(root)
    root.mainloop()
    
if __name__=='__main__':
    main()