#!/usr/bin/python3
'''
My int module
'''


class MyInt(int):
    '''
    Class My int inherits from int
    '''
    def __init__(self, n):
        '''
        Constructor
        '''
        self.__n = n

    def __eq__(self, second):
        '''
        changes == for !=
        '''
        return (self.__n != second)

    def __ne__(self, second):
        '''
        changes != for ==
        '''
        return(self.__n == second)
