from utils import *

# from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def is_odd_period(s):
    m = [0]
    d = [1]
    a = [int(sqrt(s))]

    n = 0
    try:
        while a[n] != 2 * a[0]:
            m.append((d[n] * a[n]) - m[n])
            d.append((s - (m[n+1]**2)) / d[n])
            a.append(int((a[0] + m[n+1]) / d[n+1]))
            n += 1
    except ZeroDivisionError:
        pass
    finally:
        return is_odd(n)


def main(n = 10000):
    num_odd_period = 0
    for x in xrange(n + 1):
        odd_period = is_odd_period(x)
        print x, odd_period
        if odd_period:
            num_odd_period += 1
    print '{} odd period fractions for N <= {}'.format(num_odd_period, n)

main()
