import sys
from collections import defaultdict, deque

input = sys.stdin.readline

graph = defaultdict(set)
for _ in range(int(input()) - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

leaf_nodes = deque([idx for idx, nodes in graph.items() if len(nodes) == 1])
is_early = [0] * (len(graph) + 1)

# Leaf node가 얼리 어답터인건 이득이 없음
while leaf_nodes:
    leaf_node = leaf_nodes.popleft()
    for next_node in graph[leaf_node]:
        # next_node는 얼리 어답터
        for neighbor in graph[next_node]:
            if neighbor == leaf_node:
                continue
            # next_node는 얼리 어답터이기 때문에 leaf node가 아닌 neighbor에는 아무 영향을 안 끼침
            graph[neighbor].remove(next_node)
            if len(graph[neighbor]) == 1:
                leaf_nodes.append(neighbor)
        is_early[next_node] = 1
        # 더 이상 고려 하지 않아도 되는 node 삭제
        del graph[next_node]
    del graph[leaf_node]

print(sum(is_early))
