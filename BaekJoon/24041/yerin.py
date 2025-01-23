import sys
import heapq

input = sys.stdin.readline

def check(day):
    total_germs = 0
    max_heap = []

    for s, l, o in ingredients:
        germs = s * max(1, day - l)
        if o == 1:
            heapq.heappush(max_heap, -germs)  # 계산된 세균 수가 많은 순으로 정렬되도록 힙에 저장
        else:
            total_germs += germs

    # 제거 가능한 k개 재료의 세균 수는 제외
    for _ in range(min(k, len(max_heap))):
        heapq.heappop(max_heap)

    # 남은 세균 수 더하기
    total_germs += sum(-germs for germs in max_heap)

    return total_germs <= g


n, g, k = map(int, input().split())
ingredients = [list(map(int, input().split())) for _ in range(n)]

left, right = 0, 2 * 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
