#!/usr/bin/python3
'''
Number of lines module
'''


def number_of_lines(filename=""):
    '''
    Returns the number of lines of a text file

    Parameters:
        filename: String with the nema of the file
    '''
    line_counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line_counter += 1
    return line_counter
