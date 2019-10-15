#!/usr/bin/python3
'''
same class module
'''


def is_same_class(obj, a_class):
    '''
    Returns True if the object is exactly an
    instance of the specified class ; otherwise False.

    Parameters:
        obj: object
        a_class: class
    '''
    return type(obj) is a_class
