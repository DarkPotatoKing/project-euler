from utils import *

def f(x):
    arr = [int(sqrt(x))]

    # (sqrt(x) - a) / b
    a = arr[0]
    b = 1

    try:
        for _ in xrange(10):
            arr.append(int(float(b) / (sqrt(x) - float(a))))
            b = (x - (a**2)) / b
            a = (b * arr[-1]) - a
    finally:
        return arr

def main():
    for x in (range(2, 14) + [23]):
        print x, f(x)

main()
