from collections import defaultdict
from sys import stdin

def find(name):
    if friends[name] == name:
        return name
    else:
        parent = find(friends[name])
        friends[name] = parent # 경로 압축
        return parent


def union(name1, name2):
    name1, name2 = (name2, name1) if name2 < name1 else (name1, name2) # 사전 순으로 정렬
    parent1 = find(name1)
    parent2 = find(name2)
    if parent1 != parent2:
        friends[parent2] = parent1
        counts[parent1] += counts[parent2]



input = stdin.readline
test_case = int(input())
for _ in range(test_case):
    friends = {}
    counts = defaultdict(lambda :1)
    n = int(input())

    for _ in range(n):
        friend1, friend2 = input().split()

        if friend1 not in friends:
            friends[friend1] = friend1

        if friend2 not in friends:
            friends[friend2] = friend2

        union(friend1, friend2)
        print(counts[find(friend1)])
