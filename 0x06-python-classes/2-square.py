#!/usr/bin/python3

"""2-square.py: class Square"""

class Square:
    """Represents a square with Private instance attribute size.
        Attribute:
            size (int): size of square.
    """
    
    def __init__(self, size=0):
        """Initialization of instance attributes.

        Args:
            size (int): Zero or positve number.
        Raises:
            TypeError: If size not int.
            ValueError: If size < 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else
            self.__size = size
