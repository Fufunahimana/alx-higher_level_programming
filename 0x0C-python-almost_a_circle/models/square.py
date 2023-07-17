#!/usr/bin/python3

""" Defines a square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Creates a square """

    def __init__(self, size, x=0, y=0, id=None):

        """ Initializes square """
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Gets size """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets width and height

        Args:
            value: width
            value1: height

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value
