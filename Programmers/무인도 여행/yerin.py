'''
'x' : 바다
숫자 : 식량
'''

from collections import defaultdict, deque


def bfs(start_x, start_y, maps, group_id, visited, amount_per_island, island_grp):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))  # 방문 처리
    amount_per_island[group_id] = int(maps[start_x][start_y])  # maps 값이신 string이므로 int로 변환
    island_grp[(start_x, start_y)] = group_id  # 시작 좌표에 섬 id 할당

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                amount_per_island[group_id] += int(maps[nx][ny])  # 해당 좌표가 해당하는 섬(섬 id)에
                island_grp[(nx, ny)] = group_id


def solution(maps):
    visited = set()
    amount_per_island = defaultdict(int)  # 그룹(섬) 넘버 : 식량 양
    island_grp = defaultdict(int)  # 좌표 : 그룹(섬) 넘버
    group_id = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # 숫자를 값으로 가지고 있고 방문한 적이 없을 때. 방문한 적이 있다면 다른 섬인 경우.
            if maps[i][j] != "X" and (i, j) not in visited:
                bfs(i, j, maps, group_id, visited, amount_per_island, island_grp)
                group_id += 1  # 다른 섬 id 갱

    return sorted(amount_per_island.values()) if amount_per_island else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
