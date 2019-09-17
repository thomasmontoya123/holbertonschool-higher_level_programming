#!/usr/bin/python3
def print_list_integer(my_list=[]):
    size = len(my_list)
    for i in range(size):
        print("{:d}".format(my_list[i]))
