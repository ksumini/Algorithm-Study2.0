from typing import List
from collections import deque


class Solution:
    def topology_sort(self, vertex, edges):
        # 모든 노드에 대한 진입차수는 0으로 초기화
        indegree = [0] * (vertex)
        # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
        graph = [[] for _ in range(vertex)]

        # 방향 그래프의 모든 간선 정보를 입력 받기
        for a, b in edges:
            graph[b].append(a)  # 정점 B에서 A로 이동 가능
            # 진입차수를 1 증가
            indegree[a] += 1

        result = []  # 알고리즘 수행 결과를 담을 리스트
        q = deque()  # 큐 기능을 위한 deque 라이브러리 사용

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(vertex):
            if indegree[i] == 0:
                q.append(i)

        # 큐가 빌 때까지 반복
        while q:
            # 큐에서 원소 꺼내기
            now = q.popleft()
            result.append(now)
            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        # 모든 노드를 방문했는지 확인 (사이클 판별)
        return len(result) == vertex

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :param numCourses: 전체 강의 수(=노드의 수)
        :param prerequisites:(선후 관계)
        :return: 모든 강의를 수강할 수 있다면 True, 없다면 False
        """
        if not prerequisites:
            return True
        return self.topology_sort(numCourses, prerequisites)