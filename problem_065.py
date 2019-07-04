from utils import *

def continued_fraction(a):
    if len(a) == 1:
        return Fraction(a[0])
    else:
        return Fraction(a[0]) + Fraction(1, continued_fraction(a[1:]))

def e(n):
    if n == 0:
        return 2
    elif n % 3 == 2:
        return 2 * ((n / 3) + 1)
    else:
        return 1
def euler(n):
    return [e(i) for i in xrange(n)]

def main(n = 100):
    convergent = continued_fraction(euler(n))
    print digit_sum(convergent.numerator)

main()
