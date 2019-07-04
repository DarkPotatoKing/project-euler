from utils import *

def hash(num):
    hash_val = ''
    frequency = [0] * 10

    for d in digits(num):
        frequency[d] += 1

    for f in frequency:
        hash_val += str(f)

    return hash_val

def main():
    cubic_permutations = dict()
    cube = dict()
    limit = 10**4
    num_permutations = 5

    for i in xrange(1, limit + 1):
        num = i ** 3
        key = hash(num)
        if key in cubic_permutations:
            cubic_permutations[key] += 1
        else:
            cubic_permutations[key] = 1
            cube[key] = num

    for key in cubic_permutations:
        if cubic_permutations[key] == num_permutations:
            print cube[key]

main()
