#!/usr/bin/python3
"""
Module: 0-add_integer.py

Function: add_integer()
"""


def add_integer(a, b=98):
    """
    add_integer: Adds integers/floats together

    Args:
    a and b are inputs, b defaults to 98

    Returns:
    The sum of a and b as an int. a and b are converted before addition
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
