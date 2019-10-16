#!/usr/bin/python3
'''
Save Object to a file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    returns the JSON representation of an object (string)
    Parameters:
        obj: object
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
