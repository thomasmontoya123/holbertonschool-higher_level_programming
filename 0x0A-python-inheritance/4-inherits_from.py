#!/usr/bin/python3
'''
Inherits from module
'''


def inherits_from(obj, a_class):
    '''
    returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.

    Parameters
        obj: object
        a_class: class
    '''
    return isinstance(obj, a_class) is True and type(obj) is not a_class
