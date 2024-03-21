'''
## 변수 설명
- `row_oil`: row의 값당 석유의 총양을 저장한 딕셔너리 ex) 1번 예시 : {3: 7, 4: 7, 5: 7, 6: 9, 0: 8, 1: 8, 2: 8, 7: 2}
- `visited`: 석유가 있는 곳은 True, 석유가 없는 곳은 False
- `x_set`: 각 석유 덩어리당 포함된 row(x)의 값들을 set으로 저장
- `oil_size`: DFS, BFS를 통하여 얻은 석유 덩어리의 석유양

## 접근 방식
- DFS, BFS로 각각의 석유 덩어리당 총 석유양과 포함된 row 값들을 저장한다.
- 각각의 덩어리 탐색이 끝나면 `x_set`에 포함된 row 값들의 석유양 `row_oil`에 추가
- DFS 방법은 recursion limit 설정 필요

## 사용한 모듈
DFS: `defaultdict, sys`
BFS: `defaultdict, deque`

## 추가 정보
- 시간: 2 hour
- 힌트: `None`

#9 [석유 시추](https://school.programmers.co.kr/learn/courses/30/lessons/250136)
'''

#----------------------------------DFS----------------------------------
from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

def solution(land):
    answer = 0
    row_oil = defaultdict(int)
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if not visited[y][x] and land[y][x] == 1:
                x_set = set()
                oil_size = dfs(x, y, land, visited, x_set)
                for x_case in x_set:
                    row_oil[x_case] += oil_size
    return max(row_oil.values())

def dfs(x, y, land, visited, x_set):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    size = 1
    x_set.add(x)
    visited[y][x] = True
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx >= 0 and xx < len(land[0]) and yy >= 0 and yy < len(land) and not visited[yy][xx] and land[yy][xx] == 1:
            size += dfs(xx, yy, land, visited, x_set)
    return size

# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.3MB)
# 테스트 2 〉	통과 (0.26ms, 10.4MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.21ms, 10MB)
# 테스트 5 〉	통과 (0.17ms, 10.4MB)
# 테스트 6 〉	통과 (1.07ms, 10.3MB)
# 테스트 7 〉	통과 (1.46ms, 10.4MB)
# 테스트 8 〉	통과 (0.57ms, 10.4MB)
# 테스트 9 〉	통과 (4.38ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (86.44ms, 28.5MB)
# 테스트 2 〉	통과 (186.49ms, 16.1MB)
# 테스트 3 〉	통과 (185.85ms, 16.2MB)
# 테스트 4 〉	통과 (86.94ms, 25.3MB)
# 테스트 5 〉	통과 (667.10ms, 246MB)
# 테스트 6 〉	통과 (161.54ms, 27.4MB)
# 채점 결과
# 정확성: 60.0
# 효율성: 40.0
# 합계: 100.0 / 100.0

#----------------------------------BFS----------------------------------
# FAIL

from collections import deque, defaultdict
def solution(land):
    answer = 0
    cnt = 0
    row_oil = defaultdict(int)
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if not visited[y][x] and land[y][x] == 1:
                x_set = set()
                oil_size = 1
                q = deque()
                q.append([x, y])
                while q:
                    xx, yy = q.popleft()
                    visited[yy][xx] = True
                    x_set.add(xx)
                    for i in range(4):
                        xxx = xx + dx[i]
                        yyy = yy + dy[i]
                        if xxx >= 0 and xxx < len(land[0]) and yyy >= 0 and yyy < len(land) and not visited[yyy][xxx] and land[yyy][xxx] == 1 and [xxx, yyy] not in q:
                            q.append([xxx, yyy])
                            oil_size += 1
                for x_case in x_set:
                    row_oil[x_case] += oil_size
    return max(row_oil.values())

# 채점을 시작합니다.
# 정확성  테스트
# 테스트 1 〉	통과 (0.07ms, 10.3MB)
# 테스트 2 〉	통과 (0.25ms, 10.3MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.16ms, 10.2MB)
# 테스트 5 〉	통과 (0.12ms, 10.3MB)
# 테스트 6 〉	통과 (1.17ms, 10.3MB)
# 테스트 7 〉	통과 (1.39ms, 10.3MB)
# 테스트 8 〉	통과 (0.58ms, 10.3MB)
# 테스트 9 〉	통과 (4.44ms, 10.6MB)
# 효율성  테스트
# 테스트 1 〉	통과 (112.10ms, 14.1MB)
# 테스트 2 〉	통과 (220.43ms, 14.1MB)
# 테스트 3 〉	통과 (206.75ms, 13.9MB)
# 테스트 4 〉	통과 (98.95ms, 14.1MB)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	통과 (123.15ms, 14MB)
# 채점 결과
# 정확성: 60.0
# 효율성: 33.3
# 합계: 93.3 / 100.0