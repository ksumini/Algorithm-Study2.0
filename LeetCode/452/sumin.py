"""
<문제>
풍선의 좌표 2차원 정수 배열 points
points[i] = [x_start, x_end]
화살을 쏴서 모든 풍선을 터뜨리기 위한 최소한의 화살 개수를 구하기

<풀이>
풀이 시간: 20분
'그리디 알고리즘'
1. points를 끝을 기준으로 오름차순 정렬한다.
2. points를 하나씩 순회하며, 화살을 쏴서 최대한 많은 풍선을 터뜨린다.
- 현재 쏜 화살로 터뜨릴 수 없는 새로운 풍선이 등장하면(시작지점이 현재 지점보다 더 뒤에 있는 경우), 화살을 추가한다.

<시간 복잡도>
O(nlogn)
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        answer = 1 # 모든 풍선을 터뜨리기 위한 화살의 최소 개수
        arrow_x = points[0][1]
        for start, end in points[1:]:
            if start > arrow_x:
                answer += 1
                arrow_x = end

        return answer