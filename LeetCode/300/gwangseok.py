class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.seq = [nums[0]]

        for num in nums[1:]:
            if self.seq[-1] < num:
                self.seq.append(num)
            else:
                idx = self.bisect_left(num)
                self.seq[idx] = num

        return len(self.seq)
    
    def bisect_left(self, target):
        left = 0
        right = len(self.seq)

        while left < right:
            mid = (left + right) // 2
            if self.seq[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
