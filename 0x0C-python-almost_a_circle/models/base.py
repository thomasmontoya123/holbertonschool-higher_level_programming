#!/usr/bin/python3
'''
Base class modue
'''
import json


class Base:
    '''
    Base Class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file:
        '''
        json_list = []
        for instance in list_objs:
            json_list.append(instance.to_dictionary())
    
        with open("{}.json".format(str(cls.__name__)), 'w', encoding='utf-8') as f:
                if list_objs is None:
                    f.write("[]")
                else:
                    new_json = cls.to_json_string(json_list)
                    f.write(new_json)

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list of the JSON string representation json_string:
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set:

        **dictionary can be thought of as a double pointer to a dictionary
        To use the update method to assign all attributes, you must create a “dummy” instance before:
        Create a Rectangle or Square instance with “dummy” mandatory attributes (width, height, size, etc.)
        Call update instance method to this “dummy” instance to apply your real values

        '''
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances
        '''
        instance_list = []

        try:
            with open("{}.json".format(cls.__name__), encoding='utf-8') as f:
                json_file = cls.from_json_string(f.read())
                for instance in json_file:
                    new = cls.create(**instance)
                    instance_list.append(new)
                return instance_list
        except :
            return instance_list