from sys import stdin
from collections import deque

MAX_SIZE = 1_000_000 + 1
EARLY_ADOPT = 1
NORMAL = 0
ROOT = 1

n: int = int(stdin.readline())
tree: list[list[int]] = [ [] for _ in range(n+1)]
dp: list[list[int]] = [ [0] * 2 for _ in range(n+1)]
visited: list[bool] = [False]  *  (n+1)
parent: list[int] = [-1] * (n + 1)

# DFS -> recursion depth Limit 초과


# def dfs(index: int):
#     global visited, tree, dp
#     visited[index] = True
#     dp[index][EARLY_ADOPT] = EARLY_ADOPT
#
#     for child in tree[index]:
#         if visited[child]:
#             continue
#         dfs(child)
#         dp[index][EARLY_ADOPT] +=  min(dp[child][EARLY_ADOPT], dp[child][NORMAL])
#         dp[index][NORMAL] += dp[child][EARLY_ADOPT]
    # print(index,min(dp[index]), dp[index] )


for _ in range(n-1):
    start, end = map(int, stdin.readline().split())
    tree[start].append(end)
    # 쌍방 관계로 추가
    tree[end].append(start)


# BFS
q: deque[int] = deque([ROOT])
visited[ROOT] = True


orders: list[int] = []

while q:
    index = q.popleft()
    orders.append(index)
    for child in tree[index]:
        if visited[child]:
            continue

        visited[child] = True
        parent[child] = index
        q.append(child)


while orders:
    index = orders.pop()
    dp[index][EARLY_ADOPT] = EARLY_ADOPT

    for child in tree[index]:
        if child == parent[index]:
            continue
        dp[index][EARLY_ADOPT] += min(dp[child][EARLY_ADOPT], dp[child][NORMAL])
        dp[index][NORMAL] += dp[child][EARLY_ADOPT]


print(min(dp[ROOT]))