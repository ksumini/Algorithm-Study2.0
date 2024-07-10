import sys
from collections import defaultdict
sys.setrecursionlimit(1000001)  # 재귀 제한 깊이 설정 (문제 해결에 필요한 경우)


def solution(n: int, lighthouse: list) -> int:
    """
    지도 정보 (등대 위치 연결) 를 담은 리스트 `lighthouse` 와 전체 지도 크기 `n`을 입력받아 
    최소 점등 수를 계산하는 함수입니다.

    Args:
        n: 전체 지도의 크기입니다.
        lighthouse: 각 등대의 위치를 연결하는 정보가 담긴 리스트입니다. (쌍 (a, b) 형태)

    Returns:
        지도 전체를 밝히기 위해 필요한 최소 등대 개수입니다.
    """

    # 전역 변수 선언
    global graph, visited
    graph = defaultdict(list)  # 연결 관계 표현 (딕셔너리 - 노드: 연결된 노드 리스트)
    visited = [False] * (n + 1)  # 방문 여부 체크 (리스트 - 노드: 방문 여부)

    # 연결 관계 초기화 (등대 위치 정보를 기반으로 그래프 생성)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    # 탐색 시작 노드는 1번째 노드 (어떤 노드든 가능)
    return min(dfs(1))


def dfs(node: int) -> tuple:
    """
    깊이 우선 탐색 (DFS) 알고리즘을 수행하여 해당 노드를 기준으로 
    지도를 밝히는 방법의 수 (ON, OFF) 를 계산하는 함수입니다.

    Args:
        node: 현재 탐색 대상 노드입니다.

    Returns:
        해당 노드를 기준으로 지도를 밝히는 방법의 수 (ON: 현재 노드를 포함, OFF: 현재 노드를 제외) 를 튜플 형태로 반환합니다.
    """

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


print(solution(8, 	[[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, 	[[4, 1], [5, 1], [5, 6], [7, 6],
      [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
