#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {key: (lambda x: x * 2)(value) for key, value in a_dictionary.items()}
    return new_dict
