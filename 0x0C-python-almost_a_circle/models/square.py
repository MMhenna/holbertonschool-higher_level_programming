#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square Instance
        Args:
            size (int): size
            size (int): size
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the height value (same as width
        because it's a square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets a new height/width value
        Args:
            value (int): new height/width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square instance
        Args:
            args (list): argument lists
            kwargs (dict): argument dictionary
        """
        if len(args):
            count = 1
            for value in args:
                if count == 1:
                    self.id = value
                if count == 2:
                    self.size = value
                if count == 3:
                    self.x = value
                if count == 4:
                    self.y = value
                count += 1
        elif len(kwargs):
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns a dictionary representation of itself"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return string representation of itself"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                        self.x, self.y, self.width)