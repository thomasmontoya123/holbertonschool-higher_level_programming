#!/usr/bin/python3
'''
can i? module
'''


def add_attribute(object, attribute_name, value):
    '''
    adds a new attribute if its possible
    '''
    if hasattr(object, "__dict__"):
        object.__setattr__(attribute_name, value)
    else:
        raise TypeError("can't add new attribute")
