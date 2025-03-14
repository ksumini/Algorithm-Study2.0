from collections import defaultdict

import sys
sys.setrecursionlimit(1000000)


def generate_graph(edges):
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    return graph


# 트리별로 구분
def divide_by_group(groups, group_num, cur_node, graph, visited):
    if len(graph[cur_node]) % 2 == 0:  # 자식 노드 개수: 짝수
        if cur_node % 2 == 0:  # 현재 노드 정수가 짝수 -> 홀짝
            groups[group_num][0].append(cur_node)
        else:  # 역홀짝
            groups[group_num][1].append(cur_node)
    else:  # 자식 노드 개수: 홀수
        if cur_node % 2 == 0:  # 역홀짝
            groups[group_num][1].append(cur_node)
        else:  # 홀짝
            groups[group_num][0].append(cur_node)
    visited.add(cur_node)

    for nxt_node in graph[cur_node]:
        if nxt_node in visited:
            continue
        divide_by_group(groups, group_num, nxt_node, graph, visited)

    return groups, visited


def solution(nodes, edges):
    answer = [0, 0]

    groups = defaultdict(lambda: [[],[]])  # [홀짝, 역홀짝]
    visited = set()
    graph = generate_graph(edges)
    num = 0

    for node in nodes:
        if node in visited:
            continue

        # 자식 노드가 없는 경우 (개수 0)
        if node not in graph:
            if node % 2 == 0:  # 홀짝
                answer[0] += 1
            else:  # 역홀짝
                answer[1] += 1
            continue

        groups, visited = divide_by_group(groups, num, node, graph, visited)
        num += 1  # 트리 그룹 넘버 갱신

    for g1, g2 in groups.values():
        # 트리마다 한 개의 노드만이 홀짝 또는 역홀짝일 때, 모든 트리가 같은 성질을 가짐
        # 노드가 두 개, 각각 홀짝, 역홀짝일 경우 둘 다 루트 노드가 될 수 있음.
        if len(g1) == 1:
            answer[0] += 1
        if len(g2) == 1:
            answer[1] += 1

    return answer