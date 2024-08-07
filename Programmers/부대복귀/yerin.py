from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    # 목적지로부터의 거리를 저장하는 배열.
    # 부대원이 위치한 마을 별 거리를 인덱스로 접근할 수 있도록 (n+1)크기의 리스트 생성
    dist_info = [-1 for _ in range(n + 1)]
    # 근처 마을 목록을 저장하는 리스트
    towns = [[] for _ in range(n + 1)]

    # 근처 마을 리스트 삽입
    for a, b in roads:
        towns[a].append(b)
        towns[b].append(a)

    q = deque([(destination, 0)])  # 목적지에서부터 출발. (목적지, 거리)
    dist_info[destination] = 0

    while q:
        loc, dist = q.popleft()

        for nx in towns[loc]:
            if dist_info[nx] == -1:  # 방문한 적이 없을 때
                q.append((nx, dist + 1))
                dist_info[nx] = dist + 1  # 지역 ~ 목적지 최단 거리

    for sc in sources:
        answer.append(dist_info[sc])

    return answer


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
