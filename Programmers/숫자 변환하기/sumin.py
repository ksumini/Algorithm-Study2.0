from collections import deque


def solution(x: int, y: int, n: int) -> int:
    """
    :param x: 1 이상 1,000,000 이하의 정수
    :param y: 1 이상 1,000,000 이하의 정수
    :param n: 1 이상 y 미만의 정수
    :return: x를 y로 변환하기 위해 필요한 최소 연산 횟수
    """
    if x == y: # x와 y의 값이 같다면 연산 필요없음
        return 0

    queue = deque([(x, 0)])
    visited = set()
    visited.add(x)

    while queue:
        current, steps = queue.popleft() # 현재 좌표, 연산 횟수

        for next_step in (current + n, current * 2, current * 3): # +n, *2, *3을 다음 스텝으로 확인
            if next_step == y:
                return steps + 1
            if 1 <= next_step <= y and next_step not in visited:
                visited.add(next_step)
                queue.append((next_step, steps + 1))

    return -1