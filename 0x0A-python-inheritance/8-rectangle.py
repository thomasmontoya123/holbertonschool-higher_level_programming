#!/usr/bin/python3
'''
Rectangle module
'''
base_geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_geometry):
    '''
    A class used to represent an Rectangle
    '''
    def __init__(self, width, height):
        '''
        Constructor
        '''
        base_geometry().integer_validator("width", width)
        base_geometry().integer_validator("height", height)
        self.__width = width
        self.__height = height
