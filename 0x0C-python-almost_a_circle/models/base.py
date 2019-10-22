#!/usr/bin/python3
'''
Base class modue
'''
import json
from turtle import *
import csv


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
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            else:
                for instance in list_objs:
                    json_list.append(instance.to_dictionary())
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
            down()
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
            up()
            i += 1
            if i >= len(colors):
                i = 0

        setpos(0, 0)
        for sqr in list_squares:
            pencolor(colors[i])
            setpos(sqr.x, sqr.y)
            down()
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
            up()
            i += 1
            if i >= len(colors):
                i = 0

        input()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        save to a csv file format
        '''
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w') as f:
            counter = 0
            if cls.__name__ == 'Rectangle':
                fieldnames = ['width', 'height', 'x', 'y', 'id']
                keys = {'width': 'width', 'height': 'height', 'x': 'x',
                        'y': 'y', 'id': 'id'}
            else:
                fieldnames = ['size', 'x', 'y', 'id']
                keys = {'size': 'size', 'x': 'x', 'y': 'y', 'id': 'id'}
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for element in list_objs:
                if counter == 0:
                    writer.writerow(keys)
                    counter += 1
                writer.writerow(element.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''
        load from csv
        '''
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'r') as f:
            instance_dict = {}
            insttance_list = []
            reader = csv.DictReader(f)
            for element in reader:
                for key, value in element.items():
                    instance_dict[key] = int(value)
                instance = cls.create(**instance_dict)
                insttance_list.append(instance)
            return insttance_list
