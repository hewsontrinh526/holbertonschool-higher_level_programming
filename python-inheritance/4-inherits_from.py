#!/usr/bin/python3
"""
Module: A function that return True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class, else False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited from
    (directly or indirectly) from the specified class, else False
    """
    if isinstance(obj, a_class) is True:
        if type(obj) != a_class:
            return True
    return False
