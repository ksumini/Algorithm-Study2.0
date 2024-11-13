"""
<문제>
가장 긴 증가하는 부분 수열(LIS) 문제로 수열의 길이가 최대 100만까지 주어진다.

<풀이>
풀이 시간: 25분
수 제한이 크기 때문에 이분 탐색으로 풀이

<시간 복잡도>
O(nlogn)
"""


from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

arr = []
for num in a: # O(n)
    pos = bisect_left(arr, num) # O(logn): num이 들어갈 위치
    if pos == len(arr): # num이 arr의 가장 마지막값보다 큰 상황이기 때문에 num을 추가
        arr.append(num)
    else:
        arr[pos] = num