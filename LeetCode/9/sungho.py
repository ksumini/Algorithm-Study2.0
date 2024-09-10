class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        L, R = 0, len(height) - 1
        max_height = max(height)

        while L < R:
            if max_area >= max_height * (R-L):
                break

            if height[L] < height[R]:
                max_area = max(max_area, (R-L) * height[L])
                L += 1
            else:
                max_area = max(max_area, (R-L) * height[R])
                R -= 1
        return max_area