#!/usr/bin/python3
'''
Search and update module
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Inserts a line of text to a file,
    after each line containing a specific string (see example)
    '''
    with open(filename, 'r') as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, 'w') as f:
        f.write(new_text)
