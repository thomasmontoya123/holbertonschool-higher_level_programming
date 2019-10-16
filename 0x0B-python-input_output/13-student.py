#!/usr/bin/python3
'''
Student to JSON module
'''


class Student:
    '''
    Describes an student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        if attrs is None:
            return self.__dict__
        else:
            return ({key: value for key, value in self.__dict__.items() if key in attrs})

    def reload_from_json(self, json):
        '''
        Replaces all attributes of the Student instance
        '''
        self.__dict__.update(json)