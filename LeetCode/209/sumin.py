"""
<문제>
자연수 배열 nums에서 target 이상인 길이가 가장 작은 subarray를 반환하라.
만약 그러한 subarray가 없다면 0을 반환

<풀이>
풀이 시간: 20분
투포인터로 풀이

<시간 복잡도>
O(n)
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        answer = len(nums)

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:  # 조건을 만족할 경우 최소 길이를 구함
                answer = min(answer, right - left + 1)
                total -= nums[left]  # left 요소를 빼고
                left += 1  # left를 증가시켜 서브 배열의 길이를 줄임

        return answer if answer != len(nums) else 0  # 최소값을 찾지 못한 경우 0 반환