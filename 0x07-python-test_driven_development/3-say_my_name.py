#!/usr/bin/python3
"""Say my name  module

   first_name and last_name must be strings otherwise, raise a
   TypeError exception with the message:
   "first_name must be a string" or "last_name must be a string"
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

        Parameters
        ----------
        first_name : str
            First name

        last_name : str
            Last name (Could be None)
        """
        if isinstance(first_name, str) is False:
            raise TypeError("first_name must be a string")
        