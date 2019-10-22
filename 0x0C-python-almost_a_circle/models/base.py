#!/usr/bin/python3
'''
Base class modue
'''
import json
from turtle import *


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file:
        '''
        json_list = []
        for instance in list_objs:
            json_list.append(instance.to_dictionary())

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write(json_list)
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
        To use the update method to assign all attributes, you must create
        a “dummy” instance before:
        Create a Rectangle or Square instance with “dummy” mandatory attributes
        (width, height, size, etc.)
        Call update instance method to this “dummy” instance to apply your real
        values

        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
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
        except:
            return instance_list

    def draw(list_rectangles, list_squares):
        '''
        Opens a window and draws all the Rectangles and Squares
        '''
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        i = 0
        for rec in list_rectangles:
            setpos(rec.x, rec.y)
            width(4)
            fillcolor(colors[i])
            pencolor(colors[i])
            begin_fill()
            forward(rec.width)
            left(90)
            forward(rec.height)
            left(90)
            forward(rec.width)
            left(90)
            forward(rec.height)
            left(90)
            end_fill()
            width(0)
            i += 1
            if i >= len(colors):
                i = 0

        setpos(0, 0)
        for sqr in list_squares:
            pencolor(colors[i])
            setpos(sqr.x, sqr.y)
            width(7)
            fillcolor(colors[i])
            begin_fill()
            forward(sqr.width)
            left(90)
            forward(sqr.width)
            left(90)
            forward(sqr.width)
            left(90)
            forward(sqr.width)
            left(90)
            end_fill()
            width(0)
            i += 1
            if i >= len(colors):
                i = 0

        input()
