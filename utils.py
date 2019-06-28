from math import sqrt, floor, ceil
from itertools import combinations, permutations, product

import collections
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

@Memo
def is_prime(n):
    if n < 2:
        return False

    for d in xrange(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True

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
