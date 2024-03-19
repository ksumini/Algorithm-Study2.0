"""
<풀이 시간>
2시간 30분

<제한 사항>
- 1 ≤ edges의 길이 ≤ 1,000,000
- edges의 원소는 [a,b] 형태이며, a번 정점에서 b번 정점으로 향하는 간선이 있다는 것을 나타낸다.
- 1 ≤ a, b ≤ 1,000,000
- 문제의 조건에 맞는 그래프가 주어진다.
- 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상이다.

<문제 풀이>
생성된 정점이 없다고 했을 때, 각 그래프의 정점과 간선 특징
1) 생성된 정점
    - 나가는 간선: 2개 이상 (그래프의 수의 합이 2개 이상이기 때문)
    - 들어오는 간선: 0개

2) 도넛 모양 그래프
(시작 정점과 마지막 정점을 제외한 정점의 특징)
    - 나가는 간선: 1개
    - 들어오는 간선: 1개

3) 막대 모양 그래프
- 시작 정점: 나가는 간선(1개)
- 마지막 정점: 들어오는 간선(1개)
- 그 외, 각 정점은 들어오는 간선(1개), 나가는 간선(1개)

4) 8자 모양 그래프
- 가운데 하나의 정점만 들어오는 간선이 두 개, 나가는 간 선이 두 개
- 그 외,정점은 들어오는 간선과 나가는 간선이 모두 하나씩 존재


1. 생성된 정점 찾기(들어오는 간선이 없고, 나가는 간선이 있는 정점으로 하나밖에 존재하지 않음)
2. 생성된 정점에서 나가는 간선 모두 제거
3. 막대 모양 그래프의 시작 정점과 마지막 정점을 찾는다.

<시간 복잡도>
O(V+E)
"""
from typing import List


def solution(edges: List[List[int]]):
    # 각 정점의 들어오는 간선과 나가는 간선의 수를 셀 딕셔너리
    nodes = set()
    for a, b in edges:
        nodes.add(a)
        nodes.add(b)
    in_degree = {node: 0 for node in nodes}
    out_degree = {node: 0 for node in nodes}

    # 간선 정보로부터 in_degree와 out_degree를 셈
    for a, b in edges:
        # a -> b 간선이 존재하므로 a의 나가는 간선 수 1 증가, b의 들어오는 간선 수 1 증가
        out_degree[a] += 1
        in_degree[b] += 1

    # 생성된 정점 찾기 (들어오는 간선이 없고, 나가는 간선이 두 개 이상인 정점)
    created_vertex = [vertex for vertex in out_degree if out_degree[vertex] > 1 and in_degree[vertex] == 0][0]

    # 생성된 정점에서 나가는 간선 모두 제거하기
    total_graph_count = 0 # 모양 그래프 전체 개수
    for a, b in edges:
        if a == created_vertex:
            total_graph_count += 1
            in_degree[b] -= 1
            out_degree[a] -= 1

    # 막대 모양 그래프의 개수 찾기 (생성 정점을 제외한 들어오는(나가는) 간선이 없는 정점 = 막대 모양 그래프의 개수)
    bar_graph_cnt = 0
    for vertex in in_degree:
        if vertex == created_vertex: continue
        if in_degree[vertex] == 0:
            bar_graph_cnt += 1

    # 8자 모양 그래프의 개수 찾기 (들어오는 간선과 나가는 간선이 2개인 정점 = 8자 모양 그래프의 개수)
    figure_eight_graph_cnt = 0
    for a, b in edges:
        if in_degree[a] == 2 and out_degree[a] == 2:
            figure_eight_graph_cnt += 1
    figure_eight_graph_cnt //= 2

    # 도넛 모양 그래프의 개수는 전체 개수에서 막대와 8자 모양을 뺀 것
    donut_graph_count = total_graph_count - bar_graph_cnt - figure_eight_graph_cnt

    # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
    answer = [created_vertex, donut_graph_count, bar_graph_cnt, figure_eight_graph_cnt]

    return answer


# test case
edges1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
edges2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]


# 결과 출력
print(solution(edges1))  # [2, 1, 1, 0]
print(solution(edges2))  # [4, 0, 1, 2]
