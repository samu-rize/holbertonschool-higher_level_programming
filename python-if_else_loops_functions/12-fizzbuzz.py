#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) and (i % 5):
            print('{}'.format(i), end=' ')
        elif not (i % 3) and (i % 5):
            print('Fizz', end=' ')
        elif (i % 3) and not (i % 5):
            print('Buzz', end=' ')
        else:
            print('FizzBuzz', end=' ')
