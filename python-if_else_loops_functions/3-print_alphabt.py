#!/usr/bin/python3
for ch in range(97, 123):
    if (ch != 101) & (ch != 113):
        print("{}".format(chr(ch)), end ='')
