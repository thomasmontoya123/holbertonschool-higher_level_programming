#!/usr/bin/python3
'''
Read file modue
'''


def read_file(filename=""):
    '''
    Reads a text file (UTF8) and prints it to stdout

    Parameters:
        filename: String with the nema of the file
    '''
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end="")
