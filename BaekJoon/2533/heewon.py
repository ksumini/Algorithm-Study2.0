import sys
from collections import defaultdict

sys.setrecursionlimit(1000001)  # 재귀 제한 깊이 설정 (문제 해결에 필요한 경우)
input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)  # 방문 여부 체크 (리스트 - 노드: 방문 여부)
graph = defaultdict(list)

def dfs(node: int) -> tuple:
    visited[node] = True  # 현재 노드 방문 표시

    # ON 카운트 (현재 노드 포함), OFF 카운트 (현재 노드 제외) 초기화
    on, off = 1, 0

    # 연결된 노드 탐색
    for child in [child for child in graph[node] if not visited[child]]:
        # 연결된 노드 (child) 에 대한 DFS 수행 (자식 노드 탐색)
        child_on, child_off = dfs(child)

        # 자식 노드를 포함하는 경우 (ON) 과 제외하는 경우 (OFF) 각각 최소 방법 고려
        on += min(child_on, child_off)
        off += child_on

    # 현재 노드를 기준으로 지도를 밝히는 방법의 수 (ON, OFF) 반환
    return on, off

for _ in range(n-1):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

print(min(dfs(1)))