#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    if len(tuple_a) < 2:
        for i in range(0, 2 - len(tuple_a)):
            tuple_a += (0,)
    if len(tuple_b) < 2:
        for i in range(0, 2 - len(tuple_b)):
            tuple_b += (0,)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
