#!/usr/bin/python3
'''
Square module
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Defines an Square
    '''
    def __init__(self, size):
        '''
        Constructor
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''
        Printer
        '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
