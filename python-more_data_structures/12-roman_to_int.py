#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    rom_dict = {
        "M": 1000, "D": 500, "C": 100, "X": 10, "L": 50, "V": 5, "I": 1
        }

    num = 0

    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num = num + roman_dict.get(roman_string[i])
        elif rom_dict.get(roman_string[i]) < rom_dict.get(roman_string[i + 1]):
            num = num - roman_dict.get(roman_string[i])
        else:
            num = num + roman_dict.get(roman_string[i])

    return num
