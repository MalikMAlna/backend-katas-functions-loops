#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "My own previous work with JavaScript Katas 2"

# from tests.test_main import TestMain


def add(x, y):
    return x + y


def multiply(x, y):
    mult = 0
    for counter in range(x):
        mult = add(mult, y)
    return mult


def power(x, n):
    if n == 0:
        return 1
    else:
        answer = x
        increment = x
        for num_1 in range(1, n, 1):
            for num_2 in range(1, x, 1):
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
    arr = [0, 1]
    for num in range(2, n+1):
        arr.append(add(arr[num-2], arr[num-1]))
    return arr[n-1]


fibonacci(8)

if __name__ == '__main__':
    pass
