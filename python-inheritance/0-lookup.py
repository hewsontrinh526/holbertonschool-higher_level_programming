#!/usr/bin/python3
"""
Module: A function that returns a list of avaliable
attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of avaliable attributes and methods
    of an object
    """
    return dir(obj)
