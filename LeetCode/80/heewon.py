class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        exp_len = 2  # 고유한 숫자를 저장할 위치
        for num in nums[2:]:
            # 현재 숫자가 2개 전 숫자와 다를 경우
            if num != nums[exp_len - 2]:
                nums[exp_len] = num
                exp_len += 1
        return exp_len