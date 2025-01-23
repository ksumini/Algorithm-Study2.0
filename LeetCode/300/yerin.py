from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                dp[bisect_left(dp, num)] = num
        return len(dp)
