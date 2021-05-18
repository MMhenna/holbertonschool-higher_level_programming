#!/usr/bin/python3
""" Module Square """


class Square:
    """Represents a square with Private instance attribute size.
        Attribute:
            size (int): size of suare
    """
    def __init__(self, size):
        """Initialization of instance attributes
            Args:
                size (int): The size of the square
        """
        self.__size = size
