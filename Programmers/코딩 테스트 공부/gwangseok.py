import heapq


def dp_update(dp, alp_max, cop_max, alp, cop, t, q):
    alp = min(alp_max, alp)
    cop = min(cop_max, cop)

    if dp[alp][cop] > t:
        dp[alp][cop] = t
        heapq.heappush(q, [t, -alp, -cop])


def solution(alp, cop, problems):
    answer = 0

    dp = [[400] * 151 for _ in range(151)]
    alp_max, cop_max = alp, cop

    q = []
    heapq.heappush(q, [0, -alp, -cop])  # 시간은 작은 것, alp, cop는 큰 순으로 heap sort
    dp[alp][cop] = 0

    for problem in problems:
        if problem[0] <= alp and problem[1] <= cop:
            # 문제를 사전에 풀 수 있는 경우
            dp[problem[0]][problem[1]] = 0
            heapq.heappush(q, [0, -problem[0], -problem[1]])
        else:
            # 사전에 못 푸는 경우
            alp_max = max(alp_max, problem[0])
            cop_max = max(cop_max, problem[1])

    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]  # 가장 기본적인 1시간에 alp 또는 cop 올리기 문제 추가
    while q:
        cur_time, cur_alp, cur_cop = heapq.heappop(q)
        cur_alp *= -1
        cur_cop *= -1

        if cur_alp >= alp_max and cur_cop >= cop_max or dp[alp_max][cop_max] < cur_time:
            # 필요한 alp, cop를 만족한 경우 break
            # cur_time은 계속 증가하므로 alp_max, cop_max의 값이 cur_time보다 작으면 break
            break

        for r_alp, r_cop, n_alp, n_cop, n_time in problems:
            if cur_alp >= r_alp and cur_cop >= r_cop:
                # 문제를 풀 수 있으면 푼다.
                dp_update(dp, alp_max, cop_max, cur_alp+n_alp, cur_cop+n_cop, cur_time+n_time, q)
    
    for problem in problems:
        # 문제를 푸는데 가장 많은 시간이 걸린 것을 찾음.
        answer = max(answer, dp[problem[0]][problem[1]])
    
    # 한쪽이 극단적으로 크고, 다른 한 쪽이 극단적으로 다른 경우
    # DP가 update 안 됐지만, 극단적으로 큰 것을 맞추기 위해 max 값을 충족할 때까지 알고리즘 학습한 경우 고려
    # ex) [1, 1, [[0, 2, 1, 1, 100]]]
    answer = min(answer, dp[alp_max][cop_max])
    return answer
