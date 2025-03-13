import sys

sys.setrecursionlimit(1000000)


def dfs(u, count, graph, visited):
    visited[u] = True
    farthest_vertex, max_dist = u, count

    for nv, nd in graph[u]:
        if not visited[nv]:
            vertex, dist = dfs(nv, count + nd, graph, visited)
            if dist > max_dist:
                farthest_vertex, max_dist = vertex, dist

    return farthest_vertex, max_dist


def diameter(v, graph):
    visited = [False] * (v + 1)
    # 가장 먼 정점을 찾음
    start = dfs(1, 0, graph, visited)[0]

    visited = [False] * (v + 1)
    # 트리의 지름
    return dfs(start, 0, graph, visited)[1]


input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp) - 1, 2):
        graph[tmp[0]].append((tmp[i], tmp[i + 1]))
        graph[tmp[i]].append((tmp[0], tmp[i + 1]))  # 양방향

print(diameter(V, graph))
