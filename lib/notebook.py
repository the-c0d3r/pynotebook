import os
import json
from lib.note import Note

class Notebook:
    """ A notebook class responsible for storing notes """
    def __init__(self, folderpath):
        self.name = ""
        self.dir = folderpath
        self.readnotes()
        self.notecount = len(self.notes)

    def readnotes(self):
        """ Reads the note files, and create Note objects """
        self.notefiles = os.listdir(self.dir)
        # self.notefiles contains a list of notefiles under the notebook directory
        self.notes = []
        # To collect "Note" objects

        for n in self.notefiles:
            with open(str(self.dir + os.path.sep + n), 'r') as raw:
                json_data = json.load(raw)
                title     = json_data['title']
                body      = json_data['body']
                info      = json_data['info']
                filename  = n
                notebook  = json_data['notebook']

                # creation of objects
                NoteObj          = Note(title, body, info, filename, notebook)
                self.notes.append(NoteObj)





"""
TODO
----
0x1 Note creation
0x2 Note update




Notebook (FOLDER)
|----> Note1.json
       |-----> title, body, info, filename, notebook
|----> Note2.json
"""
