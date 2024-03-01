#!/usr/bin/python3

"""This module contains the function 'add_integer', which adds 2 integers"""

def add_integer(a, b=98):
    """
    This function adds two integers together and returns the result
    as an integer.

    Arguments:
        a has a default value of zero while b has a default value of 98

    Example:
    >>> add_integer(4, 5)
    9
    >>> add_integer(2)
    100

    The variables must be either integers or floats. If either a or b
    are floats, they are casted as integers. 
    However if the values are neither integers or floats, an exception
    called TypeError is raised.
    """
    if isinstance(a, (float, int)) == False:
        raise TypeError("a must be an integer")

    if isinstance(b, (float, int)) == False:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
