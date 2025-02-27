import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

before_edge = defaultdict(int)

visited = [False] * (n+1)

answer = []

for _ in range(m):
  _, *seq = list(map(int, input().split()))
  for i in range(len(seq)-1):
      graph[seq[i]].append(seq[i+1])
      before_edge[seq[i+1]] += 1

q = deque([i for i in range(1, n+1)])

cnt = 0

while q:
    singer = q.popleft()

    if cnt > n:
        break

    if before_edge[singer] == 0:
        answer.append(singer)
        for next_ in graph[singer]:
            before_edge[next_] -= 1
        cnt = 0
    else:
        q.append(singer)
        cnt += 1


if n == len(answer):
    for i in answer:
        print(i)
else:
    print(0)