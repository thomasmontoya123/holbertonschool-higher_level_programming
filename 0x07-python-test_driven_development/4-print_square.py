#!/usr/bin/python3
"""Print square module

    * size is the size length of the square

    * size must be an integer, otherwise raise a
    TypeError exception with the message:
    "size must be an integer"

    * if size is less than 0, raise a
    ValueError exception with the message:
    "size must be >= 0"

    * if size is a float and is less than 0,
    raise a TypeError exception with the message:
    "size must be an integer"
"""


def print_square(size):
    """Function that prints a square with the character #

        Parameters
        ----------
        size : int
        Square size

        """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for rows in range(size):
            for columns in range(size):
                print('#', end="")
            print()
