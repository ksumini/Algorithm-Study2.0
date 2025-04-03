import sys
from collections import defaultdict


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, size, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        if size[root_a] < size[root_b]:
            parent[root_a] = root_b
            size[root_b] += size[root_a]
        else:
            parent[root_b] = root_a
            size[root_a] += size[root_b]

    return size[find(parent, a)]


def main():
    input = sys.stdin.readline
    t = int(input().strip())

    for _ in range(t):
        f = int(input().strip())
        parent = {}
        size = {}

        for _ in range(f):
            a, b = input().strip().split()
            if a not in parent:
                parent[a] = a
                size[a] = 1
            if b not in parent:
                parent[b] = b
                size[b] = 1

            print(union(parent, size, a, b))


if __name__ == "__main__":
    main()
