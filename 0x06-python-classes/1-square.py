#!/usr/bin/python3


"""1-square.py: Creates a class Square"""


class Square:
    """Defining a Square"""
    def __init__(self, size=None):
        """ Initialization of instance attributes
            Args:
            size (int): Zero or positve number.
        """
        self.__size = size