#!/usr/bin/python3
""" This module is used as intro to classes """


class Square:
    """ square class with size(>=0 integer) attribute """
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """ size attibute getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size attribute setter """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ calculate and return the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ draw the square on stdout using the '#' character """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()