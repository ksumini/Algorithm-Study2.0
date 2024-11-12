from bisect import bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = []
        for row_values in matrix:
            rows.append(row_values[0])
        
        row_idx = bisect_right(rows, target) - 1
        col_idx = bisect_right(matrix[row_idx], target) - 1

        if matrix[row_idx][col_idx] == target:
            return True
        else:
            return False
