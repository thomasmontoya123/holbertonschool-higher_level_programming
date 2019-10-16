#!/usr/bin/python3
'''
From JSON string to Object
'''
import json


def from_json_string(my_str):
    '''
    returns an object (Python data structure)
    represented by a JSON string

    Parameters:
        obj: object
    '''
    return json.loads(my_str)
