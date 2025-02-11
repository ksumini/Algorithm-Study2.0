import sys
from collections import defaultdict, deque

input = sys.stdin.readline

graph = defaultdict(set)
for _ in range(int(input()) - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

leaf_nodes = deque([idx for idx, nodes in graph.items() if len(nodes) == 1])
is_light = [0] * (len(graph) + 1)

while leaf_nodes:
    leaf_node = leaf_nodes.popleft()
    for next_node in graph[leaf_node]:
        for neighbor in graph[next_node]:
            if neighbor == leaf_node:
                continue
            graph[neighbor].remove(next_node)
            if len(graph[neighbor]) == 1:
                leaf_nodes.append(neighbor)
        is_light[next_node] = 1
        del graph[next_node]
    del graph[leaf_node]

print(sum(is_light))
