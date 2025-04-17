from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().split())
m = len(str(n))

q = deque()
q.append((str(n), 0))
visited = set()
visited.add((str(n), 0))
result = -1

while q:
    number, count = q.popleft()

    if count == k:
        result = max(result, int(number))
        continue

    length = len(number)
    for i in range(length):
        for j in range(i + 1, length):
            number_list = list(number)
            number_list[i], number_list[j] = number_list[j], number_list[i]
            if number_list[0] == '0':  # 맨앞이 0
                continue
            next = ''.join(number_list)
            if (next, count + 1) not in visited:
                visited.add((next, count + 1))
                q.append((next, count + 1))

print(result)
