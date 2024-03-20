"""
[2024-03-14 목요일 문제]
start : 10:30
end : 12:00
"""

"""
- 새로 생성된 정점은 그래프와 무관한 정점이며 다른 그래프로 뻗어나가는 간선밖에 존재하지 않음
    - 그래프는 두 개 이상 존재하므로, 2개 이상 뻗어나가는 간선을 갖되, 들어오는 간선이 없는 점
    - 다른 그래프의 임의의 정점으로 뻗어나감
    - 그래프 순회를 통해 규칙을 찾아야 함
- 도넛 그래프 : 각 정점의 in : 1 / out : 1
- 막대 그래프 : 특정 정점이 in : 1 / out : 0 or in : 0 / out : 1
- 8자 그래프 : 특정 정점의 in or out이 2

1. 새로 생성된 정점을 찾는다.
2. 새로 생성된 정점에 연결된 각 그래프의 정점 집합을 찾는다.
3. 집합 내 정점의 in, out 간선 수를 바탕으로 그래프 유형을 파악한다.
"""

from collections import defaultdict, deque


def validate(root, st_dict, en_dict):
    """
    root로 시작하는 그래프 내 정점을 찾고, 해당 그래프의 유형을 판별하여 반환
    """

    nodes = {root}
    queue = deque([root])

    # BFS로 그래프에 포함된 정점 찾기(DFS 재귀 활용시 최대 재귀 깊이 에러)
    while queue:
        cur = queue.popleft()

        for v in st_dict[cur]:
            if v not in nodes:
                nodes.add(v)
                queue.append(v)

    # 그래프 판별
    for node in nodes:
        # 도넛 그래프의 모든 정점은 in 1 / out 1
        if not (len(st_dict[node]) == 1 and en_dict[node] == 1):
            # in, out 중 하나라도 두 개 이상이면 8자
            if len(st_dict[node]) >= 2 or en_dict[node] >= 2:
                return 3
            # in 1 / out 0 or in 0 out 1 인 경우 막대
            else:
                return 2

    return 1


def solution(edges):
    # 생성된 정점 찾기
    st_dict = defaultdict(list)
    en_dict = defaultdict(int)

    for st, en in edges:
        st_dict[st].append(en)
        en_dict[en] += 1

    for st, lst in st_dict.items():
        if len(lst) >= 2 and st not in en_dict:
            root = st

    answer = [root, 0, 0, 0]  # [정점, 도넛, 막대, 8자]

    # 생성된 정점에서 뻗은 간선 제거
    for en in st_dict[root]:
        en_dict[en] -= 1

    # 그래프 탐색
    for other_root in st_dict[root]:
        idx = validate(other_root, st_dict, en_dict)
        answer[idx] += 1

    return answer
