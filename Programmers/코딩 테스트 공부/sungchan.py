def solution(alp, cop, problems):
    answer = 0

    goal_alp = alp
    goal_cop = cop

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    dp = [[float("inf")] * (goal_cop + 2) for _ in range(goal_alp + 2)]

    dp[alp][cop] = 0

    print(alp, goal_alp, cop, goal_cop)
    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            # 트레이닝 해서 올리는 방법
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            # 문제 풀어서 올리는 방법
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                alp_up = min(goal_alp, i + alp_rwd)
                cop_up = min(goal_cop, j + cop_rwd)
                dp[alp_up][cop_up] = min(dp[alp_up][cop_up], dp[i][j] + cost)

    return dp[goal_alp][goal_cop]
