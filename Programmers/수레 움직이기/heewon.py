'''
## 함수 설명
- `bfs`: BFS 방식으로 start 지점에서 end 지점으로 가는 모든 경우의 수 출력(최적의 경로들만 X)
- `double_bfs`: 입력된 순서에 따라 2번의 bfs 적용

## 접근 방식
- 동시에 고려하는 것은 힘들다고 생각
    - 말 1개를 미리 이동 시키고 다른 말을 이동 시키자
    - 실수: 첫 시작하는 말은 최적의 경로로 가고 나머지 말을 최적의 경로로 가려고 했음 why? 둘 중에 한 말은 꼭 최적의 경로로 갈거라고 생각 but 아니였다
    - 첫 말은 DFS와 다른 말은 BFS 방식으로 코드를 작성 -> 모두 BFS로 수정
- BFS 함수의 조건 == 수레의 조건
    1. 수레는 벽이나 격자 판 밖으로 움직일 수 없습니다.(0<=next_position[0] <len(maze) and 0<=next_position[1] <len(maze[0])and next_position not in wall)
    2. 수레는 자신이 방문했던 칸으로 움직일 수 없습니다.(next_position not in path)
    3. 자신의 도착 칸에 위치한 수레는 움직이지 않습니다. 계속 해당 칸에 고정해 놓아야 합니다. (idx = len(path) if len(opposite_path) > len(path) else -1)
    4. 동시에 두 수레를 같은 칸으로 움직일 수 없습니다. (opposite_path[idx] != next_position)
    5. 수레끼리 자리를 바꾸며 움직일 수 없습니다. (idx < len(opposite_path) and opposite_path[idx] == now)
- 어떤 말이 시작 했느냐에 따라 결과 값이 다르기 때문에 Red->blue 와 Blue->red 경우의 최솟값으로 답 구하기
- 첫 BFS에서는 경로를 찾지만 마지막 BFS에서 경로를 못 찾으면 answer 값이 INF가 됨 -> 0 (if answer != float('INF') else 0)

## 사용한 모듈
`없음`

## 추가 정보
- 시간: 3 hour 이상
- 힌트: 거의 `None`

채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (1.42ms, 10.2MB)
테스트 7 〉	통과 (2.57ms, 10.2MB)
테스트 8 〉	통과 (12.82ms, 10.1MB)
테스트 9 〉	통과 (147.04ms, 10.3MB)
테스트 10 〉	통과 (0.31ms, 10.3MB)
테스트 11 〉	통과 (0.13ms, 10.3MB)
테스트 12 〉	통과 (25.61ms, 10.1MB)
테스트 13 〉	통과 (0.87ms, 10.4MB)
테스트 14 〉	통과 (0.27ms, 10.3MB)
테스트 15 〉	통과 (0.13ms, 10.4MB)
테스트 16 〉	통과 (0.14ms, 10.2MB)
테스트 17 〉	통과 (0.28ms, 10.3MB)
테스트 18 〉	통과 (0.21ms, 10.1MB)
테스트 19 〉	통과 (0.61ms, 10.2MB)
테스트 20 〉	통과 (0.50ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0

### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #35
'''

from collections import deque

def solution(maze):

    def bfs(start:list, end:list, opposite_path:list=[])->list:
        q = deque()
        q.append([start, [start]])
        # start에서 end로 가는 모든 경로 리스트로 저장
        paths = []
        while q:
            # 지금의 좌표, 지금까지의 경로
            now, path = q.popleft()
            if len(path) > 16:
                continue
            # 도착 지점에 도착하면 경로 저장
            if end == now:
                paths.append(path)
                continue
            # 상하좌우 이동
            for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # 다음 지점
                next_position = [now[0] + move[0], now[1] + move[1]]
                # 수레 조건 1, 2
                if 0<=next_position[0]<len(maze) and 0<=next_position[1]<len(maze[0])and next_position not in wall and next_position not in path:
                    if opposite_path:
                        # 수레 조건 3
                        idx = len(path) if len(opposite_path) > len(path) else -1
                        # 수레 조건 5
                        if idx < len(opposite_path) and opposite_path[idx] == now:
                            continue
                        # 수레 조건 4
                        if opposite_path[idx] != next_position:
                            q.append([next_position, path + [next_position]])
                    else:
                            q.append([next_position, path + [next_position]])
        return paths
    
    def double_bfs(first:list, last:list, move_cnt:float) -> int:
        # 첫 말의 경로들 모두 찾기
        first_paths = bfs(first[0], first[1])
        
        # 각각의 첫 말 경로 유무 확인
        if first_paths:
            for first_path in first_paths:
                # 각각의 첫 말 경로에 수레 조건을 만족하는 나머지 말 경로 구하기
                last_paths = bfs(last[0], last[1], first_path)
                if last_paths:
                    for last_path in last_paths:
                        # 모든 경우의 수 중에 최소 이동 저장
                        move_cnt = min(move_cnt, max(len(first_path)-1, len(last_path)-1))
        else:
            return 0
        return move_cnt
    
    wall = []

    # 시작점, 도착점, 벽 위치 찾기
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_start = [i, j]
            elif maze[i][j] == 2:
                blue_start = [i, j]
            elif maze[i][j] == 3:
                red_end = [i, j]
            elif maze[i][j] == 4:
                blue_end = [i, j]
            elif maze[i][j] == 5:
                wall.append([i,j])
                
    answer = 17
    
    answer = double_bfs([red_start, red_end], [blue_start, blue_end], answer) # Red 경로 찾고 조건에 맞는 Blue 찾기 
    answer = double_bfs([blue_start, blue_end], [red_start, red_end], answer) # Blue 경로 찾고 조건에 맞는 Red 찾기
    return answer if answer != 17 else 0 # 경로를 못 찾는 경우는 0

# ----------------------NEW--------------------------------------

from collections import deque

def solution(maze):

    def bfs(start:list, end:list)->list:
        q = deque()
        q.append([start, [start]])
        # start에서 end로 가는 모든 경로 리스트로 저장
        paths = []
        while q:
            # 지금의 좌표, 지금까지의 경로
            now, path = q.popleft()
            if len(path) > 16:
                continue
            # 도착 지점에 도착하면 경로 저장
            if end == now:
                paths.append(path)
                continue
            # 상하좌우 이동
            for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # 다음 지점
                next_position = [now[0] + move[0], now[1] + move[1]]
                # 수레 조건 1, 2
                if 0<=next_position[0]<len(maze) and 0<=next_position[1]<len(maze[0])and next_position not in wall and next_position not in path:
                    q.append([next_position, path + [next_position]])
        return paths
    
    wall = []

    # 시작점, 도착점, 벽 위치 찾기
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_start = [i, j]
            elif maze[i][j] == 2:
                blue_start = [i, j]
            elif maze[i][j] == 3:
                red_end = [i, j]
            elif maze[i][j] == 4:
                blue_end = [i, j]
            elif maze[i][j] == 5:
                wall.append([i,j])
                
    answer = 17
    
    # 간단한 BFS로 모든 경로 탐색
    red_paths = bfs(red_start, red_end)
    blue_paths = bfs(blue_start, blue_end)
    
    # 경로가 없으면 0 출력
    if not blue_paths or not red_paths:
        return 0
    
    # 가능한 경로의 모든 경우의 수들 남은 조건 확인
    for red_path in red_paths:
        for blue_path in blue_paths:
            # 긴 경로와 짧은 경로 지정 
            if len(red_path) > len(blue_path):
                long_path = red_path
                short_path = blue_path
            else:
                long_path = blue_path
                short_path = red_path
            # 수레 조건 확인 전에 최적의 경로가 가능한지 비교
            if len(long_path) - 1 >= answer:
                continue
            # 경로를 확인하며 수레 조건 확인
            for index in range(len(long_path) - 1):
                # 짧은 경로는 도착하면 멈춰야 한다!
                if index < len(short_path)-1:
                    short_index = index
                else: 
                    short_index = -1
                # 수레 조건 4 동시에 같은 좌표 불가
                if long_path[index] == short_path[short_index]:
                    break
                # 수레 조건 5 자리 바꾸기 불가
                if short_index != -1:
                    if long_path[index + 1] == short_path[short_index] and long_path[index] == short_path[short_index+1]:
                        break
            else:
                # 최적 경로 갱신
                answer = len(long_path) - 1
                    
    
    return answer if answer != 17 else 0 # 경로를 못 찾는 경우는 0

# -----------------------DFS---------------------------------------
# 시도한 코드 (휴지통)
def dfs(maze, start, end, path=[]):
    # print(start, path)
    # 현재 위치를 방문한 경로에 추가
    path = path + [start]

    # 시작 위치가 도착 위치와 같으면 경로 반환
    if start == end:
        return [path]

    # 시작 위치가 미로 범위를 벗어난 경우 빈 리스트 반환
    if start[0] < 0 or start[0] >= len(maze) or start[1] < 0 or start[1] >= len(maze[0]):
        # print('1')
        return []

    # 시작 위치가 벽(1)이거나 이미 방문한 곳이면 빈 리스트 반환
    if maze[start[0]][start[1]] == 5 or maze[start[0]][start[1]] == 2 or start in path[:-1]:
        # print('2')
        return []

    # 상하좌우로 이동하며 DFS 재귀 호출
    paths = []
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_position = [start[0] + move[0], start[1] + move[1]]
        if 0<=next_position[0] <len(maze) and 0<=next_position[1] <len(maze[0])and next_position not in path:
            new_paths = dfs(maze, next_position, end, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths