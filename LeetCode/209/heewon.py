class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_len = len(nums) + 1
        min_len = max_len
        start, end = 0, 0
        sum_ = 0
        while end < len(nums):
            sum_ += nums[end]
            while sum_ >= target:
                min_len = min(min_len, end - start + 1)
                sum_ -= nums[start]
                start += 1
            end += 1
        return min_len if min_len != max_len else 0