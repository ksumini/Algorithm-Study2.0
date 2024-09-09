class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] > height[right]:
                answer = max(answer, (right-left) * height[right])
                right -= 1
            else:
                answer = max(answer, (right-left) * height[left])
                left += 1
        return answer

f = open('user.out', 'w')
s = Solution()
for case in map(loads, stdin):
    f.write(f"{s.maxArea(case)}\n")
f.flush()
exit(0)