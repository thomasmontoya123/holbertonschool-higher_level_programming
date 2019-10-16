#!/usr/bin/python3
'''
to JSON module
'''
import json


def to_json_string(my_obj):
    '''
    returns the JSON representation of an object (string)
    Parameters:
        obj: object
    '''
    return json.dumps(my_obj)
