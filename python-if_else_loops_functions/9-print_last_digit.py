#!/usr/bin/python3
def print_last_digit(number):
    output = abs(number)
    output %= 10
    print('{}'.format(output), end='')
    return (output)
