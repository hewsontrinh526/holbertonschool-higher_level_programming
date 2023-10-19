#!/usr/bin/python3
"""
Module: 8-class_to_json
"""
import json


def class_to_json(obj):
    """
    A function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialisation of an object.
    """
    return vars(obj)
