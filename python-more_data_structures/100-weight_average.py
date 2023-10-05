#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    product = 0
    for item in my_list:
        value, weight = item
        product = product + (value * weight)
        average = average + weight
    if average == 0:
        return 0
    else:
        return product / average
