import sys
input = sys.stdin.readline

from collections import defaultdict


def find(root, p1):
    if root[p1] == p1:
        return p1
    return find(root, root[p1])


def union(network, root, p1, p2):
    p1 = find(root, p1)
    p2 = find(root, p2)

    if p1 > p2:
        root[p1] = p2
        network[p2] += network[p1]
        del network[p1]
        print(network[p2])
    elif p1 == p2:
        print(network[p1])
    else:
        root[p2] = p1
        network[p1] += network[p2]
        del network[p2]
        print(network[p1])



for _ in range(int(input())):
    network = defaultdict(lambda : 1)
    root = {}
    for _ in range(int(input())):
        p1, p2 = input().split()

        if p1 not in root: root[p1] = p1
        if p2 not in root: root[p2] = p2

        union(network, root, p1, p2)
