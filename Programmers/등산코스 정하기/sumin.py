"""
<문제>
출입구에서 산봉우리를 방문하고 다시 출입구로 돌아올 때 intensity가 최소가 되는 경로를 찾는 문제
- Intensity: 경로를 구성하는 등산로 중 가장 높은 가중치
- 휴식이 가능한 곳: 쉼터, 산봉우리

<풀이>
풀이 시간: 1시간 30분
1, 출입구에서 출발하는 경로만 탐색하고, 산봉우리에 도달하면 탐색을 중단하는 방식으로 단방향성을 구현
2. intensity를 최소화하는 다익스트라 알고리즘을 사용하여 경로를 탐색(다익스트라 변형)
3. 최소 intensity와 번호가 가장 작은 산봉우리를 반환

<시간 복잡도>
O((n+m)logn) + O(k)
- n: 노드 수
- m: 간선 수
- k: 산봉우리 수
"""
from typing import List
import heapq


def solution(n: int, paths: List, gates: List, summits: List) -> List:
    """
    :param n: 산의 지점 수
    :param paths: 각 등산로의 정보를 담은 2차원 정수 배열
    :param gates: 출입구들의 번호가 담긴 정수 배열
    :param summits: 산봉우리들의 번호가 담긴 정수 배열
    :return: intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호와 intensity의 최솟값을 차례대로 정수 배열에 담아 return
    """
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for a, b, weight in paths: # a에서 b까지 걸리는 시간
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    # 산봉우리 집합
    summit_set = set(summits)

    heap = []
    intensity = [float('inf')] * (n + 1)

    # 출입구를 시작점으로 하는 다익스트라 실행
    for gate in gates:
        heapq.heappush(heap, (0, gate)) # (현재까지의 최대 난이도, 현재 노드)
        intensity[gate] = 0

    while heap:
        current_intensity, node = heapq.heappop(heap)

        if node in summit_set:
            continue  # 산봉우리에 도달하면 더 이상 탐색하지 않음

        # 이미 더 작은 intensity로 방문했다면 스킵
        if current_intensity > intensity[node]:
            continue

        for neighbor, weight in graph[node]:
            max_intensity = max(current_intensity, weight)
            # 아직 방문하지 않았거나 더 작은 intensity로 방문할 수 있는 경우
            if intensity[neighbor] > max_intensity:
                intensity[neighbor] = max_intensity
                heapq.heappush(heap, (max_intensity, neighbor))

    # 산봉우리 중에서 최소 intensity와 번호가 가장 작은 것을 찾기
    min_intensity = float('inf') # 지금까지 확인한 산봉우리 중 가장 작은 intensity
    best_summit = -1

    # 산봉오리를 순회하며 각각의 Intensity 확인
    for summit in summits:
        if intensity[summit] < min_intensity:
            min_intensity = intensity[summit]
            best_summit = summit
        elif intensity[summit] == min_intensity:
            best_summit = min(best_summit, summit)

    return [best_summit, min_intensity]