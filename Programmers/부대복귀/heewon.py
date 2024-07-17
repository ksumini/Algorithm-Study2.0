from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    """
    주어진 지도 정보 (도로 연결 정보)와 시작 노드 리스트, 도착 노드를 이용하여
    각 시작 노드로부터 도착 노드까지의 최단 거리를 계산하고 반환하는 함수입니다.

    Args:
        n: 지도의 크기 (노드 개수)입니다.
        roads: 각 도로의 연결 정보 (시작 노드, 도착 노드)를 담은 리스트입니다.
        sources: 최단 거리를 계산할 시작 노드 리스트입니다.
        destination: 도착 노드입니다.

    Returns:
        각 시작 노드로부터 도착 노드까지의 최단 거리 리스트입니다.
    """
    graph = defaultdict(list)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    dp = defaultdict(lambda : -1)   # node 번호 : destination까지의 거리 (불가는 -1)
    q = deque()
    q.append([destination, 0])
    dp[destination] = 0
    
    while q:    # BFS 탐색
        now, dist = q.popleft() # 현재 노드, 거리
        
        for new in graph[now]:  # 현재 노드에서 연결된 모든 노드 탐색
            if dp[new] == -1:   # 방문하지 않은 노드만
                dp[new] = dist + 1
                q.append([new, dist + 1])
        
    return [dp[s] for s in sources] # 각 시작 노드로부터 도착 노드까지의 최단 거리 리스트 반환