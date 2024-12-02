from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirement = defaultdict(list)
        for a, b in prerequisites:
            requirement[b].append(a)

        visited = [False] * numCourses  # 현재 DFS 경로에서 방문 여부
        checked = [False] * numCourses  # 이미 확인 완료된 노드 여부

        def dfs(node):
            if visited[node]:  # 현재 DFS 경로에서 이미 방문 => 사이클
                return True
            if checked[node]:  # 이미 확인된 노드 => 탐색 불필요
                return False

            visited[node] = True  # 현재 DFS 경로 방문 처리
            for neighbor in requirement[node]:
                if dfs(neighbor):  # 하위 노드에서 사이클 발견
                    return True

            visited[node] = False  # DFS 경로에서 제거
            checked[node] = True  # 확인 완료 처리
            return False

        for course in range(numCourses):
            if dfs(course):  # 사이클 발견 시 False 반환
                return False
        return True
