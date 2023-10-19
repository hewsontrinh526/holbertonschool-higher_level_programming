#!/usr/bin/python3
"""
Module: 9-student
"""


class Student:
    """
    A class Student that defines a student by first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialisation of an object.
        """
        return self.__dict__
