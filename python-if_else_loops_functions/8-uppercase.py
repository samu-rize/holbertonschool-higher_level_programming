#!/usr/bin/python3
def uppercase(str):
    strout = ''
    for ch in str:
        if ord(ch) in range(97, 123):
            strout += chr(ord(ch) - 32)
        else:
            strout += ch
    print(strout)
