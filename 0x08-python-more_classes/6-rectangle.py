#!/usr/bin/python3
"""rectangle class

"""


class Rectangle:
    """makes rectangle object

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes square

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets width

        """
        return self.__width

    @property
    def height(self):
        """gets height

        """
        return self.__height

    @width.setter
    def width(self, value):
        """sets width

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area

        """
        return self.height * self.width

    def perimeter(self):
        """ returns perimeter

        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """modifies str object

        """
        if not self.perimeter:
            return ""
        return ('\n'.join('#' * self.width for x in range(self.height)))

    def __repr__(self):
        """modifies repr object

        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """modifies del object

        """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))