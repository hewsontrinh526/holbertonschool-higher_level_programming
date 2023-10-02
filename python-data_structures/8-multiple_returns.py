#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence is None:
        first = " "
    else:
        first = sentence[0]
    tuple_return = (length, first)
    return tuple_return