#!/usr/bin/python3

"""0-add_integer: module that adds two integers together"""

def add_integer(a, b=98):
    """Add integer adds two integers together that are int types

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: a + b

    Raises:
        TypeError: if any of the args is not an int or a float
    """

    types = [int, float]

    if type(a) not in types:
        raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")       
    return int(a) + int(b)