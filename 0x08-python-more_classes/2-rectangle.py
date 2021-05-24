#!/usr/bin/python3

"""2-rectangle.py: Rectangle class"""

class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """class Rectangle. Sets a height and width
        Args:
            width (int): sets the width
            height (int): sets the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width
        Args:
            value (int): width position
        """
        if type(value) is not int:
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height
        Args:
            value (int): height position
         """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)