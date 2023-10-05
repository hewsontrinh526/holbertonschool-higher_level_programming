#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_delete:
        a_dictionary.pop(key)
    return a_dictionary
