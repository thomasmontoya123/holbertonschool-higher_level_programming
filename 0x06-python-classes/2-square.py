#!/usr/bin/python3
class Square():
    '''
    Clas definition: Square
    '''
    def __init__(self, size=0):
        '''
        Args:
            size: Square size
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size