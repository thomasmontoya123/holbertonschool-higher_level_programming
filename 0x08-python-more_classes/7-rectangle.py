#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    """
    A class used to represent an Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initializer'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            symbol_cast = str(self.print_symbol)
            line = symbol_cast * self.width + "\n"
            return ((self.height - 1) * (line) + self.width * symbol_cast)

    def __repr__(self):
        '''returns an string that
        could be used to recreate an object with the
        same value'''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        '''Detect instance deletion'''
        Rectangle.number_of_instances -= 1
        print ("Bye rectangle...")
