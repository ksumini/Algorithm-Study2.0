"""
<문제>
동들의 초기 상태와 목표 상태가 주어졌을 때, 초기 상태에서 최소 몇 번의 동전을 뒤집어야 목표 상태가 되는지 구하라.
동전을 뒤집기 위해서는 같은 줄에 있는 모든 동전을 뒤집어야 한다.

<제한 사항>
- 1 ≤ beginning의 길이 = target의 길이 ≤ 10
- 1 ≤ beginning[i]의 길이 = target[i]의 길이 ≤ 10
    - 0은 동전의 앞면을, 1은 동전의 뒷면을 의미

<풀이 시간>
2시간 이상

<풀이>
1. 모든 가능한 행과 열의 뒤집기 조합을 탐색한다. (n과 m이 최대 10이기 때문에 1024 * 1024의 경우의 수)
2. 각 조합에 대해 뒤집은 후의 상태가 목표 상태와 일치하는지 확인
3. 일치하는 경우, 현재까지 뒤집기 횟수보다 더 작다면 뒤집기 횟수 업데이트

<시간 복잡도>
1. 행과 열의 뒤집기 경우의 수: O(2^n * 2^m)
2. 각 경우에 대한 상태 비교: O(n*m)
-> 전체 시간 복잡도: O(2^n * 2^m * n * m)
"""


def compare(beginning, target, row_mask, col_mask) -> bool:
    """
    :param beginning: 동전의 초기 상태 배열
    :param target: 목표 상태
    :param row_mask: 어떤 행을 뒤집을지 결정하는 비트 마스크
    :param col_mask: 어떤 열을 뒤집을지 결정하는 비트 마스크
    :return: 뒤집은 후의 상태가 target과 같다면 True, 다르다면 False 반환
    """
    for r in range(len(beginning)):
        for c in range(len(beginning[0])):
            is_row_flip = ((row_mask >> r) & 1) # row_mask의 r번째 비트가 1이면, r번째 행이 뒤집혔다는 것을 의미
            is_col_flip = ((col_mask >> c) & 1) # col_mask의 c번째 비트가 1이면, c번째 열이 뒤집혔다는 것을 의미
            # r번째 비트와 c번째 비트 둘 중 하나만 뒤집힌 경우 diff는 1, 두 개 모두 뒤집히거나 뒤집히지 않은 경우 0
            diff = is_row_flip ^ is_col_flip
            # 현재 동전의 상태를 diff를 통해 뒤집은 후 target과 비교
            if (beginning[r][c] ^ diff) != target[r][c]:
                return False
    return True


def solution(beginning: list, target: list) -> int:
    """
    :param beginning: 동전들의 초기 상태를 나타내는 2차원 정수 배열
    :param target: 목표 상태
    :return: 초기 상태에서 목표 상태로 만들기 위해 필요한 동전 뒤집기 횟수의 최솟값
    """
    n, m = len(beginning), len(beginning[0])
    answer = n * m + 1

    for row_flip in range(1 << n): # 행을 뒤집는 경우의 수
        for col_flip in range(1 << m): # 열을 뒤집는 경우의 수
            flip_cnt = bin(row_flip).count('1') + bin(col_flip).count('1')
            if flip_cnt < answer and compare(beginning, target, row_flip, col_flip):
                answer = flip_cnt

    return answer if answer < n * m + 1 else -1