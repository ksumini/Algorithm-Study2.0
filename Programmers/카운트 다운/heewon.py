def doubleortriple(dp, now, point):
    dp[now+point][0] = min(dp[now+point][0], dp[now][0] + 1)

def bullorsingle(dp, now, point):
    dp[now+point][0] = min(dp[now+point][0], dp[now][0] + 1)
    if dp[now+point][0] == dp[now][0] + 1:
        dp[now+point][1] = max(dp[now+point][1], dp[now][1] + 1)

def solution(target):
    cnt = 0
    # 247 이상의 값은 60 주기를 가짐 - why? 60과 50의 차이 10 때문에 발생하는 이유
    if target > 247:
        cnt, target = divmod(target, 60)
        target += 60 * 4
        cnt -= 4
    
    dp = [[target + 1, 0] for _ in range(target + 61)]  # dp 테이블 초기화
    dp[0] = [0, 0]  # 초기값 설정
    for idx in range(target):
        for single in range(1, 21): # 1~20 점
            bullorsingle(dp, idx, single)   # single
            doubleortriple(dp, idx, single * 2) # double
            doubleortriple(dp, idx, single * 3) # triple
        bullorsingle(dp, idx, 50)   # bull / 50점
    dp[target][0] += cnt    # 247 이상의 60 주기

    return dp[target]