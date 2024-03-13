"""
https://school.programmers.co.kr/learn/courses/30/lessons/258711
"""


def solution(edges):
    """
    - 약 2시간 풀이 후 실패로 답지 참조
    - 초기 접근
        - DFS로 접근하되, 방문마다 visited 배열의 값을 갱신하여 특정 조건에서 종료
        - 이후 시작, 8자, 도넛, 막대 각각의 조건을 찾으려했음
            - 시작의 경우 본인 노드는 딱 한번 방문, 연결된 나머지 노드들은 전부 방문
            - 막대의 경우 본인 노드만 방문
            - 8자와 도넛의 규칙을 찾지 못했음
                - 하나를 찾으면 다른 하나가 틀리는 현상 발생 ...
        - 애초에 입력의 길이가 100만으로 매우 길어 완전탐색으로 풀이가 어렵다는 것을 인지하지 못함

    - 힌트
        - 방문을 할 필요가 없음, 나가고 들어온 간선의 수만 파악하는 것이 핵심
            - 시작 노드에서 모든 그래프들이 생성되기 때문임
                - 즉 시작 노드에서 나가는 간선의 수가 총 그래프의 개수
                - 이 때문에 모든 방문을 할 필요가 없는 것
                - 문제를 대충 읽어 이 부분을 놓친 것이 풀이 실패의 큰 원인 중 하나 인것 같음
        - 또한 도넛형 그래프의 경우 복잡하므로, 8자형과 막대기형을 찾고 시작 노드의 간선 수에서 빼버림
    """
    from collections import defaultdict

    dic = defaultdict(lambda: [0, 0])  # [나가는 간선의 수, 들어온 간선의 수]

    for a, b in edges:
        dic[a][0] += 1  # a -> b로 나가는 간선의 수
        dic[b][1] += 1  # a -> b로 들어온 간선의 수

    start, donut, stick, eight = 0, 0, 0, 0
    for node, item in dic.items():
        give, take = item

        # 기준 노드는 들어오는 것이 없고 나가는게 2개 이상
        if give >= 2 and take == 0:
            start = node

        # 막대기형 : 마지막 도착 노드가 받기만 함
        elif give == 0 and take >= 1:
            stick += 1

        # 8자형 : 나가고 들어온 간선의 개수가 2개 이상
        elif give >= 2 and take >= 2:
            eight += 1

    total = dic[start][0]  # 총 그래프의 개수 = 시작 노드의 나가는 간선의 수
    donut = total - stick - eight
    return start, donut, stick, eight
