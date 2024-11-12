import sys
from bisect import bisect_left


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = [arr[0]]

for num in arr[1:]: # O(n log n)
    # 자신보다 큰 것 중 제일 작은 수의 앞의 수를 업데이트
    # 손해 없이 가장 긴 수열의 길이를 구할 수 있다.
    if num > ans[-1]:
        ans.append(num)
    else:
        ans[bisect_left(ans, num)] = num

print(len(ans))
