import sys
input = sys.stdin.readline

N = int(input())
stones = list(map(int,input().split()))

# dp[i] -> 0 ~ i까지 줄일 수 있는 횟수
dp = [0] * N

for i in range(N):
    dp[i] = max(dp[i], dp[i-1]) # 0 ~ i-1 까지 줄일 수 있는 개수 업데이트
    x = stones[i]

    for j in range(i + 1, N):
        # i ~ j까지 줄일 수 있는 개수 업데이트
        x = stones[j] - x
        if x < 0:
            # 줄일 수 있는 경우 없음
            break
        if x == 0:
            # i ~ j까지 1 줄일 수 있음
            # j + 1 ~ N까지는 i가 j+1일 때 또 구할 수 있으므로 break
            dp[j] = max(dp[j], dp[i-1] + 1)
            break

# 최대 횟수 - 최대 줄일 수 있는 횟수
print(N - dp[-1])


# from collections import deque


# N = int(input())
# stones = list(map(int, input().split()))

# q = deque([(0, stones)])  # work cnt, stones state
# ans = N

# while q:  # O(N)
#     cnt, cur_stones = q.popleft()

#     if ans <= cnt:
#         break

#     if not cur_stones:
#         ans = min(ans, cnt)
#         continue

#     if len(cur_stones) == 1:
#         ans = min(ans, cnt + 1)
#         continue

#     if cur_stones[0] > cur_stones[1]:
#         # case 2
#         q.append((cnt + 1, cur_stones[1:]))
#     else:
#         # case 2: 
#         q.append((cnt + 1, cur_stones[1:]))

#         # case 1:
#         cur_stones[1] -= cur_stones[0]
#         if cur_stones[1] == 0:
#             q.append((cnt + 1, cur_stones[2:]))
#         else:
#             q.append((cnt + 1, cur_stones[1:]))

# print(ans)
