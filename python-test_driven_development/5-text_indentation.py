#!/usr/bin/python3
"""
Module: 5-text_indentation

Function: text_indentation()
"""


def text_indentation(text):
    """
    text_indentation: Will print the given text, but place new
    lines after '.', '?' or ':'.

    Args:
    text: Text to be indented

    Return:
    Indented text
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
