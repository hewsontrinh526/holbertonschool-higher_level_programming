#!/usr/bin/python3
"""
Module: 0-read_file
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    """
    with open('my_file_0.txt', encoding="utf-8") as my_file_0:
        print(my_file_0.read(), end="")
