#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in romans:
            break
        if i > 0 and romans[roman_string[i]] > romans[roman_string[i - 1]]:
            result += romans[roman_string[i]] - 2 * romans[roman_string[i - 1]]
        else:
            result += romans[roman_string[i]]
    return result
