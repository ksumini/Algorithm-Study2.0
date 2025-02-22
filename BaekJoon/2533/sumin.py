"""
<문제>
정점(Node, Vertex): 사람
엣지(Edge): 관계

새로운 아이디어를 먼저 받아들인 사람: early adaptor
사람들은 ealry adaptor이거나 아니거나인데 아닌 사람은 자신의 모든 친구들이 early adaptor일 때만 아이디어를 받아들인다.

친구 관계 그래프가 트리인 경우(모든 두 정점 사이에 이들을 잇는 경로가 존재하면서 사이클이 존재하지 않는 경우)
친구 관계 트리가 주어졌을 때, 모든 개인이 새로운 아이디어를 수용하기 위해 필요한 최소 early adaptor수를 구해야 한다.

<풀이>
1. dp[u][1]: 노드 u가 얼리 어답터일 때, 서브트리에서 최소 얼리 어답터 수
- 자식 노드들이 어떤 상태든 상관없기 때문에, 모든 자식에서 최솟값
- dp[u][1] = sum(min(dp[v][0], dp[v][1])) for all children v of u

2. dp[u][0]: 노드 u가 얼리 어답터가 아닐 때, 서브트리에서 최소 얼리 어답터 수
- 자식 노드는 반드시 얼리 어답터여야 한다.
- dp[u][0] = sum(dp[v][1]) for all children v of u
"""
# DFS 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 친구 관계 트리의 정점 개수
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n+1)]


def dfs(node, parent):
    dp[node][0] = 0 # node가 얼리 어답터가 아닌 경우
    dp[node][1] = 1 # node가 얼리 어답터인 경우

    for child in graph[node]:
        if child == parent: # base condition
            continue
        dfs(child, node)
        dp[node][0] += dp[child][1] # 자식 노드는 반드시 얼리 어답터
        dp[node][1] += min(dp[child][0], dp[child][1]) # 자식 노드는 자유롭게 선택 가능


# 루트에서 DFS 시작 (임의로 1번 노드를 루트로 설정)
dfs(1, -1)

# 결과 출력
print(min(dp[1][0], dp[1][1]))


# BFS 풀이
import sys
input = sys.stdin.readline
from collections import deque


# 친구 관계 트리의 정점 개수
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DP 테이블 초기화
dp = [[0, 0] for _ in range(n + 1)]

parent = [-1] * (n + 1)
queue = deque([1])
bfs_order = []

# 트리 구조 (1번 노드를 루트 설정)
while queue:
    node = queue.popleft()
    bfs_order.append(node)
    for neighbor in graph[node]:
        if neighbor != parent[node]:
            parent[neighbor] = node
            queue.append(neighbor)

for node in reversed(bfs_order):
    dp[node][0] = 0  # 노드가 얼리 어답터가 아닌 경우
    dp[node][1] = 1  # 노드가 얼리 어답터인 경우

    for child in graph[node]:
        if child == parent[node]:  # 부모 노드로 거슬러 올라가는 것을 방지
            continue
        dp[node][0] += dp[child][1]  # 자식 노드는 반드시 얼리 어답터
        dp[node][1] += min(dp[child][0], dp[child][1])  # 자식 노드는 자유롭게 선택 가능


print(min(dp[1][0], dp[1][1]))