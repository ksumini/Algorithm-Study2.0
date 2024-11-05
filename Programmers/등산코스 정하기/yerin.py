'''
n개의 지점
[출입구, 쉽터, 산봉우리]
양방향 통행 가능
휴식 : 쉼터, 산봉우리
intensity : 휴식 없이 이동해야 하는 시간 중 가장 긴 시간

출입구 ~ 산봉우리 ~ 출입구
출입구, 산봉우리 모두 하나씩만 갈 수 있음
intensity 최소

풀이 => 출발지에서 산봉우리까지의 최소 시간 구하고 * 2
'''
import heapq
from collections import deque


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    # 이후 In 함수를 사용하기 위해 set으로 변환
    gates_set = set(gates)
    summits_set = set(summits)
    min_intensity_to_summit = [float('inf'), float('inf')]

    # 양방향 그래프 생성
    for n1, n2, dist in paths:
        graph[n1].append([n2, dist])
        graph[n2].append([n1, dist])

    intensity_by_node = [-1] * (n + 1)  # 지점별 강도
    q = deque()

    # 출발 지점을 모두 강도 0으로 설정
    for gate in gates_set:
        q.append(gate)
        intensity_by_node[gate] = 0

    while q:
        node = q.popleft()
        for next_node, dist in graph[node]:
            # 다음 노드가 출입구인 경우 제외
            if next_node in gates_set:
                continue
            # 강도 더 큰 값으로 업데이트
            intensity = max(dist, intensity_by_node[node])
            # 다음 노드가 산봉우리일 때, 최소 강도로 업데이트. 이 때 산봉우리에서 다른 지점으로 갈 순 없으므로 q 삽입 x.
            # [강도, 산봉우리 지점 번호]
            if next_node in summits_set:
                min_intensity_to_summit = min(min_intensity_to_summit, [intensity, next_node])
            else:
                # 강도가 초기값이거나 이전에 기록된 강도보다 현재 강도가 더 작은 낮은 경우 업데이트
                if intensity_by_node[next_node] == -1 or intensity < intensity_by_node[next_node]:
                    intensity_by_node[next_node] = intensity
                    q.append(next_node)

    return min_intensity_to_summit[::-1]


if __name__ == '__main__':
    print(solution(	6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
