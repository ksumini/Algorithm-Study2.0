def product(*args, repeat):
    pools = [arg for arg in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def solution(clockHands):
    answer = float('INF')
    N = len(clockHands)
    
    for p in product(range(4), repeat=N):
        now = [row[:] for row in clockHands]
        cnt = 0
        
        # 첫 번째 행의 시계 방향을 설정합니다.
        for i in range(N):
            clockwise(now, i, 0, p[i], N)
            cnt += p[i]
        
        # 나머지 행을 설정합니다.
        for j in range(1, N):
            turn = [(4 - ch) % 4 for ch in now[j-1]]    # 시계 위치 3(9시) : 1번 회전((4-1)%4)
            for k in range(N):  # 각각의 열 값 확인
                clockwise(now, k, j, turn[k], N)
                cnt += turn[k]
        
        # 마지막 행의 시계 방향만 확인합니다. - 위의 모든 시계를 맞췄기 때문에
        if sum(now[N-1]) == 0:
            answer = min(answer, cnt)
    
    return answer

def clockwise(clockHands, x, y, time, N):
    clockHands[y][x] = (clockHands[y][x] + time) % 4                        # 가운데
    if x > 0:       clockHands[y][x-1] = (clockHands[y][x-1] + time) % 4    # 서
    if y > 0:       clockHands[y-1][x] = (clockHands[y-1][x] + time) % 4    # 북
    if x < N - 1:   clockHands[y][x+1] = (clockHands[y][x+1] + time) % 4    # 동
    if y < N - 1:   clockHands[y+1][x] = (clockHands[y+1][x] + time) % 4    # 남

# def print_(clockHands):
#     for row in clockHands:
#         print(*row)
#     print()
