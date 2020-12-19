"""
csv_file_cleaner_version_2
"""
from tkinter import Tk, Menu, simpledialog
from tkinter import messagebox as msg, filedialog
import pandas as pd
def helpmenu():
    """ help menu funciton """
    msg.showinfo("Help", "THE PURPUSE OF THIS APP IS TO HELP YOU CLEAN YOUR 'MESSY' CSV FILES ")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "CSV FILE CLEANER \nVersion 2.0")
class CsvFileCleaner():
    """ CsvFileCleaner Class"""
    def __init__(self, master):
        self.master = master
        self.master.title("Csv-File-Cleaner")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.filename = ""
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
        self.remove_menu.add_command(label="Remove Row")
        self.remove_menu.add_command(label="Remove column", accelerator='Alt+B', command=self.removecol)
        self.menu.add_cascade(label="Remove", menu=self.remove_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show names of columns",
                                   accelerator='Alt+T',
                                   command=self.showcol)
        self.show_menu.add_command(label="Show type of columns",
                                   accelerator='Ctrl+V',
                                   command=self.showtypeofcolumns)
        self.show_menu.add_command(label="Show shape of the dataset",
                                   accelerator='Ctrl+F',
                                   command=self.showshape)
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
        self.master.bind('<Control-v>', lambda event: self.showtypeofcolumns())
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Control-s>', lambda event: self.save_file())
        self.master.bind('<Control-F4>', lambda event: self.closefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-f>', lambda event: self.showshape())
        self.master.bind('<Alt-t>', lambda event: self.showcol())
        self.master.bind('<Alt-b>', lambda event: self.removecol())
        self.master.bind('<Control-t>', lambda event: self.delete_duplicates(False))
        self.master.bind('<Alt-f>', lambda event: self.delete_duplicates('first'))
        self.master.bind('<Alt-l>', lambda event: self.delete_duplicates('last'))
        self.master.bind('<Alt-c>', lambda event: self.dropspecific(False))
        self.master.bind('<Control-b>', lambda event: self.dropspecific('first'))
        self.master.bind('<Control-l>', lambda event: self.dropspecific('last'))
        self.master.bind('<Alt-m>', lambda event: self.drop_missing(1))
        self.master.bind('<Alt-n>', lambda event: self.drop_missing(0))
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
    
    def removecol(self):
        """ removes a column from the file"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            self.drop_specific_user_input()
            if self.asked_column in self.df.columns:
                self.df.drop(self.asked_column, axis=1, inplace=True)
                msg.showinfo("SUCCESS", "COLUMN HAS SUCCESSFULLY REMOVED")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")
    def showshape(self):
        """ shows the name of the columns"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            msg.showinfo("Shape of the dataset", str(self.df.shape))
    
    def showtypeofcolumns(self):
        """ shows the types of the columns"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            msg.showinfo("Column Types", str(list(self.df.dtypes)))

        
    def showcol(self):
        """ shows the name of the columns"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            msg.showinfo("Column Names", str(self.df.columns))

    def checkifcsv(self, filenamesave):
        """ checks if the inserted file is a csv file """
        if filenamesave.endswith('.csv'):
            msg.showinfo("SUCCESS", "THE CSV FILE SAVED SUCCESSFULLY")
            self.df.to_csv(filenamesave, index=False)
        else:
            msg.showerror("NO SAVE", "FILE EXTENSION NEEDS TO BE .CSV")
    def savefunction(self, save):
        """ saves the csv """
        if save:
            filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                        filetypes=(("csv files", "*.csv"),
                                                                   ("all files", "*.*")))
            self.checkifcsv(filenamesave)
        else:
            msg.showerror("NO SAVE", "NO FILE SAVED")
    def save_file(self):
        """ saves the new csv file"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO SAVE")
        else:
            save = msg.askyesno("SAVE FILE", "DO YOU WANT TO SAVE A NEW CSV FILE??")
            self.savefunction(save)
    def delete_duplicates(self, keep):
        """ removes duplicates """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            self.df.drop_duplicates(keep=keep, inplace=True)
            msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
    def drop_specific_user_input(self):
        """ user enters the name of the column to drop"""
        self.asked_column = simpledialog.askstring("Column",
                                                   "Columns"+str(self.df.columns.values.tolist())+
                                                   "\nInsert the name of the column"+
                                                   "you want to drop")
        while self.asked_column is None or self.asked_column == "":
            self.asked_column = simpledialog.askstring("Column",
                                                       "Columns"
                                                       +str(self.df.columns.values.tolist())+
                                                       "\nInsert the name of the column"+
                                                       "you want to drop")
    def dropspecific(self, keep):
        """ drops all duplicates from a specific column """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            self.drop_specific_user_input()          
            if self.asked_column in self.df.columns:
                self.df.drop_duplicates(subset=self.asked_column, keep=keep, inplace=True)
                msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")
    def drop_missing(self, axis):
        """ deletes columns or rows with missing values"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            self.df.dropna(axis=axis, inplace=True)
            msg.showinfo("MISSING VALUES", "MISSING VALUES HAS SUCCESSFULLY REMOVED")
    def closefile(self):
        """ closes the csv file """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.filename = ""
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")
    def checkfile(self):
        """ checks if inserted file is a csv """
        if self.filename.endswith('.csv'):
            msg.showinfo("SUCCESSFUL INSERTION", "YOUR CSV FILE HAS SUCCESFULLY INSERTED")
            if msg.askyesno("COPY FILE", "DO YOU WANT TO CREATE A COPY FILE TO CLEAN?\n"+
                            "\n Yes: Creates and uses a copy of the inserted file\n"+
                            "No: Uses the inserted file"):
                self.df = pd.read_csv(self.filename)
                fstr = self.filename.split("/")[-1]
                self.df.to_csv('copy'+fstr)
                self.df = pd.read_csv('copy'+fstr)
            else:
                self.df = pd.read_csv(self.filename)
        else:
            msg.showerror("INSERT A CSV", "YOU HAVE TO INSERT A CSV FILE")
    def insertfile(self):
        """ inserts the csv file """
        if ".csv" in self.filename:
            msg.showerror("ERROR", "A CSV FILE IS ALREADY OPEN")
        else:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"),
                                                                  ("all files", "*.*")))
            self.checkfile()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    CsvFileCleaner(root)
    root.mainloop()
if __name__ == '__main__':
    main()
    