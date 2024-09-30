from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def idx2position(idx, n):
            r, c = (idx - 1) // n, (idx - 1) % n
            if r % 2 == 0:
                return n - 1 - r, c
            else:
                return n - 1 - r, n - 1 - c

        visited = set()
        visited.add(1)

        q = deque()
        q.append((1, 0))
        while q:
            now_idx, now_cnt = q.popleft()
            r, c = idx2position(now_idx, n)
            if board[r][c] != -1:
                now_idx = board[r][c]

            if now_idx == n * n:
                return now_cnt

            for i in range(1, 7):
                if now_idx + i <= n * n and now_idx + i not in visited:
                    visited.add(now_idx + i)
                    q.append((now_idx + i, now_cnt + 1))
        return -1