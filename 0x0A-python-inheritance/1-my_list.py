#!/usr/bin/python3
'''
    Mylist Class module
'''


class MyList(list):
    '''
    Derived class Mylist
    inherits from the class list
    '''
    def print_sorted(self):
        print(sorted(self))
