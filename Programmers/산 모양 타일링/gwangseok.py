import sys
sys.setrecursionlimit(10**6)


def get_count(dp, left_bottom_color, idx, tops):
    # 밑변 2, 윗변 1인 사다리꼴 칠하는 가지 수
    # left_bottom_color: 사다리꼴 제일 왼쪽이 칠해진 여부
    
    if dp[left_bottom_color][idx] != -1:
        return dp[left_bottom_color][idx]
    
    if left_bottom_color:
        if tops[idx]:
            dp[left_bottom_color][idx] = 2 * get_count(dp, 0, idx + 1, tops) + 1 * get_count(dp, 1, idx + 1, tops)
        else:
            dp[left_bottom_color][idx] = 1 * get_count(dp, 0, idx + 1, tops) + 1 * get_count(dp, 1, idx + 1, tops)
    else:
        if tops[idx]:
            dp[left_bottom_color][idx] = 3 * get_count(dp, 0, idx + 1, tops) + 1 * get_count(dp, 1, idx + 1, tops)
        else:
            dp[left_bottom_color][idx] = 2 * get_count(dp, 0, idx + 1, tops) + 1 * get_count(dp, 1, idx + 1, tops)
    
    return dp[left_bottom_color][idx] % 10007
        
        
def solution(n, tops):
    dp = [[-1] * len(tops) for _ in range(2)]
    
    if tops[-1]:
        dp[1][-1] = 3
        dp[0][-1] = 4
    else:
        dp[1][-1] = 2
        dp[0][-1] = 3    
    
    answer = get_count(dp, 0, 0, tops)    
    return answer % 10007
