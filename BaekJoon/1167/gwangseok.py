import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node, tree, visited, cur_weight, max_weight, max_node=None):
    visited[node] = True
    if len(tree[node]) == 1:
        if cur_weight > max_weight:
            max_node = node
            max_weight = cur_weight
            return max_weight, max_node
    
    for n, w in tree[node]:
        if not visited[n]:
            max_weight, max_node = dfs(n, tree, visited, cur_weight + w, max_weight, max_node)
        
    return max_weight, max_node


V = int(input()) # 2 ~ 100,000
tree = {}

for _ in range(V):
    data = list(map(int, input().split()))    
    node = data[0]
    tree[node] = []
    for i in range(1, len(data)-1, 2):
        tree[node].append((data[i], data[i+1]))
    

visited = [False] * (V+1)
visited[1] = True

_, max_node = dfs(1, tree, visited, 0, 0)

visited = [False] * (V+1)
visited[max_node] = True
max_weight, _ = dfs(max_node, tree, visited, 0, 0)

print(max_weight)
