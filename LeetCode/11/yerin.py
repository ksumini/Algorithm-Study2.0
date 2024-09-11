'''
int 배열 : height
height 길이 : n

예1)
7 * 7 = 49

'''


class Solution:
    def maxArea(self, height: list) -> int:
        n = len(height)
        height = sorted(enumerate(height), reverse=True, key= lambda x: x[1])
        area = 0
        min_index, max_index = height[0][0], height[0][0] 
        for i in range(1, n):
            width = max(abs(min_index - height[i][0]), abs(max_index - height[i][0]))
            area = max(area, width * height[i][1])

            min_index = min(min_index, height[i][0])
            max_index = max(max_index, height[i][0])

        return area

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
