from typing import List


class Solution:
    def dfs(self, board, x, y, word, index):
        if index == len(word) - 1:
            return True

        temp = board[x][y]
        board[x][y] = "#"  # 방문 표시

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            # 경계 벗어 나거나 다음 문자가 아닌 경우 제외
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]) or board[nx][ny] != word[index + 1]:
                continue
            if self.dfs(board, nx, ny, word, index + 1):
                return True

        board[x][y] = temp

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # 첫 번째 글자가 일치하는 경우만 dfs함수 호출
                    if self.dfs(board, i, j, word, 0):
                        return True
        return False