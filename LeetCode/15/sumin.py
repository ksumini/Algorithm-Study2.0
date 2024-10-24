"""
<문제>
세 수의 합이 0이 되는 경우를 찾아서 반환하라

<풀이>
풀이 시간: 40분
인덱스를 반환하는 것이 아닌 원소의 값을 반환하기 때문에 정렳 후 투포인터로 접근
중복된 값은 건너뛰고, left와 right을 합에 따라 이동한다.
세 수의 합이 0일 경우에, left와 right 양 옆으로 동일한 값이 있을 수 있기 때문에 ([-2, 0, 0, 2, 2])
반복문으로 이동하여 처리해준다.

<시간 복잡도>
O(n**2)
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    right -= 1
        return answer