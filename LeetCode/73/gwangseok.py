class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows = set()
        zero_cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):                
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in zero_rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        for col in zero_cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

        return matrix

        
