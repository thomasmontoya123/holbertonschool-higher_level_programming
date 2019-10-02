#!/usr/bin/python3
class Square():
    '''
    Class definition: Square
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

    def area(self):
        '''
        returns the area of the square
        '''
        return self._Square__size ** 2

    @property
    def size(self):
        '''
        property to retrieve it
        '''
        return self._Square__size

    @size.setter
    def size(self, value):
        '''
        property to update the size value
        Args:
            value: New size
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def my_print(self):
        if self._Square__size is 0:
            print()
        else:
            for rows in range(self._Square__size):
                for columns in range(self._Square__size):
                    print('#', end="")
                print()
