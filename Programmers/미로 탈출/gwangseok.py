from collections import deque


def find_path(maps: list, src: list, dest: list) -> int:
    # 시작 -> 레버, 레버 -> 출구 식으로 길을 찾으므로 중복 고려 안 해도 됨.
    # 따라서 한번 방문한 좌표는 다시 방문하지 않는다.
    is_visit = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    # 상, 하, 우, 좌 움직임
    mv = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # 시작 좌표 방문
    is_visit[src[0]][src[1]] = True
    q = deque([[src[0], src[1], 0]]) # row, columne, distance
    
    while q:
        cur_r, cur_c, cur_d = q.popleft()
        if cur_r == dest[0] and cur_c == dest[1]:
            # 현재 좌표가 목표지점 (레버 or 출구)라면 거리 반환
            return cur_d
        
        for dx, dy in mv:
            # 상하우좌
            next_r, next_c = cur_r + dx, cur_c + dy
            if 0 <= next_r < len(maps) and 0 <= next_c < len(maps[0]) and \
               maps[next_r][next_c] != 'X' and is_visit[next_r][next_c] is False:
                # 갈 수 있으면 방문.
                # 1. map 범위를 안 벗어나야 함.
                # 2. 벽('X')가 아니어야 함.
                # 3. 방문한 적이 없어야 함.
                is_visit[next_r][next_c] = True
                q.append([next_r, next_c, cur_d + 1])
    
    # 목표지점에 갈 수 없으면 -1 반환.
    return -1


def solution(maps):
    # 시작, 출구, 레버 좌표 저장
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_point = (i, j)
            if maps[i][j] == 'E':
                end_point = (i, j)
            if maps[i][j] == 'L':
                lever_point = (i,j)
                             
    # 시작 -> 레버 길 찾기
    s_to_l = find_path(maps, start_point, lever_point)
    if s_to_l == -1:
        return -1
    # 레버 -> 출구 길 찾기
    l_to_e = find_path(maps, lever_point, end_point)
    if l_to_e == -1:
        return -1
    
    return s_to_l + l_to_e
