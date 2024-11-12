"""
<문제>
보드판에 좌에서 우, 우에서 좌로 번갈아가며 번호가 붙어있다
1에서 시작해 가장 마지막칸에 도착하기 위한 최소 이동 횟수를 구해라.
- 주사위를 던져 최대 6칸까지 이동할 수 있으며, 현재 위치에서 다음 위치로 이동할 때 그 칸에 사다리나 뱀이 있으면, 해당 칸에서 사다리나 뱀의 목적지로 강제로 이동해야 한다.
- 사다리와 뱀은 한 번만 적용되며, 도착한 위치가 다른 사다리나 뱀이 있더라도 다시 이동하지 않는다.
- 도달할 수 없다면 -1을 반환한다.

<제한 사항>
- n == board.length == board[i].length
- 2 <= n <= 20
- board[i][j] is either -1 or in the range [1, n**2].
- The squares labeled 1 and n2 are not the starting points of any snake or ladder.

<풀이 시간>
45분

<풀이>
1. 보드를 BFS로 탐색한다. 주사위를 굴려 한 번에 최대 6칸까지 이동할 수 있다.(보드를 벗어나지 않는선에서)
2. 사다리나 뱀이 있는 칸에 도달하면 즉시 그 칸의 목적지로 이동한다.
3. BFS를 사용해 마지막 칸까지 가는 최소한의 이동 횟수를 구한다.

<시간 복잡도>
O(n**2)
- get_position(num, n): O(1)
- bfs(board): O(n**2), 각 칸을 최대 한 번 방문하고 전체 보드 크기는 n**2이기 때문에
"""

from typing import List
from collections import deque


class Solution:
    @staticmethod
    def get_position(num, n):
        """
        :param num: 보드판의 숫자
        :param n: 보드판의 가로, 세로 크기
        보드 번호 num을 (row, col) 좌표로 변환
        """
        # 보드 번호를 행과 열로 변환
        row = n - 1 - (num - 1) // n # 행 계산
        col = (num - 1) % n # 열이 몇 번째인지 계산(행 기준)

        # 행이 짝수인지 홀수인지에 따라 방향이 다르므로 처리
        if (n - 1 - row) % 2 != 0: # 홀수 행은 우에서 좌로 이동
            col = n - 1 - col
        return row, col

    def bfs(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set() # 방문 처리
        queue = deque([(1, 0)]) # 시작 칸 (1번 칸, 0번 이동)
        visited.add(1)

        while queue:
            cur, moves = queue.popleft()

            # 마지막 칸에 도달한 경우
            if cur == n * n:
                return moves

            # 주사위 굴리기
            for step in range(1, 7):
                next_square = cur + step
                if next_square > n * n:
                    continue

                # 보드에서 (row, col)로 변환
                row, col = self.get_position(next_square, n)

                # 사다리 또는 뱀이 있는 경우 해당 위치로 이동
                if board[row][col] != -1:
                    next_square = board[row][col]

                # 방문한 적이 없는 칸만 큐에 추가
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        # 마지막 칸에 도달할 수 없는 경우
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return self.bfs(board)