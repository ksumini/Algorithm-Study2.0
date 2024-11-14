# O(n log n)
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

lis = [nums[0]]

for num in nums[1:]:
    if lis[-1] < num:
        lis.append(num)
    else:
        pos = bisect_left(lis, num)
        lis[pos] = num

print(len(lis))


# O(n^2)
'''
def longest_increasing_subsequence(A):
    n = len(A)
    dp = [1] * n  # 모든 dp 값을 1로 초기화
    
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:  # 증가하는 부분 수열 조건
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)  # dp 배열의 최대값이 LIS의 길이
'''