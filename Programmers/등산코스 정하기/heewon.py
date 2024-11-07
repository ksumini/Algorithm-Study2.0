from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    # 그래프 초기화: 각 노드의 인접 노드와 시간을 딕셔너리 형태로 저장
    graphs = defaultdict(dict)
    for i, j, w in paths:
        graphs[i][j] = w
        graphs[j][i] = w

    # 출입구(gates)와 봉우리(summits)를 집합으로 변환하여 효율적으로 탐색 가능하게 함
    gates, summits = set(gates), set(summits)

    # 다익스트라 알고리즘을 이용한 최단 경로 계산 함수
    def dijkstra():
        # 모든 노드의 최단 거리를 무한대로 초기화
        distances = {node: float('INF') for node in graphs}
        # 우선순위 큐 초기화
        q = []
        # 출입구들을 큐에 넣고, 거리 0으로 초기화
        for gate in gates:
            heapq.heappush(q, (0, gate))
            distances[gate] = 0

        # 다익스트라 알고리즘 시작
        while q:
            cur_distance, now = heapq.heappop(q)

            # 현재 노드가 봉우리인 경우 탐색 중단 (봉우리는 목적지), 현재 노드의 거리보다 큰 경우는 스킵
            if now in summits or cur_distance > distances[now]:
                continue

            # 현재 노드의 인접 노드 탐색
            for next_, time in graphs[now].items():
                # 인접 노드가 출입구일 경우 스킵 (출입구 간 경로는 필요 없음)
                if next_ in gates:
                    continue
                # 인접 노드까지의 거리를 현재 거리와 해당 간선의 가중치 중 큰 값으로 설정
                distance = max(cur_distance, time)
                # 더 짧은 경로가 발견되면 거리 갱신하고 우선순위 큐에 추가
                if distance < distances[next_]:
                    distances[next_] = distance
                    heapq.heappush(q, (distances[next_], next_))

        # 결과로 반환할 봉우리와 최소 거리 초기화
        answer = [0, float('INF')]
        # 봉우리들 중에서 가장 짧은 거리를 가진 봉우리를 찾음
        for summit in sorted(summits):
            if answer[1] > distances[summit]:
                answer = [summit, distances[summit]]
        return answer

    # 다익스트라 함수 호출하여 최적의 봉우리와 거리를 반환
    return dijkstra()