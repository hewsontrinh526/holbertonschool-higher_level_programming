#!/usr/bin/python3
"""
Module: 10-square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Size is privatised
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """
        Finds the area of the square
        """
        return super().area()

    def __str__(self):
        """
        Returns a description of the square
        """
        return (f"[{type(self).__name__}] {self.__size}/{self.__size}")
