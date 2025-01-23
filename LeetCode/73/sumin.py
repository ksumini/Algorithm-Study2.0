from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coordinate = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    coordinate.append([i, j])

        for r, c in coordinate:
            for j in range(m):
                matrix[r][j] = 0
            for i in range(n):
                matrix[i][c] = 0