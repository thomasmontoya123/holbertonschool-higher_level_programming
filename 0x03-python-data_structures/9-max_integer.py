#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    else:
        max = 0
        for i in my_list:
            if i > max:
                max = i
    return max