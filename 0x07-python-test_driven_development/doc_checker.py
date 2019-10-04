#!/usr/bin/python3
def documentation_checker(module_name):
    documentation = __import__(module_name).__doc__
    if len(documentation) > 1:
        return True
    else:
        return False