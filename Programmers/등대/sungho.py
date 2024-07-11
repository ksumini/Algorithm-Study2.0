from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 늘리기


def make_graph(lighthouse: list) -> dict:
    graph = defaultdict(lambda: set())
    for u, v in lighthouse:
        graph[u - 1].add(v - 1)  # 1번부터 시작이라 -1 해줬음
        graph[v - 1].add(u - 1)
    return graph


def solution(n: int, lighthouse: list) -> int:
    answer = 0
    graph = make_graph(lighthouse)

    visited = [0] * n

    def dfs(u):
        visited[u] = 1
        on, off = 1, 0

        for v in graph[u]:
            if visited[v] == 0:
                on_v, off_v = dfs(v)
                on += min(on_v, off_v)  # s 등대가 켜지면 연결된 게 켜지든 안 켜지든 상관 없음
                off += on_v  # s가 켜진게 아니라면 연결된게 켜져있어야함

        return on, off

    return min(dfs(0))
