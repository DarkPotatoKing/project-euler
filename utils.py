from math import sqrt

def is_prime(n):
    if n < 2:
        return False

    for d in xrange(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True
