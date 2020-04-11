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
        self.file_menu.add_command(label="Insert a csv file", accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Save file", accelerator='Ctrl+S', command=self.save_file)
        self.file_menu.add_command(label="Close file", accelerator='Ctrl+F4', command=self.closefile)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.dup_menu = Menu(self.menu, tearoff=0)
        self.dup_menu.add_command(label="Delete all duplicates", accelerator='Ctrl+T', command=self.delete_duplicates)
        self.dup_menu.add_command(label="Delete all duplicates except first", accelerator='Alt+F', command=self.delete_duplicates_no_f)
        self.dup_menu.add_command(label="Delete all duplicates except last", accelerator='Alt+L', command=self.delete_duplicates_no_l)
        self.dup_menu.add_command(label="Delete all duplicates by specific column", accelerator='Alt+C', command=self.dropspecific)
        self.dup_menu.add_command(label="Delete all duplicates except first by specific column", accelerator='Ctrl+B', command=self.dropspecificfirst)
        self.dup_menu.add_command(label="Delete all duplicates except last by specific column", accelerator='Ctrl+L', command=self.dropspecificlast)
        self.menu.add_cascade(label="Duplicates", menu=self.dup_menu)
        self.miss_v = Menu(self.menu, tearoff=0)
        self.miss_v.add_command(label="Drop columns with missing values", accelerator='Alt+M', command=self.drop_missing_col)
        self.miss_v.add_command(label="Drop rows with missing values",accelerator='Alt+N', command=self.dropmissing)
        self.menu.add_cascade(label="Missing Values", menu=self.miss_v)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Control-s>', lambda event: self.save_file())
        self.master.bind('<Control-F4>', lambda event: self.closefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-t>', lambda event: self.delete_duplicates())
        self.master.bind('<Alt-f>', lambda event: self.delete_duplicates_no_f())
        self.master.bind('<Alt-l>', lambda event: self.delete_duplicates_no_l())
        self.master.bind('<Alt-c>', lambda event: self.dropspecific())
        self.master.bind('<Control-b>', lambda event: self.dropspecificfirst())
        self.master.bind('<Control-l>', lambda event: self.dropspecificlast())
        self.master.bind('<Alt-m>', lambda event: self.drop_missing_col())
        self.master.bind('<Alt-n>', lambda event: self.dropmissing())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
    def save_file(self):
        """ saves the new csv file"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            save = msg.askyesno("SAVE FILE", "DO YOU WANT TO SAVE A NEW CSV FILE??")
            if save:
                filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
                if filenamesave.endswith('.csv'):
                    msg.showinfo("SUCCESS", "THE CSV FILE SAVED SUCCESSFULLY")
                    self.df.to_csv(filenamesave, index=False)
            else:
                msg.showerror("NO SAVE", "NO FILE SAVED")
    def delete_duplicates(self):
        """ removes duplicates """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.df.drop_duplicates(keep=False, inplace=True)
            msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
    def delete_duplicates_no_l(self):
        """ removes duplicates except last """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.df.drop_duplicates(keep='last', inplace=True)
            msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
    def delete_duplicates_no_f(self):
        """ removes duplicates except first """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.df.drop_duplicates(keep='first', inplace=True)
            msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
    def dropspecific(self):
        """ drops all duplicates from a specific column """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.asked_column = simpledialog.askstring("Column", "Insert the name of the column you want to drop")
            while self.asked_column is None or self.asked_column == "":
                self.asked_column = simpledialog.askstring("Column", "Insert the name of the column you want to drop")
            if self.asked_column in self.df.columns:
                self.df.drop_duplicates(subset=self.asked_column, keep=False, inplace=True)
                msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")
    def dropspecificfirst(self):
        """ drops all duplicates except first from a specific column """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.asked_column = simpledialog.askstring("Column", "Insert the name of the column you want to drop")
            while self.asked_column is None or self.asked_column == "":
                self.asked_column = simpledialog.askstring("Column", "Insert the name of the column you want to drop")
            if self.asked_column in self.df.columns:
                self.df.drop_duplicates(subset=self.asked_column, keep='first', inplace=True)
                msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")
    def dropspecificlast(self):
        """ drops all duplicates except last from a specific column """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.asked_column = simpledialog.askstring("Column", "Insert the name of the column you want to drop")
            while self.asked_column is None or self.asked_column == "":
                self.asked_column = simpledialog.askstring("Column", "Insert the name of the column you want to drop")
            if self.asked_column in self.df.columns:
                self.df.drop_duplicates(subset=self.asked_column, keep='last', inplace=True)
                msg.showinfo("DUPLICATES", "DUPLICATES HAS SUCCESSFULLY REMOVED")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")
    def drop_missing_col(self):
        """ deletes columns with missing values"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.df.dropna(axis=1,inplace=True)
            msg.showinfo("MISSING VALUES", "COLUMNS WITH MISSING VALUES HAS SUCCESSFULLY REMOVED")
    def dropmissing(self):
        """ deletes rows with missing values"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.df.dropna(inplace=True)
            msg.showinfo("MISSING VALUES", "ROWS WITH MISSING VALUES HAS SUCCESSFULLY REMOVED")
    def closefile(self):
        """ closes the csv file """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.filename = ""
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")
    def insertfile(self):
        """ inserts the csv file """
        if ".csv" in self.filename:
            msg.showerror("ERROR", "A CSV FILE IS ALREADY OPEN")
        else:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            if self.filename.endswith('.csv'):
                self.df = pd.read_csv(self.filename)
                msg.showinfo("SUSSESSFULL INSERT", "YOUR CSV FILE HAS SUCCESFULLY INSERTED")
            else:
                msg.showerror("INSERT A CSV", "YOU HAVE TO INSERT A CSV FILE")
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