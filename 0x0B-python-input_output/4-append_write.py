#!/usr/bin/python3
'''
Append to a file module
'''


def append_write(filename="", text=""):
    '''
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Parameters:
        filename: String with the nema of the file
        text: STRING TEXT
    '''
    with open(filename, encoding='utf-8', mode='a') as f:
        return f.write(str(text))
