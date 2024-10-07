class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = False
        before_num = -10^4 - 1
        exp_len = 0
        for num in nums:
            if num != before_num:
                nums[exp_len] = num
                exp_len += 1
                before_num = num
                check = True
            elif check:
                check = False
                nums[exp_len] = num
                exp_len += 1
        return exp_len
