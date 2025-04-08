import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
LOG = 21 # 100,000 기준으로 log(100,000)


graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n+1)
parent = [[0] * (n+1) for _ in range(LOG)]

def bfs(root):
    queue = deque([root])
    visited = [False] * (n + 1)
    visited[root] = True
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                depth[next_node] = depth[node] + 1
                parent[0][next_node] = node
                queue.append(next_node)

bfs(1)  # 루트는 1번 노드로 가정

for k in range(1, LOG):
    for v in range(1, n + 1):
        parent[k][v] = parent[k - 1][parent[k - 1][v]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for k in reversed(range(LOG)):
        if depth[u] - depth[v] >= (1 << k):
            u = parent[k][u]

    if u == v:
        return u

    for k in reversed(range(LOG)):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    return parent[0][u]

M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
