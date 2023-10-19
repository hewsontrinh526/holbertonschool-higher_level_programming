#!/usr/bin/python3
"""
Module: 6-base_geometry
"""


class BaseGeometry:
    """
    Public instance method: def area(self):
    """
    def area(self):
        """
        Raises exception that area has not been implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
