from collections import deque


def can_go(maps, is_visited, row, col):
    # 이전에 방문한 적이 있거나 'X'일 때 못 감.
    if maps[row][col] != 'X' and is_visited[row][col] is False:
        return True
    else:
        False


def search(maps, is_visited, mvs, row, col):
    ans = int(maps[row][col])  # 현재 식량
    is_visited[row][col] = True
    q = deque([(row, col)])
    
    while q:
        # 이동하며 연결된 식량 합을 구함.
        cur_r, cur_c = q.popleft()
        for dr, dc in mvs:
            next_r, next_c = cur_r + dr, cur_c + dc
            if 0 <= next_r < len(maps) and 0 <= next_c < len(maps[0]):
                if can_go(maps, is_visited, next_r, next_c):
                    ans += int(maps[next_r][next_c])
                    is_visited[next_r][next_c] = True
                    q.append((next_r, next_c))
    
    return ans    


def solution(maps):
    answer = []
    is_visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    mvs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if can_go(maps, is_visited, row, col):
                # 방문하지 않은 곳 그리고 식량이 있으면 주위 식량 탐색.
                answer.append(search(maps, is_visited, mvs, row, col))
        
    if answer:
        return sorted(answer)
    else:
        return [-1]
