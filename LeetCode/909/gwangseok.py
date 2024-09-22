from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.length = len(board)
        visited = [[False] * self.length for _ in range(self.length)]
        start_row, start_col = self.get_coordinate(1)
        target_point = self.get_coordinate(self.length ** 2)
        
        q = deque([[start_row, start_col, 0]])
        visited[start_row][start_col] = True
        
        while q:
            cur_row, cur_col, turn = q.popleft()
            
            is_right = True if (self.length - cur_row) % 2 == 1 else False
            
            cnt = 0
            while cnt < 6 and cur_row >= 0:
                # 6가지 경우의 이동하는 수
                if is_right is True:
                    # 오른쪽으로 이동해야 할 때
                    if cur_col == self.length - 1:
                        # 현재 column이 제일 끝일 때
                        # row를 하나 낮춰주고 이후 왼쪽으로 이동하게 만든다.
                        is_right = False
                        cur_row -= 1
                    else:
                        cur_col += 1
                else:
                    # 왼쪽으로 이동해야 할 때
                    if cur_col == 0:
                        is_right = True
                        cur_row -= 1
                    else:
                        cur_col -= 1
                
                cnt += 1
                if visited[cur_row][cur_col] is False:
                    # 방문한적이 없다면 queue에 넣어준다.
                    visited[cur_row][cur_col] = True
                    if board[cur_row][cur_col] != -1:
                        # snake 또는 ladder를 만나면 이동한다.
                        next_row, next_col = self.get_coordinate(board[cur_row][cur_col])
                    else:
                        next_row, next_col = cur_row, cur_col

                    if (next_row, next_col) == target_point:
                        return turn + 1
                    else:
                        q.append([next_row, next_col, turn + 1])
                    
        return -1
    
    def get_coordinate(self, num: int) -> List[int]:
        row = self.length - 1
        row -= (num - 1) // self.length
        col = (num - 1) % self.length

        if (self.length - row) % 2 == 0:
            col = self.length - 1 - col

        return row, col
