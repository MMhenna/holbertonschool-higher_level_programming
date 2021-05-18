#!/usr/bin/python3
""" Module Square """


class Square:
    """Represents a square with Private instance attribute size.
        Attribute:
            size (int): size of square
    """
    def __init__(self, size=0):
        """Initialization of instance attributes
        Args:
            size (int): size of square
        Exception raises:
            TypeError: if size is not an int
            ValueError: size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
                        
    def area(self):
        """Calculates the area.
            Return: 
                The current square area
        """
        return self.__size * self.__size