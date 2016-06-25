import time
import json


class Note:
    """ A note class for storing separate notes as objects """
    def __init__(self, title, body, info, filename, notebook):
        self.title    = title
        self.body     = body
        self.info     = info
        self.filename = filename
        self.notebook = notebook

    def __str__(self):
        """ To print title when executing print obj """
        return self.filename

    def save(self):
        if self.title == "":
            print("Title is empty!")
            return
        elif self.body == "":
            print("Body is empty!")
            return
        else:
            self.info = self.get_timestamp()
            # Calls the writing function later

    def get_timestamp(self):
        """ Returns the current timestamp """
        # Time format = Hour:Minute AM/PM - Days/Month/Year
        return time.strftime("%H:%M %p - %d/%m/%Y")

    def get_json(self):
        """ Returns a JSON format data, to write"""
        data = {
            "title"    : self.title,
            "body"     : self.body,
            "info"     : self.info,
            "notebook" : self.notebook
        }
        return json.loads(str(data))
