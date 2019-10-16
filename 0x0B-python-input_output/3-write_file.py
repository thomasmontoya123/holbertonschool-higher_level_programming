#!/usr/bin/python3
'''
Writo into a file module
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file (UTF8)
    and returns the number of characters written

    Parameters:
        filename: String with the nema of the file
        text: STRING TEXT
    '''
    with open(filename, encoding='utf-8', mode='w') as f:
        return f.write(str(text))
