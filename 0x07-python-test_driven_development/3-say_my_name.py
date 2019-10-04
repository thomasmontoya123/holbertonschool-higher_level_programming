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
            Last name (Could be Empty)
        """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    elif first_name == "":
        print("first_name can't be empty")
    else:
        print("My name is {} {}".format(first_name, last_name))
