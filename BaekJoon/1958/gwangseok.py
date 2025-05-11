import sys
read_line = sys.stdin.readline


def lcs(str1, str2, str3):
    dp = [[[0] * (len(str3) + 1) for _ in range(len(str2) + 1)] for __ in range(len(str1) + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            for k in range(len(str3)):
                if str1[i] == str2[j] == str3[k]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[len(str1)-1][len(str2)-1][len(str3)-1]

num_str = 3
st = [read_line().strip() for _ in range(num_str)]

print(lcs(*st))
