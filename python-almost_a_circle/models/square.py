#!/usr/bin/python3
"""
Module - square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Size assignment that inherits from Rectangle
        """
        return self.width
    
    @size.setter
    def size(self, value):
        """
        Size validation that inherits from Rectangle
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square
        object that can be used to create a normal square.
        This does not inherit from Rectangle
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))
