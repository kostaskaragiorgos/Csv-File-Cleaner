"""
csv_cleaner_version_2
"""
from tkinter import  simpledialog
from tkinter import messagebox as msg, filedialog
import pandas as pd
import numpy as np



def helpmenu():
    """ help menu funciton """
    msg.showinfo("Help", "THE PURPUSE OF THIS APP IS TO HELP YOU CLEAN YOUR 'MESSY' CSV FILES ")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "CSV FILE CLEANER \nVersion 2.0")


def showinformation(filename="", typeofinfo=None, messagetitle=None):
    """
    pops up an informative window based on input
    Args:
        filename: the name of the file
        typeofinfo: the desired info
        messagetitle: the window title
    """
    if ".csv" not in filename:
        msg.showerror("ERROR", "NO CSV IMPORTED")
    else:
        msg.showinfo(title=str(messagetitle), message=str(typeofinfo))

def savechanges(dataframe, effectedlines, filename):
    """saves the file after changes.
    Args:
        dataframe: the dataframe of the file
        effectedlines: the number of effected lines
        filename: the name of the file
    """
    if effectedlines > 0:
        ans = msg.askquestion("SAVE CHANGES", "DO YOU WANT TO SAVE THE CHANGES BEFORE CLOSE???")
        if ans:
            dataframe.to_csv(filename)


def drop_user_input(dt="Integer", titlel="", promptl="", minvalue=0, maxvalue=0):
    """
Saves the user input
Args:
dt: the type of the  dialog(input)
dialogtype: the dialogtypr
type: row or column to delete
title: the title of the window
prompt: the message of the window
minvalue: the lowest possible input value
maxvalue: the biggest possible input value
Returns:
    asked: the user input
"""
    asked = ""
    while asked is None or asked == "":
        if dt == "Integer":
            asked = simpledialog.askinteger(title=titlel,
                                            prompt=promptl,
                                            minvalue=minvalue,
                                            maxvalue=maxvalue)
        else:
            asked = simpledialog.askstring(title=titlel, prompt=promptl)
    return asked

class CsvCleaner():

    """csv file cleaner class"""
    def __init__(self, master):
        self.effectedlines = 0
        self.filename = ""
        self.df = pd.DataFrame()
        self.master = master

    def removecol(self):
        """ removes a column from the file"""
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            asked = drop_user_input(titlel="Column", dt="String",
                                    promptl="Columns"+str(self.df.columns.values.tolist())+
                                    "\nInsert the name of the column"+
                                    "you want to drop")
            if asked in self.df.columns:
                self.df.drop(asked, axis=1, inplace=True)
                msg.showinfo("SUCCESS",
                             "COLUMN " +
                             asked + " HAS SUCCESSFULLY REMOVED.\n THERE ARE "+
                             str(self.df.shape[1]) +"COLUMNS REMAINING")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")

    def removerow(self):
        """ removes a row from the file"""
        if ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            row_r = drop_user_input(titlel="Rows",
                                    dt="Integer",
                                    promptl="Enter the number of row to delete",
                                    minvalue=0, maxvalue=self.df.shape[0])
            original = len(self.df)
            self.df.drop(self.df.index[row_r], inplace=True)
            self.effectedlines += abs(original - len(self.df))
            msg.showinfo("SUCCESS", "ROW HAS SUCCESSFULLY BEEN REMOVED \nTHERE ARE " +
                         str(self.effectedlines) + " EFFECTED LINES.\nTHERE ARE " +
                         str(len(self.df)) + " REMAINING LINES")

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
        if ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV TO SAVE")
        else:
            save = msg.askyesno("SAVE FILE", "DO YOU WANT TO SAVE A NEW CSV FILE??")
            self.savefunction(save)
    def delete_duplicates(self, keep):
        """ removes duplicates """
        if  ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            original = len(self.df)
            self.df.drop_duplicates(keep=keep, inplace=True)
            self.effectedlines = abs(original - len(self.df))
            msg.showinfo("DUPLICATES", "DUPLICATES HAVE SUCCESSFULLY REMOVED \nTHERE ARE " +
                         str(self.effectedlines) + " EFFECTED LINES.\nTHERE ARE " +
                         str(len(self.df)) + " REMAINING LINES")

    def dropduplicatecolumns(self):
        """removes the duplicate columns"""
        if  ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            self.df = self.df.loc[:, ~self.df.columns.duplicated()]
            msg.showinfo("DUPLICATES",
                         "DUPLICATE COLUMNS HAVE  SUCCESSFULLY REMOVED\n THERE ARE "
                         + str(self.df.shape[1])+
                         " REMAINING COLUMNS")

    def dropspecific(self, keep):
        """ drops all duplicates from a specific column """
        if ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            asked = drop_user_input(titlel="Column",
                                    promptl="Columns"+str(self.df.columns.values.tolist())+
                                    "\nInsert the name of the column"+
                                    "you want to drop", dt="String")
            if asked in self.df.columns:
                original = len(self.df)
                self.df.drop_duplicates(subset=asked, keep=keep, inplace=True)
                self.effectedlines += abs(original - len(self.df))
                msg.showinfo("DUPLICATES",
                             "DUPLICATES HAVE SUCCESSFULLY REMOVED\nTHERE ARE " +
                             str(self.effectedlines) +
                             " EFFECTED LINES.\nTHERE ARE " +
                             str(len(self.df)) + " REMAINING LINES")
            else:
                msg.showerror("ERROR", "THERE IS NO SUCH A COLUMN")
    
    def replace_nanvalues(self, value):
        if ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            self.df.replace(to_replace = np.nan, value = value, inplace=True)

    def drop_missing(self, axis):
        """ deletes columns or rows with missing values"""
        if ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV IMPORTED")
        else:
            original = len(self.df)
            self.df.dropna(axis=axis, inplace=True)
            self.effectedlines += abs(original-self.effectedlines)
            msg.showinfo("MISSING VALUES",
                         "MISSING VALUES HAS SUCCESSFULLY REMOVED\nTHERE ARE "
                         +str(self.effectedlines)+ " EFFECTED LINES\nTHERE ARE " +
                         str(len(self.df)) + " REMAINING LINES")
    def closefile(self):
        """ closes the csv file """
        if ".csv" not in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            savechanges(self.df, self.effectedlines, self.filename)
            self.filename = ""
            self.effectedlines = 0
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
