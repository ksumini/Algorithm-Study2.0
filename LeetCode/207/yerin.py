'''
0 ~ (numCourses - 1)
prerequisites[i] = [ai, bi] -> ai를 들으려면 bi 무조건 먼저 들어야 함
모든 강의를 마칠 수 있으면 -> True
else -> false

false인 경우
- bi보다 ai를 먼저 듣는 경우
- ai == bi

'''
from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.course_graph = defaultdict(set)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for a, b in prerequisites:
            if a in self.course_graph[b] or a == b:
                return False

            self.course_graph[a].add(b)
            if not self.dfs(b, set(), a):
                return False
        return True

    def dfs(self, course, visited, target_course):
        # 부모 과목(?)이 선행 과목에 있을 때
        if target_course in self.course_graph[course]:
            return False

        # 현재 과목의 모든 선행 과목 탐색
        for pre_course in self.course_graph[course]:
            if pre_course in visited:
                continue

            # 방문 처리
            visited.add(pre_course)
            if not self.dfs(pre_course, visited, target_course):
                return False
        return True


if __name__ == '__main__':
    print(Solution().canFinish(numCourses=3, prerequisites=[[1,0],[0,2],[2,1]]))



