from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, len(order)-1):
        graph[order[i]].append(order[i+1])
        indegree[order[i+1]] += 1

result = []
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    result.append(current)

    for i in graph[current]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) == n:
    print(*result, sep='\n')
else:
    print(0)
