#!/usr/bin/python3
'''
Create object from a JSON file module
'''
import json


def load_from_json_file(filename):
    '''
    creates an Object from a “JSON file”
    '''
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
