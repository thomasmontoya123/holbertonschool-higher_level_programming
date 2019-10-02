#!/usr/bin/python3
class Square:
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
            self.__size = size

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

    def area(self):
        '''
        returns the area of the square
        '''
        return self._Square__size ** 2

    def __lt__(self, other):
        '''
        special method
        '''
        return (self.size < other.size)

    def __gt__(self, other):
        '''
        special method
        '''
        return (self.area() > other.area())

    def __le__(self, other):
        '''
        special method
        '''
        return (self.area() <= other.area())

    def __ge__(self, other):
        '''
        special method
        '''
        return (self.area() >= other.area())

    def __eq__(self, other):
        '''
        special method
        '''
        return (self.size == other.size)

    def __eq__(self, other):
        '''
        special method
        '''
        return (self.area() == other.area())
