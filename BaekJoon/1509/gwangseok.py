import sys
read_line = sys.stdin.readline


def update_is_palindrome(text, is_palindrome):
    is_palindrome[0][0] = True

    for idx in range(1, len(text)):
        is_palindrome[idx][idx] = True
        if text[idx-1] == text[idx]:
            is_palindrome[idx-1][idx] = True

    for length in range(2, len(text)):
        for idx in range(len(text) - length):
            if text[idx] == text[idx+length] and is_palindrome[idx+1][idx+length-1]:
                is_palindrome[idx][idx+length] = True


def update_dp(dp, is_palindrome, txt, start_idx):
    for idx in range(len(txt) - 1, start_idx, -1):
        if is_palindrome[start_idx][idx]:
            dp[idx] = min(dp[idx], dp[start_idx-1] + 1)
    
    dp[start_idx] = min(dp[start_idx], dp[start_idx - 1] + 1)


text = read_line().strip()
dp = [2500] * len(text) + [0]
is_palindrome = [[False] * len(text) for _ in range(len(text))]

update_is_palindrome(text, is_palindrome)

for i in range(len(text)):
    update_dp(dp, is_palindrome, text, i)

print(dp[len(text) - 1])
