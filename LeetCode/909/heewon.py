from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        maps = [-1] # index를 칸으로 하기 위하여 0인칸 추가
        for idx, b in enumerate(board[::-1]):   # 1차원으로 변경
            if idx % 2 == 0:
                maps += b
            else:
                maps += b[::-1]

        q = deque()
        q.append([1, 0])    # [현재위치, 이동 횟수]
        visited = set()     # 방문 위치 저장
        visited.add(1)
        
        while q:
            now, cnt = q.popleft()
            if now >= n**2: # 도착 지점 도착
                return cnt
            cnt += 1
            next_ = maps[now+1:min(now+7, n**2+1)]  # 이동 가능 경우들
            now = min(now+7, n**2+1)    # 최대 이동 값 + 1
            last_check = True   # 뱀, 사다리가 아닌 최대 칸 확인
            for point in next_[::-1]:   # 가장 큰 칸부터 확인
                now -= 1    # 위치 뒤로 이동
                if point != -1 and point not in visited:    # 사다리와 뱀 경우
                    q.append([point, cnt])
                    visited.add(point)
                elif point == -1 and point not in visited and last_check:   # 뱀, 사다리가 아닌 최대 칸 경우
                    q.append([now, cnt])
                    visited.add(now)
                    last_check = False

        return -1   # 도달 불가