#!/usr/bin/python3
'''
Kind of class module
'''


def is_kind_of_class(obj, a_class):
    '''
    Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Parameters
        obj: object
        a_class: class
    '''
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
