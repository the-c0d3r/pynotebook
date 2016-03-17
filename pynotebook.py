import os
import time

__author__ = "the-c0d3r"

class menu:
    """The main menu for the program"""
    def __init__(self):
        pass

class note:
    """The note object which needs to have certain information attached"""
    def __init__(self,data):
        """Accepts Data as note content"""
        self.text = data

    def add_info(self):
        """Adds the basic timestamp info to the note content"""
        self.date_time = time.strftime("%H:%M %A - %d/%m/%Y")
        self.text = "|{}|\n".format(self.date_time) + self.text
        # Adds the date/time stamp

class notebook:
    """The notebook object which handles writing and reading..."""
    def __init__(self,filename=None):
        """Accepts filename argument"""
        if filename == None:
            self.filename = input("Enter notebook name : ")
        else:
            self.filename = filename

    def write_note(self,note):
        try:
            with open(self.filename,"a") as nb:
                nb.write(note)
        except IOError:
            self.catch_exception()

    def exists(self):
        """Check if the defined notebook exist"""
        return os.path.exists(self.filename)
    
    def create_notebook(self):
        """Creates & !Overwrites! the file"""
        try:
            open(self.filename,'w').close()
        except IOError:
            print("[-] Permission error")

    def read_notebook(self):
        try:
            data = [line for line in open(self.filename,"r").readlines()]
            if len(data) == 0:
                print("[-] Notebook is empty")
            else:
                return data
        except IOError:
            self.catch_exception()

    def catch_exeption(self):
        if self.exists():
            print("[-] No Read Permission for {}".format(self.filename))
        elif not self.exists():
            print("[-] Notebook {} didn't exist!".format(self.filename))                 
