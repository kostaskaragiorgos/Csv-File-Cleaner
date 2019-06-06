from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog

class CSV_FILECLEANER():
    def __init__(self,master):
        self.master = master
        self.master.title("CSV FILE CLEANER")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        

    
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