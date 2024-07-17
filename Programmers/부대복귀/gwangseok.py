# 1시간

from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    
    # 서로 연결되어 있는 node 정보를 저장한다.
    links = defaultdict(set)
    
    # destination으로 부터 각 node까지 가는 거리를 저장한다.
    distances = [-1] * (n+1)
    distances[destination] = 0
    
    q = deque([])
    for road in roads:
        # 만약 road가 destination과 연결되어 있다면 queue에 넣어준다.
        if road[0] == destination:
            distances[road[1]] = 1
            q.append((road[1], 1))
        
        if road[1] == destination:
            distances[road[0]] = 1
            q.append((road[0], 1))
        
        # 서로 연결된 정보를 저장한다.
        links[road[0]].add(road[1])
        links[road[1]].add(road[0])
        
    # destination을 기준으로 bfs 탐색
    while q:
        cur_node, distance = q.popleft()
        
        for next_node in links[cur_node]:
            if distances[next_node] == -1:
                # 방문한 적이 없을 때 distances를 update한다.
                distances[next_node] = distance + 1
                q.append((next_node, distance + 1))
                
    return [distances[src] for src in sources]
