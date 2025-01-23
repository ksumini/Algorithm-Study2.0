class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        rows = []
        cols = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.add(j)
        
        for row in rows:
            matrix[row] = [0] * m
        
        for col in cols:
            for i in range(n):
                matrix[i][col] = 0

        