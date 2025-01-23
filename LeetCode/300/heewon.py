from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = [nums[0]]
        for num in nums[1:]:
            if answer[-1] < num:
                answer.append(num)
            else:
                idx = bisect_left(answer, num)
                answer[idx] = num
        return len(answer)