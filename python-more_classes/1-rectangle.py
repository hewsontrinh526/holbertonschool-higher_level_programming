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
    """
    def __init__(self, width=0, height=0):
        """
        Initialises a new instance of a rectangle

        Arguments:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        """
        self.__height = height
        self.__width = width

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
            raise TypeError("width ust be an integer")
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
