#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    dic_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum, prev = 0, 0
    roman_string = reversed(roman_string)
    for roma in roman_string:
        if roma not in dic_rom:
            return 0
        now = dic_rom[roma]
        if now >= prev:
            sum += now
        else:
            sum -= now
        prev = now
    return sum
