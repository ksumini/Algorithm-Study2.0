from collections import deque, defaultdict


def make_graph(roads: list) -> dict:
    """
    부대 간 연결. 양 방향
    :param roads: 연결 관계
    :return: 연결 관계 그래프 dictionary
    """
    graph = defaultdict(lambda: [])
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def make_dist(n: int, graph: list, dest: int):
    """
    도착지점(dest) 기준에서 다른 지점들까지 최단 경로 구하기
    :param n: n개 지점
    :param graph: 그래프 dictionary
    :param dest: 도착지점
    :return:
    """
    dist_dict = defaultdict(lambda: -1)
    dist_dict[dest] = 0 # dest->dest는 0 번만에 감

    visited = [False] * (n + 1) # 방문 처리
    q = deque()
    q.append(dest) # dest에서 출발
    visited[dest] = True # 방문 처리
    dist = 0 # 최단 거리
    while True:
        next_q = deque() # dist+1에 해당하는 곳들
        for _ in range(len(q)):
            now = q.popleft()
            dist_dict[now] = dist # dist에 해당하는 곳들
            for next_ in graph[now]:
                if visited[next_] == False:
                    next_q.append(next_)
                    visited[next_] = True # 방문 처리
        if len(next_q) == 0:
            break
        dist += 1
        q = next_q
    return dist_dict


def solution(n, roads, sources, destination):
    """
    params n: 각 지역. 1~n까지
    params roads: 두 지역 왕복할 수 있는 길. (방향성 X, a,b있으면 b,a는 주어지지않음. 중복해서 주는거 없음)
    params sources: 각 부대원이 위치한 서로 다른 지역들
    params destination: 주어진 sources의 원소 순서대로 강철부대로
    """
    answer = [0] * len(sources)
    graph = make_graph(roads)
    dist_dict = make_dist(n, graph, destination)

    for i, s in enumerate(sources):
        answer[i] = dist_dict[s]

    return answer