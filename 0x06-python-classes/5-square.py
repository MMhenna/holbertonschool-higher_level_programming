#!/usr/bin/python3


class Square:    

    """Defining a Square"""

    def __init__(self, size):
        '''Initialization of instance attributes
            Args: 
            size (int): Zero or positve number.
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else
            self.__size = size

    @property
    def size(self):
        """returns the size of the length of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the size value
            Args:
            value (int): Zero or positve number.
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else
            self.__size = value

    def area(self):
        '''Calculates the area
            Return: 
            The current square area.
        '''
        return self.__size * self.__size

    def my_print(self):
         """Prints the a square in # the size of the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)