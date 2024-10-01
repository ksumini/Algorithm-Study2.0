# 찾는 word가 하나만 있기 때문에 dfs로 찾았다.
# 만약 찾는 word가 많다면 trie 자료 구조를 활용해야 한다.
# 유사하지만 더 어려운 문제: https://www.acmicpc.net/problem/9202

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    self.visited = [[False] * len(board[0]) for _ in range(len(board))]
                    self.visited[row][col] = True            
                    if self.dfs(row, col, 1) is True:
                        return True
        
        return False
    
    def dfs(self, row, col, idx):
        if idx >= len(self.word):
            # 모두 찾은 경우
            return True
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for d_row, d_col in moves:
            next_row, next_col = row + d_row, col + d_col

            if 0 <= next_row < len(self.board) and \   # row가 범위 안에 있음 
                0 <= next_col < len(self.board[0]) and \  # col이 범위 안에 있음
                not self.visited[next_row][next_col] and \  # 방문한 적 없음
                self.board[next_row][next_col] == self.word[idx]:  # 찾고자 하는 단어

                self.visited[next_row][next_col] = True
                if self.dfs(next_row, next_col, idx + 1) is True:
                    return True
                self.visited[next_row][next_col] = False  # 해당 부분을 잊어서 처음에 틀림
        
        return False
