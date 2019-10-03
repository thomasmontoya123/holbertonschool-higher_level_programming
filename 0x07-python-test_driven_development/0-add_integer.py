#!/usr/bin/python3
"""Add two integers module

function that adds 2 integers.

Prototype: def add_integer(a, b=98):

    * a and b must be integers or floats, otherwise raise a
    TypeError exception with the message
    ("a must be an integer") or ("b must be an integer")
    * a and b must be first casted to integers if they are float

Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """Adds a and b if they are int or float.

        If a or b are different to int or float:
            raise TypeError

        if a or b are floats cast them to ints

        Parameters
        ----------
        a : int, float
            First value

        b : int, float
            Second Value
        """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
