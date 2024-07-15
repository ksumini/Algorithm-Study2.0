'''
x, y : 자연수
return 최소 연산 횟수(x --> y)
불가능 --> -1
'''
from collections import deque, defaultdict


def bfs(x, y, n):
    q = deque([(x, 0)])
    visited = defaultdict(lambda: float("inf"))

    while q:
        cur_x, cnt = q.popleft()

        for nx in [cur_x + n, cur_x * 3, cur_x * 2]:
            if nx == y:
                return cnt + 1
            # if nx < y:
            #     if nx in visited and visited[nx] < cnt + 1:
            #         continue
            #     q.append((nx, cnt + 1))
            #     visited[nx] = cnt + 1
            if nx < y and visited[nx] > cnt + 1:
                q.append((nx, cnt + 1))
                visited[nx] = cnt + 1
    return -1


def solution(x, y, n):
    if x == y:
        return 0
    # x가 짝수이고 n이 짝수일 때 y는 홀수이면 불가능
    if x % 2 == 0 and n % 2 == 0 and y % x != 0:
        return -1

    return bfs(x, y, n)

print(solution(10, 40, 5))
print("---")
print(solution(2, 5, 4))
