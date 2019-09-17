#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            string = string + character
    return string
