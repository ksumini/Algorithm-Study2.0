'''
조건)
얼리어답터 x : 모든 친구가 얼리어답터인 경우 아이디어를 받아들임

최소의 수 얼리 어답터
모든 사람이 아이디어를 받아들이게

-트리인 경우 (사이클 존재하지 않은 경우)

return 얼리 어답터의 수
'''
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(graph, node, parent):
    early, not_early = 1, 0  # 현재 노드가 얼리 어답터인 경우, 아닌 경우
    for child in graph[node]:
        if child != parent:
            child_early, child_not_early = dfs(graph, child, node)

            # 현재 노드가 얼리 어답터인 경우, 자식은 얼리 어답터일 수도 있고 아닐 수도 있음
            early += min(child_early, child_not_early)
            # 현재 노드가 얼리 어답터가 아닌 경우, 모든 자식은 반드시 얼리 어답터여야 함
            not_early += child_early

    return [early, not_early]


n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(graph, 1, 0)
print(min(result))

