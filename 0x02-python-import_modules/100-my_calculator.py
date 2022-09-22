#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def my_calc(argv):
    '''
        performs basic maths operations on arguments.
        shows error if the wrong operators are used
        shows error if less than 3 or more arguments are passed.
    '''

    n = len(argv) - 1

    if n != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if op == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a,b))

    elif op == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))

    elif op == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))

    elif op == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))

    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)


if __name__ == '__main__':
    import sys
    my_calc(sys.argv)

