"""
https://github.com/faif/python-patterns/blob/master/patterns/creational/factory.py
"""
from __future__ import unicode_literals
from __future__ import print_function

class GreekLocalizer(object):
    
    def __init__(self):
        self.translations = {"dog": "+++", "cat": "+++"}
    
    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer(object):
    def localize(self, msg):
        return msg

class JapaneseLocalizer(object):

    def __init__(self):
        self.translations = {"dog": "Inu", "cat": "Neko"}
    
    def localize(self, msg):
        return self.translations.get(msg, msg)

def get_localizer(language = "English"):
    """ factory """
    localizers = {
        "English" : EnglishLocalizer,
        "Greek" : GreekLocalizer,
        "Japanese" : JapaneseLocalizer
    }
    return localizers[language]()

def main():
    e, g, j = get_localizer(language="English"), get_localizer(language="Greek"), get_localizer(language="Japanese")
    
    for msg in "dog parrot cat bear".split():
        print(e.localize(msg), g.localize(msg), j.localize(msg))

if __name__ == "__main__":
    main()