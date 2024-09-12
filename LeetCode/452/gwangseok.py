class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cnt = 1
        shot = points[0][1]
        for point in points[1:]:
            if point[0] <= shot:
                if point[1] < shot:
                    shot = point[1]
                continue
            else:
                shot = point[1]
                cnt += 1
        
        return cnt
