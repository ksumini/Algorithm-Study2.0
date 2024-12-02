class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        
        nums[2] += nums[0]

        for idx in range(3, len(nums)):
            nums[idx] += max(nums[idx-3], nums[idx-2])

        return max(nums[-1], nums[-2])
