#!/usr/bin/python3

""" This module contains a class that defines a rectangle """

from models.base import Base


class Rectangle(Base):
    """ Defines a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes rect """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """ Gets width """
        return self.__width

    @property
    def height(self):
        """ Gets height """
        return self.__height

    @property
    def x(self):
        """ Gets X """
        return self.__x

    @property
    def y(self):
        """ Gets Y """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets new width

        Args:
            value: new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets new heigh

        Args:
            value: new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets new x

        Args:
            value: new x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets new y

        Args:
            value: new y value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Gets area of rectangle """

        return self.__width * self.__height

    def display(self):
        """ Prints out the rectangle using # """
        str = ""

        for _ in range(self.__y):
            print()
            str += "\n"

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
            str += " " * self.__x + "#" * self.__width + "\n"
        return str

    def __str__(self):
        """ Returns a string rep """
        str = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
        )
        return str

    def update(self, *args, **kwargs):
        """ updates rectangle values """

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]

        if len(args) == 0:
            for key, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'width' in kwargs:
                    self.__width = kwargs['width']
                if 'height' in kwargs:
                    self.__height = kwargs['height']
                if 'x' in kwargs:
                    self.__x = kwargs['x']
                if 'y' in kwargs:
                    self.__y = kwargs['y']
