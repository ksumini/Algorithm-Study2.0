"""
<문제>
배열 height
x축(세로선) 두 개로 물을 최대로 담을 때, 해당 container의 크기를 구하라

<풀이>
투포인터로 풀이
1. 두 포인터 사이의 거리와 더 작은 높이를 사용해 현재 면적을 계산
2. 더 작은 높이를 가진 포인터를 한 칸 이동시킨다.
3. left가 right보다 작을 때까지 반복한다.

<시간 복잡도>
O(n): 최악의 경우, 한 포인터만 계속 이동해야할 수 있기 때문에
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right]) # 높이
            area = (right - left) * h
            answer = max(area, answer)

            # 더 작은 높이의 포인터를 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer
