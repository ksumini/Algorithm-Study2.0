# BFS 풀이
from collections import deque
class Solution:
    def bfs(self, x, y):
        q = deque()
        q.append([x, y, 0, [(x, y)]])   # x, y, index, visited
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        while q:
            x, y, index, visited = q.popleft()
            if index == len(self.word) - 1:
                return True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < len(self.board) and 0<= ny < len(self.board[0]) and (nx, ny) not in visited and self.board[nx][ny] == self.word[index+1]:
                    q.append([nx, ny, index+1, visited+[(nx,ny)]])
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if board[i][j] == word[0]:
                    if self.bfs(i, j):
                        return True
        return False
    
# DFS
class Solution:
    def dfs(self, x, y, index):
        if not (0<=x<len(self.board) and 0<=y<len(self.board[0]) and self.word[index] == self.board[x][y]):
            return False

        if index == len(self.word) - 1:
            return True
            
        temp = self.board[x][y]  # 현재 위치 문자 저장
        self.board[x][y] = '#'   # 방문 표시
        
        result = self.dfs(x+1, y, index+1) or \
                 self.dfs(x-1, y, index+1) or \
                 self.dfs(x, y+1, index+1) or \
                 self.dfs(x, y-1, index+1)
        
        self.board[x][y] = temp  # 방문 표시 해제
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if board[i][j] == word[0] and self.dfs(i, j, 0):
                    return True
        return False
