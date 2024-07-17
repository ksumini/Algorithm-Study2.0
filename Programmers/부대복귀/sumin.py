"""
<문제>
각 지역은 유일한 번호로 구분된다.
두 지역 간의 길을 통과하는데 걸리는 시간은 모두 1로 동일하다.
지도 정보를 이용해 최단 시간에 부대로 복귀하고자 한다.
되돌아오는 경로가 없어져, 복귀가 불가능한 부대원도 있을 수 있다

<제한 사항>
- 3 <= n <= 100,000
    - 각 지역은 정수 1부터 n까지의 번호로 구분된다.
- 2 <= roads의 길이 <= 500,000
    - roads의 원소의 길이 = 2
    - [a, b]의 형태로 두 지역 a,b가 서로 왕복할 수 있음을 의미한다.
    - [a, b]와 [b, a]가 중복해서 주어지지 않는다.
- 1 <= sources의 길이 <= 500
    - 1 <= sources[i] <= n
- 1 <= destination <= n

<풀이 시간>
30분

<풀이>
n개의 지역(노드)와 roads(간선)
각 지역간의 거리는 1이기 때문에 BFS를 이용해 최단 거리를 구한다.
sources의 길이가 최대 500이고, 각 부대원(k)마다 BFS를 수행하면 시간복잡도는 O(k * (V + E))가 돼 시간초과가 날 수 밖에 없다.

하지만, 강철부대는 하나 밖에 없기 때문에
강철부대에서 BFS를 통해 모든 지역에 대한 최단 거리를 구하면 시간복잡도는 O(V + E + K)로 해결이 가능하다.

<시간 복잡도>
O(V + E + K)
- V: 지역의 개수
- E: roads의 길이
- K: sources의 길이
"""
from collections import deque, defaultdict


def solution(n: int, roads: list, sources: list, destination: int) -> list:
    """
    :param n: 강철부대가 위치한 지역을 포함한 총 지역의 수
    :param roads: 두 지역을 왕복할 수 있는 길 정보를 담은 2차원 정수 배열
    :param sources: 각 부대원이 위치한 서로 다른 지역들을 나타내는 정수 배열
    :param destination: 강철부대의 지역
    :return: 주어진 sources의 원소 순서대로 강철부대로 복귀할 수 있는 최단 시간을 담은 배열
    """
    # 1. 그래프(노드와 간선간의 관계)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 2.  BFS를 실행해 모든 지역에 대한 최단 거리 계산
    distances = [-1] * (n + 1) # 초기화
    distances[destination] = 0 # 시작 지점을 강철부대로 설정
    q = deque([destination])

    while q:
        cur_node = q.popleft()
        for adj_node in graph[cur_node]:
            if distances[adj_node] == -1: # 방문하지 않은 노드에 대해서만 처리
                distances[adj_node] = distances[cur_node] + 1
                q.append(adj_node)

    # 각 source에 대한 최단 거리 결과
    return [distances[source] for source in sources]