#!/usr/bin/python3
"""
Module: 4-print_square.py

Function: print_square()
"""


def print_square(size):
    """
    print_square: Prints a square of size 'size' in the terminal

    Args:
    size: Side length of the square

    Return:
    Printed square in terminal
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
