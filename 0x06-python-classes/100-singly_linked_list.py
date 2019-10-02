#!/usr/bin/python3
class Node:
    '''
    Class definition: Node
    '''
    def __init__(self, data, next_node=None):
        '''
        Args:
            data (int): Node dat
            next_node(Node): link
        '''
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        '''
        property to retrieve it
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        property to update the data value
        Args:
            value: New data
        '''
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        property to retrieve it
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        property to update the next_node value
        Args:
            value: New next_node
        '''
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''
    Class definition: SinglyLinkedList
    '''
    def __init__(self):
        '''
        Args:
            None
        '''
        self.__head = None

    def sorted_insert(self, value):
        '''
        Inserts a new Node into the correct sorted position
        in the list (increasing order)
        Args:
            value: Value to be inserted
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temporal = self.__head
            new_node.next_node = temporal.next_node
            while temporal.next_node and value > temporal.next_node.data:
                new_node.next_node = temporal.next_node.next_node
                temporal = temporal.next_node
            temporal.next_node = new_node

    def __str__(self):
        __list = ""
        actual_node = self.__head
        while actual_node:
            __list += str(actual_node.data) + "\n"
            actual_node = actual_node.next_node
        __list = __list[:-1]
        return __list
