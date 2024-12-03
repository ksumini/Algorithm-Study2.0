'''
인접한 집들을 동일한 날에 털면 잡혀감
nums: 정수 배열 (각 집마다 가진 돈)
return 잡히지 않고 오늘밤 털 수 있는 최대 액수
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        houses_cnt = len(nums)
        if houses_cnt < 3:
            return max(nums)

        dp = [0] * houses_cnt
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, houses_cnt):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[houses_cnt-1]


if __name__ == '__main__':
    print(Solution().rob([1,2,3,1]))