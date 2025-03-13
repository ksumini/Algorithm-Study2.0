from collections import deque


def bfs(start, graph):
    visited = [-1] * len(graph)
    queue = deque([(start, 0)])  # (노드, 거리)
    visited[start] = 0
    farthest_node = start
    max_distance = 0

    while queue:
        node, dist = queue.popleft()

        # 최대 거리 갱신
        if dist > max_distance:
            max_distance = dist
            farthest_node = node

        # 다음 노드 탐색
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = dist + weight
                queue.append((next_node, dist + weight))

    return farthest_node, max_distance


V = int(input())
edges = []

graph = [[] for _ in range(V + 1)]

for _ in range(V):
    edge = list(map(int, input().split()))
    node = edge[0]
    for i in range(1, len(edge) - 1, 2):
        start, end = edge[i], edge[i + 1]
        graph[node].append((start, end))

farthest_node_from_start, _ = bfs(1, graph)

_, diameter = bfs(farthest_node_from_start, graph)

# 지름 출력
print(diameter)