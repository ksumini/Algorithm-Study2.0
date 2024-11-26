import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

parent = [-1] * n           # 이전 인덱스를 저장하는 배열
positions = [-1] * (n+1)     # LIS 각 길이의 마지막 원소 인덱스

lis = []

for idx, num in enumerate(a):
    pos = bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num
    if pos > 0:
        parent[idx] = positions[pos - 1]
    positions[pos] = idx

answer = []
current = positions[len(lis) - 1]
while current != -1:
    answer.append(a[current])
    current = parent[current]

print(len(answer))
print(*answer[::-1])