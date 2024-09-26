"""
<문제>
m x n 2차원 배열
- 각 행은 오름차순 정렬돼있다.
- 각 행의 첫 번째 수는 이전 행의 마지막 수보다 크다

<제한 사항>
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

<풀이 시간>
10분

<풀이>
이분탐색으로 풀이했다. 수 제한이 작아서 완전탐색도 가능할 것 같다.

<시간 복잡도>
2차원 배열 -> 1차원 배열: O(n*m)
1차원 배열에서 이진 탐색: O(log(n*m))
"""
from typing import List


class Solution:
    @staticmethod
    def binary_search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :param matrix: 2차원 정수 배열
        :param target: 타겟 정수
        :return: 만약 target이 matrix안에 있으면 True, 없으면 False
        """
        nums = []
        for row in matrix:
            nums.extend(row)
        return True if self.binary_search(nums, target) else False