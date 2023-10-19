#!/usr/bin/python3
"""
Module: 10-student
"""


class Student:
    """
    A class Student that defines a student by first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialisation of an object.
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if hasattr(self, i):
                new_dict[i] = getattr(self, i)
        return new_dict
