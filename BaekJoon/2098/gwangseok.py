import sys
read_line = sys.stdin.readline


def tsp(N, A, dp, cur_pos, visited):
    # cur_pos: 현재 도시
    # visited: 방문한 도시의 비트마스크

    if dp[cur_pos][visited] != float('inf'):
        return dp[cur_pos][visited]

    if visited == (1 << N) - 1: # 모든 도시를 방문했을 때
        dp[cur_pos][visited] = A[cur_pos][0] if A[cur_pos][0] != 0 else 18 * 1e6
        # 갈 수 없는 건지 방문한 적이 없는 건지 구분해야 함.
        # 따라서 float('inf') 대신 18 * 1e6을 넣음.
        return dp[cur_pos][visited]
    
    for next_pos in range(N):
        if visited & (1 << next_pos) == 0 and A[cur_pos][next_pos] != 0:
            # 다음 도시를 방문하지 않았고, 경로가 존재할 때
            dp[cur_pos][visited] = min(  # 나머지 도시를 방문하는 순서가 여러개 존재하므로, 그 중 최소값을 구함.
                dp[cur_pos][visited],
                tsp(N, A, dp, next_pos, visited | (1 << next_pos)) + A[cur_pos][next_pos]
                )
    
    return dp[cur_pos][visited]



N = int(read_line().strip())
A = [list(map(int, read_line().split())) for _ in range(N)]
dp = [[float('inf')] * (1 << N) for _ in range(N)]
# dp[i][j] = i에 도착했을 때 j에 포함된 도시를 모두 방문했을 때, 나머지 남은 도시를 순회할 최소 비용.
print(tsp(N, A, dp, 0, 1)) # 어디서 시작하든 상관없으므로 0부터 시작
