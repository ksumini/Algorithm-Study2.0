from collections import deque

N, M = map(int, input().split())
graph: list[list[int]] = [[] for _ in range(N + 1)]
indegree: list[int] = [0] * (N + 1)  # 해당 노드를 조건으로 하는 노드의 수

for _ in range(M):
    orders: list[int] = list(map(int, input().split()))[1:]
    for i in range(len(orders) - 1):
        graph[orders[i]].append(orders[i + 1])
        indegree[orders[i + 1]] += 1

q: deque[int] = deque()
result: list[int] = []

# 조건 없는 노드 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    result.append(current)

    for next_node in graph[current]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

# 만약 결과가 N개가 아니라면, 사이클이 존재한다는 의미
if len(result) != N:
    print(0)
else:
    for node in result:
        print(node)
