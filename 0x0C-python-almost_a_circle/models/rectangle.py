#!/usr/bin/python3
"""Rectangle Class Module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize id from Base
        Args:
            width (int): width
            height (int): height
            x (int): length
            y (int): height
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width of rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle instance
        Args:
            value (int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle instance
        Args:
            value (int):  value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x property
        Args:
            value (int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y property
        Args:
            value (int): value to set
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Returns a # representation of itself"""
        for row in range(self.__y):
            print()
        for num in range(self.__height):
            print(self.__x * " " + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Updates instance of itself with new arguments
        Args:
            args: set of arguments
            kwargs: set of arguments
        """
        count = 1
        if len(args):
            for value in args:
                if count == 1:
                    self.id = value
                if count == 2:
                    self.width = value
                if count == 3:
                    self.height = value
                if count == 4:
                    self.x = value
                if count == 5:
                    self.y = value
                count += 1
        elif len(kwargs):
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of itself"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return string of rectangle instance's stats"""
        return '[Rectangle] ({}) {}/{} - '\
               '{}/{}'.format(self.id, self.__x, self.__y,
                                self.__width, self.__height)