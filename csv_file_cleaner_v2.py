"""
csv_file_cleaner_version_2
The gui class
"""
from tkinter import Tk, Menu, simpledialog
from tkinter import messagebox as msg, filedialog
import pandas as pd
from csv_cleaner import CsvCleaner, aboutmenu, helpmenu, showinformation, drop_user_input


class CsvFileCleaner(CsvCleaner):
    """ CsvFileCleaner Class"""
    def __init__(self):
        
        self.master.title("Csv-File-Cleaner")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv file",
                                   accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Save file", accelerator='Ctrl+S', command=self.save_file)
        self.file_menu.add_command(label="Close file",
                                   accelerator='Ctrl+F4', command=self.closefile)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.remove_menu = Menu(self.menu, tearoff=0)
        self.remove_menu.add_command(label="Remove Row", accelerator='Alt+R', command=self.removerow)
        self.remove_menu.add_command(label="Remove column", accelerator='Alt+B', command=self.removecol)
        self.menu.add_cascade(label="Remove", menu=self.remove_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show names of columns",
                                   accelerator='Alt+T',
                                   command=lambda: self.showinformation(self.filename,str(self.df.columns), "Column Names"))
        self.show_menu.add_command(label="Show type of columns",
                                   accelerator='Ctrl+V',
                                   command=lambda: self.showinformation(self.filename, str(list(self.df.dtypes)),"Column Types" ))
        self.show_menu.add_command(label="Show shape of the dataset",
                                   accelerator='Ctrl+F',
                                   command=lambda: self.showinformation(self.filename, self.df.shape, "Shape of the dataset"))
        self.show_menu.add_command(label="Show effected lines", accelerator='Ctrl+J', command=lambda: self.showinformation(self.filename, self.effectedlines, "Number of Effected Lines"))
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.dup_menu = Menu(self.menu, tearoff=0)
        self.dup_menu.add_command(label="Delete all duplicates",
                                  accelerator='Ctrl+T',
                                  command=lambda: self.delete_duplicates(False))
        self.dup_menu.add_command(label="Delete all duplicates except first",
                                  accelerator='Alt+F',
                                  command=lambda: self.delete_duplicates('first'))
        self.dup_menu.add_command(label="Delete all duplicates except last",
                                  accelerator='Alt+L',
                                  command=lambda: self.delete_duplicates('last'))
        self.dup_menu.add_command(label="Delete all duplicates by specific column",
                                  accelerator='Alt+C',
                                  command=lambda: self.dropspecific(False))
        self.dup_menu.add_command(label="Delete all duplicates except first by specific column",
                                  accelerator='Ctrl+B',
                                  command=lambda: self.dropspecific('first'))
        self.dup_menu.add_command(label="Delete all duplicates except last by specific column",
                                  accelerator='Ctrl+L',
                                  command=lambda: self.dropspecific('last'))
        self.dup_menu.add_command(label="Delete duplicate Columns",
                                  accelerator='Alt+P',
                                  command= self.dropduplicatecolumns)
        self.menu.add_cascade(label="Duplicates", menu=self.dup_menu)
        self.miss_v = Menu(self.menu, tearoff=0)
        self.miss_v.add_command(label="Drop columns with missing values",
                                accelerator='Alt+M',
                                command=lambda: self.drop_missing(1))
        self.miss_v.add_command(label="Drop rows with missing values",
                                accelerator='Alt+N',
                                command=lambda: self.drop_missing(0))
        self.menu.add_cascade(label="Missing Values", menu=self.miss_v)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-v>', lambda event: self.showinformation(self.filename, str(list(self.df.dtypes)), "Column Types"))
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Control-s>', lambda event: self.save_file())
        self.master.bind('<Control-F4>', lambda event: self.closefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-f>', lambda event: self.showinformation(self.filename, self.df.shape, "Shape of the dataset"))
        self.master.bind('<Alt-t>', lambda event: self.showinformation(self.filename, str(self.df.columns), "Column Names"))
        self.master.bind('<Control-j>', lambda event: self.showinformation(self.filename, self.effectedlines, "Number of Effected Lines"))
        self.master.bind('<Alt-b>', lambda event: self.removecol())
        self.master.bind('<Alt-r>', lambda event: self.removerow())
        self.master.bind('<Control-t>', lambda event: self.delete_duplicates(False))
        self.master.bind('<Alt-f>', lambda event: self.delete_duplicates('first'))
        self.master.bind('<Alt-l>', lambda event: self.delete_duplicates('last'))
        self.master.bind('<Alt-c>', lambda event: self.dropspecific(False))
        self.master.bind('<Control-b>', lambda event: self.dropspecific('first'))
        self.master.bind('<Control-l>', lambda event: self.dropspecific('last'))
        self.master.bind('<Alt-p>', lambda event: self.dropduplicatecolumns())
        self.master.bind('<Alt-m>', lambda event: self.drop_missing(1))
        self.master.bind('<Alt-n>', lambda event: self.drop_missing(0))
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

    

def main():
    """ main function """
    root = Tk()
    CsvFileCleaner(root)
    root.mainloop()
if __name__ == '__main__':
    main()
    