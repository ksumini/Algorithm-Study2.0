"""
<문제>
지도는 1 x 1크기의 사각형들로 이루어진 직사각형 격자 형태이며, 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있다. 
지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타낸다. 
- 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룬다.
- 지도의 각 칸에 적힌 숫자는 식량을 나타내는데, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타낸다.
지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return 하는 solution 함수 완성. 
만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해라.


<제한 사항>
- 3 ≤ maps의 길이 ≤ 100
    - 3 ≤ maps[i]의 길이 ≤ 100
- maps[i]는 'X' 또는 1 과 9 사이의 자연수로 이루어진 문자열
- 지도는 직사각형 형태

<풀이 시간>
20분

<풀이>
DFS(스택 방식)를 사용해 풀이

<시간 복잡도>
- 지도 크기 계산 및 방문 배열 초기화: O(rows * cols)
- 모든 칸을 한 번씩 확인: O(rows * cols)
- 각 DFS 호출: O(rows * cols)
- 결과 정렬: O(NlogN)
-> O(rows * cols) + O(rows * cols) + O(NlogN)
"""


def dfs(x: int, y: int, rows: int, cols: int, maps: list, visited: list):
    stack = [(x, y)]
    total_food = 0
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < rows and 0 <= cy < cols and maps[cx][cy] != 'X' and not visited[cx][cy]:
            visited[cx][cy] = True
            total_food += int(maps[cx][cy])

            # 상하좌우로 이동
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))

    return total_food


def solution(maps: list) -> list:
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    result = []

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                food = dfs(i, j, rows, cols, maps, visited)
                if food > 0:
                    result.append(food)

    if not result:
        return [-1]

    return sorted(result)