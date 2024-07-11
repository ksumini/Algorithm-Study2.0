"""
<문제>
왼손(4), 오른손(6)위에 두고 타이핑을 시작
- 이동하지 않고, 제자리에서 다시 누르는 경우: 가중치 1
- 상하좌우 인접한 숫자를 누르는 경우: 가중치 2
- 대각선으로 인접한 숫자를 누르는 경우: 가중치 3
- 같지 않고 인접하지 않은 숫자를 누를 때는 위 규칙에 따라 가중치 합이 최소가 되는 경로를 따른다.

<제한 사항>
1 ≤ numbers의 길이 ≤ 100,000
- numbers는 아라비아 숫자로만 이루어진 문자열

<풀이 시간>
2시간 이상 접근하다 포기하고 접근방법 참고

<풀이>
1. 초기 설정
- 두 숫자간의 이동 비용을 '이동 가중치 행렬'로 미리 정의
- dp에 (left, right, idx)에 대한 최소 비용을 저장
- BFS를 위해 queue에 초기 상태 저장

2. 상태 탐색
- queue에서 현재 상태 (left, right, idx)를 꺼내 다음 숫자 next_num으로 이동할 때의 비용 계산
- 두 손가락 각각에 대해 이동하는 경우를 고려하고, 비용(dp) 업데이트
- 새로운 상태에 대한 비용이 더 작으면 queue에 추가

3. 최소 비용 계산
- 모든 상태 중 마지막 숫자까지 도달한 상태에서 최소 비용을 찾기

<시간 복잡도>
O(n)
: 상태의 개수는 각 위치마다 모든 가능한 경우를 고려하기 때문에 총 10 x 10 x n(숫자의 길이) = 100 n
"""
from collections import defaultdict, deque

# 이동 가중치 행렬
costs = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],  # 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],  # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],  # 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],  # 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],  # 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],  # 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],  # 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],  # 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],  # 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],  # 9
]


def solution(numbers: str) -> int:
    """
    :param numbers: 숫자로 이루어진 문자열
    :return: 최소한의 시간으로 타이핑을 하는 경우의 가중치 합
    """
    numbers = list(map(int, numbers))
    n = len(numbers)
    dp = defaultdict(lambda: float('inf')) # 방문하지 않은 상태를 무한대로 초기화
    dp[(4, 6, 0)] = 0

    queue = deque([(4, 6, 0)])  # 초기 상태 (left, right, index)

    while queue:
        left, right, idx = queue.popleft()
        if idx == n:
            continue

        next_num = numbers[idx] # 다음에 눌러야 할 숫자

        # 왼손을 이동하는 경우(현재 오른손의 위치와 다음 숫자가 같다면, 왼손은 이동할 필요가 없음)
        if next_num != right:
            new_cost = dp[(left, right, idx)] + costs[left][next_num]
            # 새로운 비용이 현재 저장된 비용보다 작은 경우 업데이트
            if new_cost < dp[(next_num, right, idx + 1)]:
                dp[(next_num, right, idx + 1)] = new_cost
                queue.append((next_num, right, idx + 1))

        # 오른손을 이동하는 경우(현재 왼손의 위치와 이동할 위치가 같다면, 오른손은 이동할 필요가 없음)
        if next_num != left:
            new_cost = dp[(left, right, idx)] + costs[right][next_num]
            # 새로운 비용이 현재 저장된 비용보다 작은 경우 업데이트
            if new_cost < dp[(left, next_num, idx + 1)]:
                dp[(left, next_num, idx + 1)] = new_cost
                queue.append((left, next_num, idx + 1))

    # 마지막 숫자까지 도달한 모든 상태 중 최소 비용 찾기
    return min(dp[(left, right, n)] for left in range(10) for right in range(10))