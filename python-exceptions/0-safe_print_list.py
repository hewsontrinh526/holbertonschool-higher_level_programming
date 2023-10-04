#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            list_count = list_count + 1
    except IndexError:
        print()
        return list_count
    else:
        print()
        return list_count
