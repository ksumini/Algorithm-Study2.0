class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        min_arrow_shots = 1

        points.sort()
        arrow = points[0]
        for i in range(1, len(points)):
            if arrow[1] >= points[i][1]:
                arrow[1] = points[i][1]
                continue

            if arrow[1] < points[i][0]:
                arrow = points[i]
                min_arrow_shots += 1
        return min_arrow_shots
