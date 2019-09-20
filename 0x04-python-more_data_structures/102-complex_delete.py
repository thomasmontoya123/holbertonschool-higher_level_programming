#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = list(a_dictionary.keys())
    for key in [key for key in new_dictionary if a_dictionary[key] == value]:
        del a_dictionary[key]
    return a_dictionary
