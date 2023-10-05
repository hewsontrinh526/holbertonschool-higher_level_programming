#!/usr/bin/python3
def weight_average(my_list=[]):
    total_average = 0
    total_product = 0
    for item in my_list:
        value, weight = item
        total_product = total_product + (value * weight)
        total_average = total_average + weight
    if total_average == 0:
        return 0
    else:
        return total_product / total_average
