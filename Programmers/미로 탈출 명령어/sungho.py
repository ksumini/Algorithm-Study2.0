from collections import deque

PATH_directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]  # d l r u
PATH = ['d', 'l', 'r', 'u']
DICT_directions = {'d': [1, 0], 'l': [0, -1], 'r': [0, 1], 'u': [-1, 0]}


def check_cango(point1: list, point2: list, cnt: int):
    """
    check can go point2 from point1 in cnt distance

    :param point1: location of point 1
    :param point2: location of point 1
    :param cnt: movement distance
    :return: bool. if can go, returns True
    """
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    if distance > cnt:  # too far to go in cnt step
        return False

    if abs(distance - cnt) % 2 == 1:  # can't go in cnt step
        return False
    return True


def solution(n, m, x, y, r, c, k, opt='list'):
    """
    n*m board. move from [x,y] to [r,c] in k distances. If possible, returns the dictionary fastest path route

    :param n: height of board
    :param m: width of board
    :param x: x of start point
    :param y: y of start point
    :param r: x of end point
    :param c: y of end point
    :param k: movement distance
    :param opt: option. use dict or list
    :return:
    """
    global PATH, PATH_directions, DICT_directions

    q = deque()
    q.append([x, y, ""])  # x, y, path

    if opt == 'dict':
        while q:
            x, y, path = q.popleft()
            for d, v in DICT_directions.items():
                nx = x + v[0]
                ny = y + v[1]
                if ny <= 0 or nx <= 0 or nx > n or ny > m:  # out of board
                    continue

                if len(path) + 1 > k:  # move more
                    return "impossible"

                if len(path) + 1 == k and [nx, ny] == [r, c]:  # arrive destination in k time step
                    return path + d

                if check_cango([nx, ny], [r, c], k - (len(path) + 1)):  # can go destination [r, c]
                    q.append([nx, ny, path + d])
                    break
    else:  # using list
        while q:
            x, y, path = q.popleft()
            for i in range(4):
                v = PATH_directions[i];
                d = PATH[i]
                nx = x + v[0]
                ny = y + v[1]
                if ny <= 0 or nx <= 0 or nx > n or ny > m:  # out of board
                    continue

                if len(path) + 1 > k:  # move more
                    return "impossible"

                if len(path) + 1 == k and [nx, ny] == [r, c]:  # arrive destination in k time step
                    return path + d

                if check_cango([nx, ny], [r, c], k - (len(path) + 1)):  # can go destination [r, c]
                    q.append([nx, ny, path + d])
                    break
    return "impossible"
