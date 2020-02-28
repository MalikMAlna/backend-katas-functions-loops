#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = """https://stackoverflow.com/questions/494594/
                how-to-write-the-fibonacci-sequence#499245
                and debugging help from Derek"""


def add(x, y):
    return x + y


def multiply(x, y):
    mult = 0
    if x == 0 or y == 0:
        return 0
    elif 0 > x and 0 > y:
        x = abs(x)
        y = abs(y)
        for counter in range(x):
            mult = add(mult, y)
        return mult
    elif 0 > x or 0 > y:
        x = abs(x)
        y = abs(y)
        for counter in range(x):
            mult = add(mult, y)
        return int("-" + str(mult))
    else:
        for counter in range(x):
            mult = add(mult, y)
        return mult


def power(x, n):
    if n == 0:
        return 1
    else:
        answer = x
        increment = x
        for num_1 in range(1, n):
            answer = multiply(answer, increment)
    increment = answer
    return answer


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        count = x - 1
        while count:
            x = multiply(x, count)
            count -= 1
        return x


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return add(fibonacci(n-1), fibonacci(n-2))
