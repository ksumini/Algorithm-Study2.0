from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums.sort()
        consecutive_elements = defaultdict(lambda: 0)

        for i in range(len(nums)):
            consecutive_elements[nums[i] + 1] = consecutive_elements[nums[i]] + 1

        return max(consecutive_elements.values())
