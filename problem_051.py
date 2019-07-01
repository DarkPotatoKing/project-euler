from utils import *

# must not be divisible by 2 or 3
def first_filter(num):
    return (num % 2 != 0) and (num % 3 != 0)

# must have 3 repeated digits (minus the last digit)
def second_filter(num):
    return match(r'(\d*0\d*0\d*0\d+)|(\d*1\d*1\d*1\d+)|(\d*2\d*2\d*2\d+)|(\d*3\d*3\d*3\d+)|(\d*4\d*4\d*4\d+)|(\d*5\d*5\d*5\d+)|(\d*6\d*6\d*6\d+)|(\d*7\d*7\d*7\d+)|(\d*8\d*8\d*8\d+)|(\d*9\d*9\d*9\d+)', num)

def test(num):
    s = str(num)
    for i in xrange(10):
        c = str(i)
        if s.count(c) == 3:
            prime_count = 0
            for j in xrange(10):
                d = str(j)
                n = int(s.replace(c, d))
                if len(str(n)) == len(s) and is_prime(n):
                    prime_count += 1
            return prime_count == 8



def main():
    candidates = filter(first_filter, xrange(10**6))
    candidates = filter(second_filter, candidates)
    candidates = filter(is_prime, candidates)
    for candidate in candidates:
        if test(candidate):
            print candidate
            break

    # for i in xrange(10):
    #     n = (101010 * i) + 20303
    #     print n, is_prime(n)

main()
