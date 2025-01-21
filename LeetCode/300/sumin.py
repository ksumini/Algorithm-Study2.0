from typing import List
from bisect import bisect_left


class Solution:
    # 1. 다이나믹 프로그래밍 풀이: O(n**2)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

    # 2. 이진탐색 + 다이나믹 프로그래밍 풀이: O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect_left(sub, num)
                sub[idx] = num
        return len(sub)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([0,1,0,3,2,3]))
    print(s.lengthOfLIS([7,7,7,7,7,7,7]))