class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        targets = [points[0]]  # 화살 쏘는 구간 저장하는 리스트

        for x1, x2 in points[1:]:
            prev_x1, prev_x2 = targets[-1]
            # 현재 포인트의 좌표가 target_cord 구간 안일 때
            if x1 <= prev_x2:
                if x2 <= prev_x2:
                    targets[-1] = [x1, x2]
                else:
                    targets[-1] = [x1, prev_x2]
            # 현재 포인트의 좌표가 target_cord 구간 바깥에 있을 때
            else:
                targets.append([x1, x2])

        return len(targets)