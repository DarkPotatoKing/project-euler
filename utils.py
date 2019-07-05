from fractions import Fraction
from itertools import combinations, permutations, product
from math import sqrt, floor, ceil
from sympy import sieve
from sympy.ntheory import isprime

import collections
import re
import functools

class Memo(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

def average(ls):
    return float(sum(ls)) / float(len(ls))

def create_sieve(min_num = 1, max_num = 10**6):
    return [i for i in sieve.primerange(min_num, max_num)]

def digit_sum(num):
    return sum(digits(num))

def digits(num):
    return [int(c) for c in str(num)]

def divide(numerator, denominator):
    return float(numerator) / float(denominator)

@Memo
def divisors(n):
    val = []
    for d in xrange(1, int(sqrt(n)) + 1):
        if n % d == 0:
            e = n / d
            val.append(d)
            if d != e:
                val.append(e)
    return sorted(val)

@Memo
def factorial(n):
    if n < 0:
        raise StandardError('Factorial is not defined for negative numbers')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    return isprime(n)

def match(pattern, string):
    string = str(string)
    return re.match(pattern, string) != None

def multiply(a, b):
    return a * b

@Memo
def nCr(n, r):
    if r > n or r < 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return nCr(n - 1, r - 1) + nCr(n - 1, r)

@Memo
def prime_factors(n):
    val = []
    limit = n + 1
    for d in xrange(2, limit):
        if n % d == 0:
            e = 0
            while n % d == 0:
                n /= d
                e += 1
            val.append((d, e))

        if n == 1:
            break
    return val

@Memo
def combine_prime_factors(a, b):
    pf = []
    pa = prime_factors(a)
    pb = prime_factors(b)

    x = 0
    y = 0

    while x < len(pa) and y < len(pb):
        ba, ea = pa[x]
        bb, eb = pb[y]
        if ba == bb:
            pf.append((ba, ea + eb))
            x += 1
            y += 1
        elif ba < bb:
            pf.append((ba, ea))
            x += 1
        else:
            pf.append((bb, eb))
            y += 1

    if x < len(pa):
        pf += pa[x:]
    else:
        pf += pb[y:]

    prime_factors.cache[a * b,] = pf
    return pf
