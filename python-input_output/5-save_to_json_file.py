#!/usr/bin/python3
"""
Module: 5-save_to_json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file, using
    a JSON representation
    """
    with open(filename, "w+", encoding="utf-8") as f:
        text = json.dumps(my_obj)
        chars_written = f.write(text)
