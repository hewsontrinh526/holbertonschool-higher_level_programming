#!/usr/bin/python3
"""

"""


def text_indentation(text):
    """
    
    """
    new_line_chars = ['.', '?', ':']
    prev_char = 0

    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == " " and prev_char == 1:
            continue
        prev_char = 0
        print(i, end="")
        if i in new_line_chars:
            prev_char = 1
            print('\n')