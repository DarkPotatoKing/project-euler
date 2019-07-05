from utils import *

# combine two numbers
# combine(123, 456) = 123456
def combine(a, b):
    return int(str(a) + str(b))

def find_prime_set(primes, prime_set = [], length = 5):
    print prime_set
    for i, prime in enumerate(primes):
        if test(prime, prime_set):
            if length == 1:
                return [prime]

            ps = find_prime_set(primes[i + 1:], prime_set + [prime], length - 1)
            if ps:
                return [prime] + ps

def is_prime_pair(a, b):
    return is_prime(combine(a, b)) and is_prime(combine(b, a))

def test(prime, prime_set):
    for p in prime_set:
        if not is_prime_pair(prime, p):
            return False
    return True

def main():
    primes = prime_range(1, 10**4)
    ps = find_prime_set(primes)
    print ps
    print sum(ps)

main()
