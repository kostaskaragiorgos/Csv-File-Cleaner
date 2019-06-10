from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog

class CSV_FILECLEANER():
    def __init__(self,master):
        self.master = master
        self.master.title("CSV FILE CLEANER")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.insertf = Button(self.master,text= "INSERT A CSV FILE",command = self.insertf)
        self.insertf.pack()
        
        self.deldup = Button(self.master,text = "Delete Duplicates",command = self.dropdp)
        self.deldup.pack()
        
        self.dropna = Button(self.master,text = "Drop Non Values",command = self.dropnv)
        self.dropna.pack()
        
        self.fixna = Button(self.master,text = "Fix Non Values ",command = self.fixnv)
        self.fixna.pack()
        
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
    
    def savef(self):
        pass
    
    def dropdp(self):
        pass
    
    def dropnv(self):
        pass
    
    def fixnv(self):
        pass
    
    def insertf(self):
        pass
    
    def aboutmenu(self):
        pass
    
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