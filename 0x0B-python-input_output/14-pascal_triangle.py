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

    for i in range(n):
        row = []
        for value in range(i + 1):
            row.append(combination(i, value))
        result.append(row)
    return result


def combination(n, k):
    '''
    recursion method
    '''
    if k == 0 or k == n:
        return str(1)
    else:
        return str(int(combination(n - 1, k - 1)) + int(combination(n - 1, k)))
