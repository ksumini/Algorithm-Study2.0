"""
<문제>
n x m 격자 미로
-> 미로의 (x, y)에서 출발해 (r, c)로 이동해서 탈출해야 한다.

1. 격자의 바깥으로는 나갈 수 없다.
2. (x, y)에서 (r, c)까지 이동하는 거리가 총 k여야 한다.
3. 이때, (x, y)와 (r, c)격자를 포함해, 같은 격자를 두 번 이상 방문해도 된다.
4. 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 한다.

<제한 사항>
- 2 ≤ n (= 미로의 세로 길이) ≤ 50
- 2 ≤ m (= 미로의 가로 길이) ≤ 50
- 1 ≤ x ≤ n
- 1 ≤ y ≤ m
- 1 ≤ r ≤ n
- 1 ≤ c ≤ m
- (x, y) ≠ (r, c)
- 1 ≤ k ≤ 2,500

<풀이 시간>
약 2시간

<풀이>
DFS(스택 방식)를 사용해 풀이
- 현재 위치에서 k번 모두 이동해 탈출 지점에 도달한 후(모든 탐색을 끝낸 뒤) 정답 후보에서 사전순으로 가장 빠른 문자열을 고르면 시간복잡도가 O(4^k)가 되기 때문에 시간초과가 난다.
- 스택을 사용해 현재 위치에서 (r, c)까지 이동이 불가능한 경우에는 가지치기(pruning)을 통해 탐색을 중단한다. -> 스택에 추가 x
    - 현재 위치 (nx, ny)에서 (r, c)로 이동이 불가능한 경우는 남은 이동 거리가 맨해튼 거리(최단 거리)보다 작은 경우와 (남은 거리 - 최단 거리)가 홀수가 되는 경우다.
    - 홀수번의 이동은 한 번 더 갔다가 다시 돌아올 수 없기 때문이다.
- 사전순으로 가장 빠른 경우를 출력하라고 했기 때문에 "dlru" 순으로 먼저 확인해야 한다.

<시간 복잡도>
최악의 경우 O(4^k)이나 pruning 지점이 많아 정확한 시간복잡도를 구하기 어려움
"""


def reachable(nx: int, ny: int, r: int, c: int, remain: int) -> bool:
    """
    :param nx: 현재 위치의 x좌표
    :param ny: 현재 위치의 y좌표
    :param r: 도착 위치의 x좌표
    :param c: 도착 위치의 y좌표
    :param remain: 이동할 수 있는 남은 거리
    :return: remain으로 (x, y)에서 (r, c)로 이동할 수 있으면 True, 없으면 False
    """
    manhattan_dist = abs(r - nx) + abs(c - ny)
    return remain >= manhattan_dist and (remain - manhattan_dist) % 2 == 0


def solution(n: int, m: int, x: int, y: int, r: int, c: int, k: int) -> str:
    """
    :param n: 미로의 세로 (2 ≤ n ≤ 50)
    :param m: 미로의 가로 (2 ≤ m ≤ 50)
    :param x: 출발 위치의 x 좌표
    :param y: 출발 위치의 y 좌표
    :param r: 탈출 위치의 x 좌표
    :param c: 탈출 위치의 y 좌표
    :param k: 탈출까지 이동해야 하는 거리
    :return: 미로를 탈출하기 위한 경로(위 조건대로 미로를 탈출할 수 없는 경우 "impossible")
    """
    # 스택을 사용하는 DFS에서 기본적으로 LIFO(Last In First Out) 방식으로 동작하기 때문에, 사전순으로 가장 빠른 경로를 찾기 위해서는 방향을 반대로 넣어야 한다.
    directions = [(-1, 0, "u"), (0, 1, "r"), (0, -1, "l"), (1, 0, "d")]
    if not reachable(x, y, r, c, k):
        return "impossible"

    stack = [(x, y, "", k)] # 시작 좌표, 방향 문자열, 이동할 수 있는 거리
    while stack:
        cx, cy, path, remain_dist = stack.pop()
        # k만큼 이동했을 때, (r, c)에 도달하면 path를 반환하고 도달하지 못했다면 "impossible"을 반환
        if remain_dist == 0:
            if (cx, cy) == (r, c):
                return path
            return "impossible"

        for dx, dy, move in directions:
            nx, ny, new_path = cx + dx, cy + dy, path + move
            # 범위를 벗어나지 않으면서, 남은 이동할 수 있는 거리로 r, c에 도착가능할 때만 스택에 추가
            if 1 <= nx <= n and 1 <= ny <= m and reachable(nx, ny, r, c, remain_dist - 1):
                stack.append((nx, ny, new_path, remain_dist - 1))