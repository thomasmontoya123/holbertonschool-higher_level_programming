#!/usr/bin/python3
'''
Square module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class, inherits from rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        print special method
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''
        size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Size setter
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Update the class square.
        Assigns an argument to each attribute
        '''
        args_len = len(args)
        parameters = ["id", "size", "x", "y"]
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
        Returns the dictionary representation of a Square
        '''
        keys = ["id", "size", "x", "y"]
        values = [self.id, self.height, self.x, self.y]
        return dict(zip(keys, values))