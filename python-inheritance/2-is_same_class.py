#!/usr/bin/python3
"""
Module: A function that returns True of the object is exactly an
instance
"""


def is_same_class(obj, a_class):
    """
    Returns whether obj is exactly an instance of a specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
