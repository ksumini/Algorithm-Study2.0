class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        answer = 1  # 첫 화살
        sorted_points = sorted(points, key=lambda x: x[1])
        now = sorted_points[0][1]   #   첫 화살 위치

        for x1, x2 in sorted_points:
            if x1 <= now:   # 화살 위치로 커버
                continue
            else:           # 새로운 화살 추가
                now = x2
                answer += 1
                
        return answer