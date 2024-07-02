def get_dp(e):
    dp = [0] * (e + 1)  # 등장하는 횟수를 dp로 저장한다.
    # 에라토스테네스의 체와 유사한 방식으로 등장 횟수를 e까지 모두 구한다.
    for step in range(1, int(e ** 0.5) + 1):
        dp[step ** 2] += 1
        for i in range(step * (step + 1), e + 1, step):
            dp[i] += 2
            
    return dp

            
def get_large_dp(dp, e):
    large_dp = [0] * (e + 1)  
    large_dp[-1] = e
    
    # s ~ e까지 중 등장 횟수가 가장 많은 것 중 제일 작은 수를 구해야 하기 때문에
    # 거꾸로 확인해가며 DP에 저장한다.
    for s in range(e - 1, 0, -1):
        if dp[large_dp[s+1]] <= dp[s]:
            # s의 등장 횟수가 s + 1 ~ e 보다 클 때,
            # max 등장 횟수와 idx를 update한다.
            large_dp[s] = s
        else:
            large_dp[s] = large_dp[s+1]
    
    return large_dp
    

def solution(e, starts):
    # 구해햐 하는 수가 len(starts)개 만큼 있기 때문에 DP를 사용해야 겠다고 생각했다.    
    dp = get_dp(e) # n * (1 + 1/2 + 1/3 + ... + 1/n) \approx O(NlogN)
    # 각 idx ~ e까지 등장하는 횟수가 가장 많은 수들 중 가장 작은 값을 저장한다.
    large_dp = get_large_dp(dp, e) # O(N)
    
    return [large_dp[s] for s in starts]
