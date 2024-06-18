# 2시간 30분
# 구현: 1시간, DFS: 1시간 30분


def mv_optimize(answer, x, y, r, c):
    # 현재 row, col (x, y)에서 목표 row, col (r, c)까지 최적으로 이동
    mv_up = mv_left = mv_right = mv_down = 0
        
    if x >= r: mv_up = (x - r)
    else: mv_down = (r - x)
    if y >= c: mv_left = (y - c)
    else: mv_right = (c -y)

    answer += 'd' * mv_down + 'l' * mv_left + 'r' * mv_right + 'u' * mv_up    
    
    return answer


def solution(n, m, x, y, r, c, k):
    # (r1, c1)에서 (r2, c2)까지 이동할 때 필요한 최적의 거리 계산
    compute_need_mvs = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)
    need_mvs = compute_need_mvs(x, y, r, c)
    spare_mvs = k - need_mvs  # 왕복해야 하는 여유분 이동 수 구함.
    if spare_mvs < 0 or spare_mvs % 2 != 0:
        # 여유분이 음수이거나 짝수가 아니면 이동 불가능
        # 최적으로 이동하더라도 왕복을 해야하기 때문에 여유분은 짝수여야 한다.
        return 'impossible'
    
    answer = ''
    cur_r, cur_c = x, y
    
    # 다 하고 나니 if else를 여러번 사용하면 while문도 필요 없이 이동 개수를 바로 구할 수 있을 것 같다...
    while cur_r < n:
        # 제일 아래로 이동
        if need_mvs == k:
            # 이동하던 중 목적지 까지 이동해야 할 여유 거리가 없을 경우
            # 최적의 경로로 이동
            answer = mv_optimize(answer, cur_r, cur_c, r, c)
            return answer
        
        cur_r += 1
        answer += 'd'
        k -= 1
        need_mvs = compute_need_mvs(cur_r, cur_c, r, c)
        
    while cur_c > 1:
        # 제일 왼쪽으로 이동
        if need_mvs == k:
            # 이동하던 중 목적지 까지 이동해야 할 여유 거리가 없을 경우
            # 최적의 경로로 이동
            answer = mv_optimize(answer, cur_r, cur_c, r, c)
            return answer
        
        cur_c -= 1
        answer += 'l'
        k -= 1
        need_mvs = compute_need_mvs(cur_r, cur_c, r, c)
    
    while need_mvs < k:
        # 이동 우선순위에 따라 우좌 반복해서 이동
        answer += 'rl'
        k -= 2
        
    # 이동이 필요한 수만큼 여유분이 남앗으므로 최적으로 목적지 까지 이동
    # 반복을 제외하고 대칭이동하는 것과 같다.
    answer = mv_optimize(answer, cur_r, cur_c, r, c)
    return answer


# setrecursionlimit -> 힌트보고 함.

# import sys
# sys.setrecursionlimit(5000)

# def search(target_r, target_c, cur_r, cur_c, remain_move, answer):
#     # dfs를 이용해 우선순위에 따라 이동후 도착지점까지 이동경로를 answer로 전달.
#     # 그리고 현재 위치에서 이동가능한 여유분을 ramin_move로 전달

#     if board[cur_r][cur_c] == 'e':
#         return answer, remain_move

#     # 현재 지점에서 끝까지 이동가능 여부를 판단해서 pruning해줌
#     need_mvs = compute_need_mvs(target_r, target_c, cur_r, cur_c)
#     if not is_possible(remain_move, need_mvs):    
#         return None, None

#     ret = None
#     cnt = None
#     for idx, (dr, dc) in enumerate(mvs):
#         next_r = cur_r + dr
#         next_c = cur_c + dc
        
#         if 0 < next_r < len(board) and 0 < next_c < len(board[0]):
#             ret, cnt = search(target_r, target_c, next_r, next_c, remain_move - 1, answer + mv_str[idx])
#         else:
#             continue
        
#         if ret is not None:  
#             # 우선 순위에 따라 이동 후 도착지점 까지 온 경우일 때 바로 return
#             # 이후 상황은 사전 순으로 뒤에 있으므로 고려하지 않아도 됨. 
#             break
    
#     return ret, cnt


# def is_possible(remain_mvs, need_mvs):
#     # 최적으로 이동한 후 남은 여유분 이동수를 고려해 이동 불가능 고려
#     # 여유분이 0보다 작거나 여유분이 홀수일 때 이동 불가능
#     diff = remain_mvs - need_mvs
#     if diff < 0 or diff % 2 != 0:
#         return False
#     else:
#         return True


# def compute_need_mvs(r1, c1, r2, c2):
#     # 최적의 이동 수 구함
#     return abs(r1 - r2) + abs(c1 - c2)


# def mv_horizontal(ret, c, cnt):
#     # 여유분 만큼 좌우로 이동함
#     # 좌로 끝까지 이동 후, 좌우로 이동하고 우로 대칭만큼 이동.

#     mv_left = c - 1  # 좌로 이동할 때 필요한 이동
#     if cnt > mv_left:  # 여유분이 좌로 끝까지 이동한 것보다 많을 때
#         ret = ret + 'l' * mv_left  # 좌로 끝까지 이동

#         repeat = cnt - mv_left # 우좌를 반복
#         ret = ret + 'rl' * repeat 
#         ret = ret + 'r' * mv_left # 좌로 이동한 만큼 대칭해서 우로 이동
#     else:  # 여유분이 좌로 끝까지 이동한 것보다 적을 때 좌로 이동하고 우로 해당 이동 수만큼 다시 이동
#         ret = ret + 'l' * cnt + 'r' * cnt    
#     return ret
    
    

# def solution(n, m, x, y, r, c, k):
#     global board, mvs, mv_str
    
#     need_mvs = compute_need_mvs(x, y, r, c)  # 최적의 경로로 이동 시 필요한 거리 계산
#     if not is_possible(k, need_mvs):  # 여유 분의 거리가 짝수로 나눠 떨어지지 않으면 못 감. // 갔다 와야하기 때문에
#         return 'impossible'
    
#     board = [[0] * (m + 1) for _ in range(n + 1)]  # 0은 .을 의미
#     board[x][y] = 's'
#     board[r][c] = 'e'
#     mvs = [(1, 0), (0, -1), (0, 1), (-1, 0)]  # 우선 순위에 따라 아래, 왼, 오, 위
#     mv_str = 'dlru' # 우선 순위에 따라 아래, 왼, 오, 위의 string
    
#     ret, cnt = search(r, c, x, y, k, '')  # 우선 순위에 따라 도착지 까지 이동함. cnt는 여유분
#     cnt //= 2  # 여유분의 절반까지 우선순위에 따라 이동하고 나머지는 대칭으로 이동.
#     # 해당 경우의 수를 고려하면서 굳이 dfs를 고려하지 않아도 되겠다고 생각.
    
#     if r == n:  # 좌우로만 움직임 -> 더이상 밑으로 갈 수 없을 때 좌우로만 이동
#         ret = mv_horizontal(ret, c, cnt)
#     else: # 밑으로 갈 수 있을 때
#         mv_under = (n - r)  # 제일 밑으로 이동할 때 필요한 거리
#         if cnt > mv_under:  # 여유분이 제일 밑으로 이동할 때 필요한 거리보다 많을 때 // 밑 -> 좌우 -> 위
#             ret = ret + 'd' * mv_under # 필요한 만큼 이동 
#             ret = mv_horizontal(ret, c, cnt - mv_under)  # 밑으로 이동하고 남은 여유 분으로 좌우로 이동
#             ret = ret + 'u' * mv_under # 나머지는 대칭으로 위로 이동해야 함.
#         else:  # 여유분이 제일 밑으로 이동할 때 필요한 거리보다 적을 때 // 밑 -> 위
#             ret = ret + 'd' * cnt + 'u' * cnt
#     return ret
