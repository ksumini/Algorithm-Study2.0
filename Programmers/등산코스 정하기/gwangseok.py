import heapq


def bfs(q, dp, is_stop, graph):
    while q: # O(N)
        cur_cost, cur_node = heapq.heappop(q) # O(log N)
        if dp[cur_node] < cur_cost:
            continue

        for next_node, next_cost in graph[cur_node]:
            max_cost = max(cur_cost, next_cost)
            if dp[next_node] > max_cost:
                dp[next_node] = max_cost
                if is_stop[next_node]:
                    continue
                heapq.heappush(q, [max_cost, next_node])
                
    return dp
    

def init_params(n, paths, gates, summits):
    dp = [float('inf')] * (n + 1)
    is_stop = [False] * (n + 1)
    
    for summit in summits:
        is_stop[summit] = True
    
    q = []
    for gate in gates:
        dp[gate] = 0
        q.append([0, gate])
    
    graph = [[] for _ in range(n + 1)]
    for src, dest, cost in paths:
        graph[src].append([dest, cost])
        graph[dest].append([src, cost])
        
    return q, dp, is_stop, graph
    
    
def solution(n, paths, gates, summits):
    q, dp, is_stop, graph = init_params(n, paths, gates, summits) # O(M)
    dp = bfs(q, dp, is_stop, graph) # O(N log N)
    
    
    ans_node, ans_cost = 0, float('inf')
    for summit in sorted(summits): # O(N log N)
        if dp[summit] < ans_cost:
            ans_node = summit
            ans_cost = dp[summit]

    return [ans_node, ans_cost]
