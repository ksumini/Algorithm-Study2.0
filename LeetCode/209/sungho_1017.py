class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0

        for num in nums:
            total += num  # 총합 고려
            if num >= target:  # 원소 하나가 target 보다 큰 경우
                return 1

        if total < target:  # 다 합쳐도 안됨 ㅠ
            return 0
        elif total == target:  # 다 합쳐야 target과 같음
            return len(nums)

        answer = len(nums)
        L, R = 0, 0  # 왼쪽 오른쪽 idx (2 point 방식)

        while R < len(nums):
            target -= nums[R]
            while target <= 0:
                answer = min(answer, R - L + 1)
                target += nums[L]
                L += 1
            R += 1

        return answer