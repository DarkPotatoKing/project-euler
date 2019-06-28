from math import sqrt, floor, ceil
from itertools import combinations, permutations, product

def average(ls):
    return float(sum(ls)) / float(len(ls))

def divide(numerator, denominator):
    return float(numerator) / float(denominator)

def factorial(n):
    if n < 0:
        raise StandardError('Factorial is not defined for negative numbers')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False

    for d in xrange(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True

def multiply(a, b):
    return a * b

def nCr(n, k):
    if k > n or k < 0:
        return 0.0
    else:
        return divide(factorial(n), factorial(k) * factorial(n - k))
