DIV = 1_000_000_007


def solution(n: int) -> int:
    """
    최적화 풀이, 누적합 활용
    f(n) = 2 x (f(n-1) + f(n-2) + ... + f(1)) + 2 x (f(n-3) + f(n-6) + f(n-9) + ... ) + f(n-3) - f(n-1) + f'(n)

    누적합, 부분 누적합(3의 배수인 항) 필요
    """

    dp = [0, 1, 3, 10]

    if n < 4:
        return dp[n]

    w_sum = sum(dp)
    partial_w_sum = [10, 1, 3]

    for i in range(4, n+1):
        f_n = 4 if i % 3 == 0 else 2     # f'(n) 반영
        f_n += 2 * (w_sum + partial_w_sum[i % 3]) + dp[i-3] - dp[i-1]      # 점화식 계산
        dp.append(f_n % DIV)
        w_sum += f_n % DIV                      # 누적합 업데이트
        partial_w_sum[i % 3] += f_n % DIV       # 부분합 업데이트

    return dp[-1]


def solution_tle(n: int) -> int:
    """
    설명에 기반한 풀이, 최적화가 필요
    """
    dp = [0, 1, 3, 10]

    if n < 4:
        return dp[n]

    for i in range(4, n + 1):
        tmp_answer = 4 if i % 3 == 0 else 2
        for j in range(i - 1, 0, -1):
            right_blocks = i - j  # j : left_blocks

            if right_blocks == 1:
                tmp_answer += dp[j] % DIV
            elif right_blocks == 3:
                tmp_answer += dp[j] * 5 % DIV
            elif right_blocks % 3 == 0:
                tmp_answer += dp[j] * 4 % DIV
            else:
                tmp_answer += dp[j] * 2 % DIV

        dp.append(tmp_answer % DIV)

    return dp[-1] % DIV
