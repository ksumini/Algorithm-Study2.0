'''
양수 배열: nums
양수 : target
return 서브배열의 최소길이. 서브배열 없으면 0
서브배열 : 합이 target보다 크거나 같음.
'''

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

if __name__ == '__main__':
    print(Solution().minSubArrayLen(4, [1,4,4]))
