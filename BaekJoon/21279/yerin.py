import heapq
import sys


def main():
    input = sys.stdin.readline
    n, c = map(int, input().split())

    gems_map = [[] for _ in range(100_001)]
    for _ in range(n):
        x, y, v = map(int, input().split())
        heapq.heappush(gems_map[x], (-y, v))  # y값을 내림차순 정렬

    heap = []  # 선택된 광석들을 저장할 최소 힙
    total_value = 0  # 현재 선택된 광석들의 총 가치
    max_value = 0  # 최대 가치

    for gems in gems_map:
        if not gems:
            continue

        # 꼭짓점~현재 좌표 중, 선택 가능한 광석의 개수가 제한을 초과하는 경우 처리
        while len(heap) + len(gems) > c:
            if heap and gems:
                max_y = min(heap[0][0], gems[0][0])  # 가장 높은 y 값 찾기(내림차순 정렬 -> min 사용)
            elif gems:
                max_y = gems[0][0]
            else:
                max_y = heap[0][0]

            # 가장 높은 좌표에 있는 광석 제거
            while heap and heap[0][0] == max_y:
                total_value -= heapq.heappop(heap)[1]
            while gems and gems[0][0] == max_y:
                heapq.heappop(gems)

        # 남은 광석들을 heap에 추가
        while gems:
            reversed_y, value = heapq.heappop(gems)
            heapq.heappush(heap, (reversed_y, value))
            total_value += value

        max_value = max(max_value, total_value)

    print(max_value)


if __name__ == "__main__":
    main()
