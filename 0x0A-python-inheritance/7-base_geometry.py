#!/usr/bin/python3
'''
BaseGeometry module
'''


class BaseGeometry:
    '''
    BaseGeometry Class
    '''
    def area(self):
        '''
        empty method
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validates value

        Parameters
        name: string name
        value: value, should be an integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
