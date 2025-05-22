# 간선이 모두 양수
# 한 노드에서 다른 한 노드로 가는 최소한의 거리
# 다익스트라 알고리즘

import sys
read_line = sys.stdin.readline

import heapq
from collections import defaultdict


def dijkstra(n, bus, start, end):
    costs = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    q = [[0, start, [start]]] # weight, node

    while q:
        cost, node, path = heapq.heappop(q)
        if visited[node]:
            continue

        visited[node] = True
        costs[node] = cost
        if node == end:
            return cost, len(path), path
            

        for next_node, next_cost in bus[node]:
            total_cost = cost + next_cost
            if not visited[next_node] and costs[next_node] > total_cost:
                next_path = path.copy()
                next_path.append(next_node)
                heapq.heappush(q, [total_cost, next_node, next_path])


n = int(read_line()) # 도시의 개수
m = int(read_line()) # 버스의 개수

# 버스 정보
bus =  defaultdict(list)
for _ in range(m):
    a, b, c = map(int, read_line().split())
    bus[a].append((b, c))

a, b = map(int, read_line().split()) # 출발지와 도착지

cost, num_city, path = dijkstra(n, bus, a, b)
print(cost)
print(num_city)
print(*path)
