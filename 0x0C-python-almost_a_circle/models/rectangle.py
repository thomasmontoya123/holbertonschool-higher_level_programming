#!/usr/bin/python3
'''
Rectangle class modue
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle Class, inherits from base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Retrieves Private instance attribute  width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Private attribute setter (width)
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Retrieves Private instance attribute  height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Private attribute setter (width)
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''
        Retrieves Private instance attribute  x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Private attribute setter (x)
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''
        Retrieves Private instance attribute  y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Private attribute setter (y)
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Calculates the area of the rectangle
        '''
        return self.width * self.height

    def display(self):
        '''
        Prints the rectangle
        '''
        for y_spaces in range(self.y):
            print()

        for i in range(self.height):
            for x_spaces in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        '''
        print special method
        '''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''
        Update the class Rectangle.
        Assigns an argument to each attribute
        '''
        args_len = len(args)
        parameters = ["id", "width", "height", "x", "y"]
        for i in range(args_len):
            if i > len(parameters):
                break
            else:
                setattr(self, parameters[i], args[i])
        if args_len == 0:
            for key, value in kwargs.items():
                if key in parameters:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of a Rectangle
        '''
        keys = ["id", "width", "height", "x", "y"]
        values = [self.id,  self.width, self.height, self.x, self.y]
        return dict(zip(keys, values))
