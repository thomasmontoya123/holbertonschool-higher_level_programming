#!/usr/bin/python3


def find_peak(list_of_integers):
    if len(list_of_integers) > 0:
        # Base case for recursion
        if len(list_of_integers) == 1:
            return list_of_integers[0]

        middle = len(list_of_integers) // 2

        if len(list_of_integers) == 2:
            if list_of_integers[middle] > list_of_integers[0]:
                return list_of_integers[middle]
            else:
                return list_of_integers[0]

        if (list_of_integers[middle] > list_of_integers[middle + 1] and
                list_of_integers[middle] > list_of_integers[middle - 1]):
            return list_of_integers[middle]

        if list_of_integers[middle + 1] > list_of_integers[middle]:
            return find_peak(list_of_integers[middle + 1:])

        return find_peak(list_of_integers[0:middle])
