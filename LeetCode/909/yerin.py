from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # 라벨을 보드의 좌표로 매핑
        label_map = {}
        r, c, direction = n - 1, 0, 1
        for i in range(1, n ** 2 + 1):
            label_map[i] = (r, c)
            if i % n == 0:  # 한 행이 끝나면 방향 전환
                r -= 1
                direction *= -1
            else:
                c += direction

        # BFS 초기화
        q = deque([(1, 0)])  # (현재 라벨, 이동 횟수)
        visited = {1}  # 방문한 라벨 기록

        while q:
            label, step = q.popleft()
            
            for move in range(label + 1, min(label + 6, n ** 2) + 1):
                x, y = label_map[move]
                next_label = board[x][y] if board[x][y] != -1 else move
                
                if next_label == n ** 2:  # 도착했을 때 바로 리턴
                    return step + 1
                
                if next_label not in visited:
                    q.append((next_label, step + 1))
                    visited.add(next_label)

        return -1
