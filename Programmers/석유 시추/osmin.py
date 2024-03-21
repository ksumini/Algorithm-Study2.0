# bfs 문제.
from collections import deque
visited = [[0 for _ in range(500)] for _ in range(500)]
def solution(land):
    n, m = len(land), len(land[0])
    oil = {i:[] for i in range(m)}
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                a,b, sum_ = bfs(land, i,j)
                for idx in range(a,b + 1):
                    oil[idx].append(sum_)
                
                
    print(oil)
    answer = max([sum(oil[i]) for i in range(m)])
    return answer

def bfs(land, i, j):
    dir_ = {(0,1),(0,-1),(1,0),(-1,0)}
    q = deque([[i,j]])
    visited[i][j] = 1
    min_, max_, sum_ = j, j, 0
    n, m = len(land), len(land[0])
    while q:
        x, y = q.popleft()
        max_ = max(y, max_)
        min_ = min(y, min_)
        sum_ += 1
        for dx, dy in dir_:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if not visited[x + dx][y + dy]:
                    if land[x + dx][y + dy]:
                        visited[x + dx][y + dy] = 1
                        q.append([x + dx, y + dy])
    return min_, max_, sum_

'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 12.2MB)
테스트 2 〉	통과 (0.55ms, 12.2MB)
테스트 3 〉	통과 (0.15ms, 12.2MB)
테스트 4 〉	통과 (0.15ms, 12.1MB)
테스트 5 〉	통과 (0.11ms, 12.1MB)
테스트 6 〉	통과 (1.00ms, 12.1MB)
테스트 7 〉	통과 (1.37ms, 12.1MB)
테스트 8 〉	통과 (0.55ms, 12.2MB)
테스트 9 〉	통과 (4.06ms, 12.3MB)
효율성  테스트
테스트 1 〉	통과 (65.53ms, 14.2MB)
테스트 2 〉	통과 (373.39ms, 15.2MB)
테스트 3 〉	통과 (198.03ms, 14.9MB)
테스트 4 〉	통과 (61.04ms, 14.3MB)
테스트 5 〉	통과 (343.35ms, 14.3MB)
테스트 6 〉	통과 (109.33ms, 14.3MB)
'''