#!/usr/bin/python3

"""This module contains the function 'add_integer', which adds 2 integers."""

def add_integer(a, b=98):
    """This function adds two integers together and returns the result as an integer.
    Arguments: a has a default value of zero while b has a default value of 98
    Raises:
        The variables must be either integers or floats. If either a or b are floats, they are casted as integers. However if the values are neither integers or floats, an exception called TypeError is raised.
        """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
