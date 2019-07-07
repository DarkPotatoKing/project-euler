from utils import *

class Node:

    def __init__(self, polygon_number, value):
        self.polygon_number = polygon_number
        self.value = value
        self.next = []
        self.left = value / 100
        self.right = value % 100

    def __repr__(self):
        return '({}-{})'.format(self.polygon_number, self.value)

    def __eq__(self, other):
        return self.polygon_number == other.polygon_number and self.value == other.value

def p(x, n):
    if x == 3:
        return n * (n + 1) / 2
    elif x == 4:
        return n**2
    elif x == 5:
        return n * (3*n - 1) / 2
    elif x == 6:
        return n * (2*n - 1)
    elif x == 7:
        return n * (5*n - 3) / 2
    elif x == 8:
        return n * (3*n - 2)

def dfs(node, path = [], length = 6):
    path = deepcopy(path)
    path.append(node)
    # print path

    if len(path) == 6:
        print path
        start = path[0]
        if path[0].left == path[-1].right:
            return path
    else:
        explored = set([n.polygon_number for n in path])
        for n in node.next:
            if n.polygon_number in explored:
                continue

            p = dfs(n, deepcopy(path))
            if p:
                return p

def main():
    m = 1
    candidates = [[] for _ in xrange(9)]
    for x in xrange(3, 9):
        n = 0
        while True:
            if 1000 <= p(x, n) <= 9999:
                candidates[x].append(Node(x, p(x, n)))
            elif p(x, n) > 9999:
                break
            n += 1

    for x in xrange(3, 9):
        for y in xrange(3, 9):
            if x == y:
                continue

            for a in candidates[x]:
                for b in candidates[y]:
                    if a.right == b.left:
                        a.next.append(b)

    for i, n in enumerate(candidates[8]):
        print '{}/{}: {}'.format(i + 1, len(candidates[8]), n)
        path = dfs(n)
        if path:
            print sum([n.value for n in path])
            return

    # a = Node(1, 2)
    # b = Node(2, 4)
    # a.next.append(b)
    # print a
    # print b
    # a.next[0].value = 6
    # print a
    # print b
    # print a.next[0] == b

main()
