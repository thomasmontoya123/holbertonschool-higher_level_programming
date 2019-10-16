#!/usr/bin/python3
'''
Pascal traingle module
'''


def pascal_triangle(n):
    '''
    returns a list of lists of
    integers representing the Pascal’s
    triangle of n
    '''
    result = []
    if n <= 0:
        return result

    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            elem = result[i-1][j-1] + result[i-1][j]
            row.append(elem)
        row.append(1)
        result.append(row)
    return result
