#!/usr/bin/python3
""" This module is used as intro to classes """


class Square:
    """ square class with size(>=0 integer) attribute """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ size attibute getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size attribute setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else
            self.__size = value

    def area(self):
        """ calculate and return the area of the square """
        return self.__size * self.__size