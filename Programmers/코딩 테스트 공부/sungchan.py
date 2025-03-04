def solution(alp, cop, problems):
    answer = 0

    goal_alp = alp
    goal_cop = cop

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    dp = [[float("inf")] * (goal_cop + 1) for _ in range(goal_alp + 1)]

    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[i][j] = 0

    result = float("inf")
    for i in range(goal_alp+1):
        for j in range(goal_cop+1):
            # 트레이닝 해서 올리는 방법
            dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j])
            #문제 풀어서 올리는 방법
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_rwd > i or cop_rwd > j:
                    continue

                if i-alp_rwd < alp_req or j-cop_rwd < cop_req:
                    continue
                dp[i][j] = min(dp[i-alp_rwd][j-cop_rwd]+cost, dp[i][j])
    return dp[goal_alp][goal_cop]
