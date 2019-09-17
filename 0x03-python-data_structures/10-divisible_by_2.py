#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 is 0:
            newlist.append(True)
            i += 1
        else:
            newlist.append(False)
            i += 1
    return newlist
