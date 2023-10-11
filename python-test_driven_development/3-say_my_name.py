#!/usr/bin/python3
"""
Module: 3-say_my_name

Function: say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: Takes an input first and last name
    and prints it to the terminal

    Args:
    first_name: The first name
    last_name: The last name

    Return:
    Prints the first and last name to the terminal, else raises error.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
