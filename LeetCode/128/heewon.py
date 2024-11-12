class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        now = -10**9 - 2
        cnt = 0
        for num in nums:
            if now + 1 == num:  # 다음 수가 있으면 길이 증가
                cnt += 1
            elif now != num:    # 다음 수 또는 동일 값이 없으면 다시 길이 측정
                cnt = 1
            answer = max(answer , cnt)
            now = num
        return answer