#!/usr/bin/python3
class Square():
    '''
    Class definition: Square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Args:
            size: Square size
            position: tuple of coordinates
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
        if (len(position) != 2 or type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int) or not
                isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        '''
        property to retrieve it
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        property to update the position value
        Args:
            value: New size
        '''
        if (len(position) != 2 or type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0] is not int or type(position[1] is not int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        '''
        Print the square.
        '''
        if self._Square__size <= 0:
            print()
        else:
            for row_spaces in range(self.__position[1]):
                print()
            for rows in range(self._Square__size):
                for column_spaces in range(self.__position[0]):
                    print(" ", end="")
                for columns in range(self._Square__size):
                    print('#', end="")
                print()
