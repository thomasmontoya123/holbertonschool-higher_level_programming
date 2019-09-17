#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        last = 0
        for colunm in row:
            last += 1
            if last == len(row):
                print("{}".format(colunm), end='')
            else:
                print("{}".format(colunm), end=' ')
        print()
