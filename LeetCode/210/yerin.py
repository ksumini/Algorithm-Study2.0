'''
[수강 희망 과목, 선수 과목]

수강 순서 아무거나
if 사이클이 있는 경우, 빈 배열
'''

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        courses = [[] for _ in range(numCourses)]
        visited = set()
        ans = []

        for a, b in prerequisites:
            degree[a] += 1
            courses[b].append(a)

        q = deque([])

        for i, cnt in enumerate(degree):
            if cnt == 0:
                q.append(i)

        while q:
            now = q.popleft()
            if now in visited:
                ans = []
                break
            ans.append(now)
            visited.add(now)

            for course in courses[now]:
                degree[course] -= 1
                if degree[course] == 0:
                    q.append(course)

        return ans if len(ans) == numCourses else []


if __name__ == '__main__':
    print(Solution().findOrder(3, [[1,0],[1,2],[0,1]]))