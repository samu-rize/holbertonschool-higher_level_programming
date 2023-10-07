#!/usr/bin/python3
for i in range(0, 101):
    if (i % 3) and (i % 5):
        print('{}'.format(i), end=' ')
    elif not (i % 3) and (i % 5):
        print('Fizz', end=' ')
    elif (i % 3) and not (i % 5):
        print('Buzz', end=' ')
    else:
        print('FizzBuzz', end=' ')
