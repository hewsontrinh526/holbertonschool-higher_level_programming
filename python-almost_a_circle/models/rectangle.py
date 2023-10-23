#!/usr/bin/python3
"""
Module - rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        self.__height = value

    @property
    def x(self):
        """
        Retrieves itself
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Determines whether the value is suitable for x
        """
        self.__x = value

    @property
    def y(self):
        """
        Retrieves itself
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Determines whether the value is suitable for y
        """
        self.__y = value
