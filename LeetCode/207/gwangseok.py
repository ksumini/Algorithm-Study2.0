from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for src, dest in prerequisites:
            graph[src].append(dest)
            in_degrees[dest] += 1

        q = deque([])

        for node, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(node)
        
        for _ in range(numCourses):
            if not q: 
                return False

            cur_node = q.popleft()
            for next_node in graph[cur_node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    q.append(next_node)
            
        
        return True
