#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    """
    A class used to represent an Rectangle
    """
    def __init__(self, width=0, height=0):
        '''Initializer'''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' width Retriever'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Height Retriever'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height Setter'''
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''area calculation'''
        return self.width * self.height

    def perimeter(self):
        ''' Perimeter calculation'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        '''When print or str is called prints the rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            line = self.width * "#" + "\n"
            return ((self.height - 1) * (line) + self.width * "#")

    def __repr__(self):
        '''returns an string that
        could be used to recreate an object with the
        same value'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''Detect instance deletion'''
        print ("Bye rectangle...")
