def update_dp(dp, e):
    # 에라토스테네스의 체와 유사한 방식으로 등장 횟수를 e까지 모두 구한다.
    for step in range(1, e + 1):
        for i in range(step, e + 1, step):
            # 각 step의 배수를 고려하며 등장하는 개수 증가시킨다.
            # 1: 1, 2, ... 
            # step: step, 2 * step, 3 * step, ... 
            dp[i] += 1

            
def update_large_dp(dp, large_dp, e, min_s):
    max_frequency = -1
    max_idx = None
    
    # s ~ e까지 중 등장 횟수가 가장 많은 것 중 제일 작은 수를 구해야 하기 때문에
    # 거꾸로 확인해가며 DP에 저장한다.
    for s in range(e, min_s - 1, -1):
        if max_frequency <= dp[s]:
            # s의 등장 횟수가 s + 1 ~ e 보다 클 때,
            # max 등장 횟수와 idx를 update한다.
            max_frequency = dp[s]
            max_idx = s
        large_dp[s] = max_idx
    

def solution(e, starts):
    # 구해햐 하는 수가 len(starts)개 만큼 있기 때문에 DP를 사용해야 겠다고 생각했다.
    answer = []
    
    # 에라토스테네스의 체가 떠올랐다.
    dp = [0] * (e + 1)  # 등장하는 횟수를 dp로 저장한다.
    update_dp(dp, e) # n * (1 + 1/2 + 1/3 + ... + 1/n) \approx O(NlogN)
    
    large_dp = [0] * (e + 1)  
    # 각 idx ~ e까지 등장하는 횟수가 가장 많은 수들 중 가장 작은 값을 저장한다.
    update_large_dp(dp, large_dp, e, min(starts)) # O(N)
    
    for start in starts:
        answer.append(large_dp[start])
    
    return answer
