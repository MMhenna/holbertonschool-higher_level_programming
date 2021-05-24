#!/usr/bin/python3

"""7-rectangle.py: Rectangle Class"""

class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class Rectangle. Sets a height and width
        Args:
            width (int): sets the width
            height (int): sets the height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """prints as square from the symbol"""
        new_str = ''
        if self.__width == 0 or self.__height == 0:
            return new_str
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        for width in range(self.__height - 1):
            new_str += (self.print_symbol * self.__width) + '\n'
        new_str += (self.print_symbol * self.__width)
        return new_str

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")