class Solution:
    def binary_search(self, line, start, end, target):
        if start >= end:
            return False
        mid = (start + end) // 2
        if line[mid] < target:
            return self.binary_search(line, mid+1, end, target)
        elif line[mid] > target:
            return self.binary_search(line, start, mid, target)
        else:
            return True

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []   # 2d -> 1d
        for m in matrix:
            nums += m
        return self.binary_search(nums, 0, len(nums), target)