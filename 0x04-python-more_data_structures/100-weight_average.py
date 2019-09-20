#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    x_y_mul = 0
    y_add = 0
    for x, y in my_list:
        x_y_mul += x * y
        y_add += y
    return (x_y_mul / y_add)
