#!/usr/bin/python3
''' lookup module'''


def lookup(obj):
    '''
    returns the list of available attributes and methods of an object
    Parameters:
        obj: object
    '''
    return list(dir(obj))
