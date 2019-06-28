from utils import *

def main():

    def b(n):
        return reduce(multiply, [nCr(n, r) for r in xrange(n + 1)])

    print b(5)

main()
