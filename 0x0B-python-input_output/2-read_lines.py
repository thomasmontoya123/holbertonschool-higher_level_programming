#!/usr/bin/python3
'''
Read n lines module
'''


def read_lines(filename="", nb_lines=0):
    '''
    Reads n lines of a text file (UTF8) and prints it to stdout

    Parameters:
        filename: String with the nema of the file
        nb_lines: number of lines to be read
    '''
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            read_data = f.read()
            print(read_data, end="")
        else:
            line_count = 0
            for line in f:
                line_count += 1
                print(line, end="")
                if line_count == nb_lines:
                    break
