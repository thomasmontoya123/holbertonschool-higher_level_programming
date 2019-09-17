#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        position = 0
        for colunm in row:
            position += 1
            if position != len(row):
                print("{:d}".format(colunm), end=' ')
            else:
                print("{:d}".format(colunm), end='')
        print()
