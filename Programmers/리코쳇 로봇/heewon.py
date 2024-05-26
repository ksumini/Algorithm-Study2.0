'''
## 함수 설명
- `find_start`: 시작 위치만 알면 되므로 굳이 모든 보드를 확인할 필요가 없다 -> 함수로 작업

## 접근 방식
- BFS로 작업
- 슬라이딩 작업을 위하여 while문 사용
- visited 확인 작업을 추가하여 복잡도 줄이기

## 사용한 모듈
`deque`

## 추가 정보
- 시간: 2 hour 이하
- 힌트: 코드 참고

### ISSUE NUMBER
<!-- 이슈 번호를 입력해주세요 -->
- #69 
'''

from collections import deque
from typing import Tuple, List

def solution(board:List)->int:
    n = len(board)
    m = len(board[0])
    
    def find_start()->Tuple:    # 시작 위치 찾기
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'R':
                    return (row, col)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    start = find_start()

    q = deque()
    q.append([start[0], start[1], 0])
    visited = set()
    while q:
        x, y, move = q.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if board[x][y] == 'G':
            return move
        for i in range(4):
            now_x = x
            now_y = y
            while 1:    # 이동 가능한 만큼 슬라이딩
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]
                if 0<= next_x < n and 0 <= next_y < m and board[next_x][next_y] != 'D':
                    now_x = next_x
                    now_y = next_y
                    continue
                q.append([now_x, now_y, move + 1])
                break
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))