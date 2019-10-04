#!/usr/bin/python3
"""Divide matrix module

    * matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message:
    ("matrix must be a matrix (list of lists) of integers/floats")

    * Each row of the matrix must be of the same size,
     otherwise raise a TypeError exception with the message:
    ("Each row of the matrix must have the same size")

    * div must be a number (integer or float),
    otherwise raise a TypeError exception with the message:
    ("div must be a number")

    * div can’t be equal to 0, otherwise raise a
    ZeroDivisionError exception with the message:
    ("division by zero")

    * All elements of the matrix are divided  by div,
    and rounded to 2 decimal places

Returns a new matrix
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

        Parameters
        ----------
        matrix : list of list
            hold the values

        div : int, float
            number to divide each element of the matrix
        """

    if isinstance(matrix, list) is False or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    elif isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])

    for row in matrix:
        for value in row:
            if isinstance(value, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)\
                            of integers/floats")

            if len(row) != row_size:
                raise TypeError("Each row of the matrix must\
                            have the same size")

    return [list(map(lambda x: round(x / div, 2), row))for row in matrix]
