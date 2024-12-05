from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # 그래프 생성 및 진입 차수 계산
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        # 초기 진입 차수가 0인 노드들 추가
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        schedule = []

        while q:
            current_course = q.popleft()
            schedule.append(current_course)
            
            # 현재 노드의 후속 노드들의 진입 차수 감소
            for course in graph[current_course]:
                in_degree[course] -= 1
                if in_degree[course] == 0:  # 진입 차수가 0이 된 경우 큐에 추가
                    q.append(course)

        # 모든 코스를 방문했는지 확인
        return schedule if len(schedule) == numCourses else []