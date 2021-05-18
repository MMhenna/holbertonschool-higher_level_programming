#!/usr/bin/python3


class Square:    

    """Defining a Square"""

    def __init__(self, size=None, position=(0, 0)):
        '''Initialization of instance attributes
            Args: 
            size (int): Zero or positve number.
            position (int): 2 coordinate position.
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (len(position) is not 2 or type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else
            self.__size = size
            self.__position = position

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

    @property
    def size(self):
        """returns the position"""
        return self.__position

    @position.setter
    def size(self, value):
        """sets the position values
            Args:
            value (int): the tuple value to set the position
        """
        if (len(position) is not 2 or type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else
            self.__position = position

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


    