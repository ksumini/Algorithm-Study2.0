def solution(n, m, x, y, r, c, k):
    # (r,c), (x,y) 사이 거리
    dist = abs(r - x) + abs(c - y)
    rest = k - dist

    # 거리가 k보다 크거나 남은 횟수가 홀수인 경우(왕복 불가)
    if dist > k or rest % 2 != 0:
        return 'impossible'

    # 출발 지점에서 도착 지점까지의 방향별 횟수
    d_cnt, l_cnt, r_cnt, u_cnt = 0, 0, 0, 0
    if x < r:
        d_cnt = r - x
    else:
        u_cnt = x - r
    if y > c:
        l_cnt = y - c
    else:
        r_cnt = y - c

    # rest만큼 더 이동해야 하므로 추가 거리 계산
    # 이 때, 순서가 높은 d, l을 기준으로 생각
    # 격자 내부에서만 이동할 수 있도록 함.
    # 아래로 향하는 d의 경우 x,r 중 가장 아래에 있는 값을 기준으로 더 이동할 수 있는 거리를 계산. 만일 남은 거리가 그보다 작다면 남은 거리의 절반만큼만 이동할 수 있도록 min처라
    # l의 경우에도 동일. 더 왼쪽에 있는 값을 기준으로 함.

    extra_d_cnt = min(n - max(x, r), rest // 2)
    rest -= extra_d_cnt * 2 # 왕복 고려하여 *2로 빼줌
    extra_l_cnt = min(min(y, c) - 1, rest // 2)
    rest -= extra_l_cnt * 2 # 이후 rest는 'rl' 횟수로 사용

    return 'd' * (d_cnt + extra_d_cnt) + 'l' * (l_cnt + extra_l_cnt) + 'rl' * (rest // 2) + 'r' * (r_cnt + extra_l_cnt) + 'u' * (u_cnt + extra_d_cnt)
print(solution(3, 4, 2, 3, 3, 1, 5))