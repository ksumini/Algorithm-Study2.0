class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        all_Set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                all_Set.add(matrix[i][j])

        return target in all_Set

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1  # => (0,0), (2,3) 11%4, 11%4

        def idx2matrix(idx):
            return matrix[idx // n][idx % n]

        if target < idx2matrix(L) or idx2matrix(R) < target:
            return False

        while L <= R:
            mid = (L + R) // 2

            if target == idx2matrix(mid):
                return True

            if target > idx2matrix(mid):
                L = mid + 1
            else:
                R = mid - 1
