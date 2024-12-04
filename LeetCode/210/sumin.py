from typing import List
from collections import deque


class Solution:
    def topology_sort(self, vertex: int, edges: List[List[int]]):
        """
        :param vertex: 노드의 수
        :param edges: 간선 정보
        :return:
        """
        indegree = [0] * vertex
        graph = [[] for _ in range(vertex)]

        for a, b in edges:
            graph[b].append(a) # 정점 B에서 A로 이동
            indegree[a] += 1

        result = []
        q = deque()

        for i in range(vertex):
            if indegree[i] == 0:
                q.append(i)

        for _ in range(vertex):
            if not q:
                return []

            cur_node = q.popleft()
            result.append(cur_node)
            for adj_node in graph[cur_node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    q.append(adj_node)
        return result

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        return self.topology_sort(numCourses, prerequisites)