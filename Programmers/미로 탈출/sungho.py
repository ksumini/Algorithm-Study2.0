from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def go(maps: list, a: list, b: list) -> int:
    """
    go bfs (minimum move)

    Params
        list a, b = location start, end

    Returns
        int : minimum time, if can't go 'E', return -1
    """
    h = len(maps); w = len(maps[0])
    q = deque(); visited = [[0] * w for _ in range(h)] # if visisted, value = 1
    q.append([a[0], a[1], 0]); visited[a[0]][a[1]] = 1 # visited

    while q:

        y, x, dist = q.popleft()

        for i in range(4):
            ny = y + dy[i];
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:  # out of maps
                continue
            if maps[ny][nx] == 'X' or visited[ny][nx] == 1:  # wall or visited
                continue
            if [ny, nx] == b:  # arrive end point(b)
                return dist + 1

            visited[ny][nx] = 1
            q.append([ny, nx, dist + 1])
    return -1

def find_locations(maps: list) -> list:
    """
    find locations ('S', 'L', 'E' => start, lever, end)

    Params
        list(str) maps : maps

    Returns
        list locations : locations of 'S', 'L', 'E'
    """
    location_start, location_lever, location_end = None, None, None
    h = len(maps)
    for i in range(h):
        s = maps[i].find('S')
        l = maps[i].find('L')
        e = maps[i].find('E')
        if s != -1:
            location_start = [i, s]
        if l != -1:
            location_lever = [i, l]
        if e != -1:
            location_end = [i, e]
        if location_start and location_lever and location_end:
            return location_start, location_lever, location_end
    return location_start, location_lever, location_end


def solution(maps: list) -> int:
    """
    'S' => 'L' => 'E'

    Params
        double-list maps :

    Returns
        int : minimum time, if can't go 'E', return -1
    """
    total_time = 0
    location_start, location_lever, location_end = find_locations(maps)

    # start -> lever
    start_to_lever = go(maps, location_start, location_lever)
    if start_to_lever == -1:
        return -1
    else:
        total_time += start_to_lever

    # lever -> exit
    lever_to_end = go(maps, location_lever, location_end)
    if lever_to_end == -1:
        return -1
    else:
        total_time += lever_to_end

    return total_time

