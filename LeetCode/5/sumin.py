"""
<문제>
substring 중 가장 긴 팰린드롬

<풀이>
풀이 시간: 40분

1. DP 테이블 정의
dp[i][j]: s[i:j+1]가 팰린드롬이면 True, 아니면 False

2. 초기값 정의
길이가 1인 substring은 모두 True
길이가 2인 substring은 s[i] == s[j]: True

3. 점화식 찾기
길이가 3이상인 substring의 팰린드롬 판정
if s[i] == s[j] and dp[i+1][j-1]:
    dp[i][j] = True

<시간 복잡도>
O(n**2)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j] = s[i:j+1]이 팰린드롬인지
        start = 0 # 가장 긴 팰린드롬 시작 인덱스
        max_len = 1 # 가장 긴 팰린드롬의 길이

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # 길이가 1인 문자열
                if i == j:
                    dp[i][j] = True
                # 길이가 2인 문자열
                elif (i + 1 == j) and s[i] == s[j]:
                    dp[i][j] = True
                # 길이가 3 이상인 문자열
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True

                # 현재 팰린드롬의 길이 계산, 더 길면 갱신
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    start = i
        return s[start: start + max_len]