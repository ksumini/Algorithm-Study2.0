class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [nums[0], 0]   # [마지막 집이 털린 경우, 마지막 집이 안 털린 경우]

        for i in range(1, len(nums)):
            houses[0], houses[1] = max(houses[1] + nums[i], houses[0]), houses[0]
        return max(houses)