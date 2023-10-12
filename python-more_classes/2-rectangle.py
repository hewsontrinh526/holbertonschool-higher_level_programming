#!/usr/bin/python3
"""
Module: 1-rectangle

A class that defines a rectangle

Function:
        __init__(self, width=0, height=0): Initialises a new
            instance of a rectangle
        width(self): Retrieves the width
        width(self, value): Determines whether the value
            is suitable for the width
        height(self): Retrieves the height
        height(self, value): Determines whether
            the value is suitable for the height
        area(self): Finds the area of the rectangle
        perimeter(self): Finds the perimeter of the rectangle
"""


class Rectangle:
    """
    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle

    Methods:
        __init__(self, width=0, height=0): Initialises a new
            instance of a rectangle
        width(self): Retrieves the width
        width(self, value): Determines whether the
            value is suitable for the width
        height(self): Retrieves the height
        height(self, value): Determines whether the
            value is suitable for the height
        area(self): Finds the area of the rectangle
        perimeter(self): Finds the perimeter of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialises a new instance of a rectangle

        Arguments:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves itself
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Determines whether the value is suitable for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves itself
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Determines whether the value is suitable for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Finds the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Finds the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)
