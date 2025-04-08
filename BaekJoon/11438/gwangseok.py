import sys
input = sys.stdin.readline
from collections import defaultdict, deque


class Node:
    def __init__(self, num, depth, num_parents):
        self.num = num
        self.depth = depth
        self.parents = [-1] * num_parents


def find_lca(nodes, num_parents, node1, node2):
    if nodes[node1].depth < nodes[node2].depth:
        # node1의 depth를 더 깊게 설정
        node1, node2 = node2, node1

    depth_diff = nodes[node1].depth - nodes[node2].depth
    if depth_diff != 0:
        bit_diff = bin(depth_diff)[:1:-1]  # bit만 역순으로 만듦.
        for idx, cur_bit in enumerate(bit_diff):
            if cur_bit == '1': 
                node1 = nodes[node1].parents[idx]
    
    if node1 == node2:
        return node1

    for idx in range(num_parents - 1, -1, -1):
        if nodes[node1].parents[idx] != nodes[node2].parents[idx]:
            node1 = nodes[node1].parents[idx]
            node2 = nodes[node2].parents[idx]
    
    return nodes[node1].parents[0]


N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

num_parents = 0
v = 1
while v < N:
    v *= 2
    num_parents += 1

nodes = [None] * (N + 1)  # [i] = [depth, node_parent]
nodes[1] = Node(1, 0, num_parents)

is_visited = [False] * (N + 1)
q = deque([])
q.append(1)
is_visited[1] = True


while q:
    cur_node = q.popleft()
    for next_node in graph[cur_node]:
        if is_visited[next_node] is False:
            is_visited[next_node] = True
            q.append(next_node)
            nodes[next_node] = Node(next_node, nodes[cur_node].depth + 1, num_parents)
            nodes[next_node].parents[0] = cur_node

for parent_idx in range(1, num_parents):
    for node_idx in range(2, N+1):
        half_jump_node = nodes[node_idx].parents[parent_idx - 1]
        nodes[node_idx].parents[parent_idx] = nodes[half_jump_node].parents[parent_idx - 1]           


M = int(input())
for _ in range(M):
    node1, node2 = map(int, input().split())
    print(find_lca(nodes, num_parents, node1, node2))
