class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        ans = 0
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return ans     


# 반례: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         self.height = height
        
#         lefts = [0]
#         right = 1
#         max_area = 0

#         while right < len(height):
#             cur_area = self.get_area(lefts[0], right)
#             max_area = max(cur_area, max_area)
#             candidate_idx = 1
#             while candidate_idx < len(lefts):
#                 candidate_area = self.get_area(lefts[candidate_idx], right)
#                 if max_area < candidate_area:
#                     lefts.pop(0)
#                     max_area = candidate_area
#                     candidate_idx = 0
#                 candidate_idx += 1

#             if height[right] > height[lefts[0]]:
#                 lefts.append(right)
            
#             right += 1
        
#         return max_area

#     def get_area(self, left, right):
#         w = right - left
#         d = min(self.height[left], self.height[right])
#         return w * d
