"""
<문제>
- 퍼즐은 시계들이 행렬을 이루는 구조물
- 하나의 시계에는 시곗바늘이 하나씩만 있다.
- 각 시곗바늘은 시계 방향으로만 돌릴 수 있고, 한 번의 조작으로 90도씩 돌릴 수 있다.
- 시곗바늘을 돌리면, 그 시계의 상하좌우로 인접한 시계들의 시곗바늘도 함께 돌아간다.
- 행렬의 모서리에 위치한 시계의 시곗바늘을 돌리는 경우에, 인접한 세 시계의 시곗바늘들이 함께 돌아간다.
- 꼭짓점에 위치한 시계의 시곗바늘을 돌리는 경우에는 인접한 두 시계의 시곗바늘들이 함께 돌아간다.
- 각 시계는 12시, 3시, 6시, 9시 중 한 방향을 가리킨다.
- 각 시계의 시곗바늘을 적절히 조작하여 모든 시곗바늘이 12시 방향을 가리키면 퍼즐이 해결되어 잠금장치가 열린다.

<제한 사항>
2 ≤ clockHands의 길이 ≤ 8
- clockHands는 2차원 배열이며 행과 열의 크기가 동일하다.
- 0 ≤ clockHands의 원소 ≤ 3
clockHands[i]의 원소들은 시곗바늘의 방향을 나타내며 0은 12시 방향, 1은 3시 방향, 2는 6시 방향, 3은 9시 방향을 나타낸다.
- 해결 가능한 퍼즐만 주어진다.

<풀이 시간>
2시간

<풀이>
1. 맨 윗줄의 모든 조합: 최대 O(4 ** 8) = O(2**16) = 65,536
- 맨 윗줄의 각 시계에 대해 0, 1, 2, 3번 회전 하는 모든 조합을 만든다.
2. 아래 줄 시계 회전
- 맨 윗줄의 회전을 결정한 후, 그 아래의 시계들은 바로 위의 시계 상태를 보고 결정한다. 바로 위의 시계가 12시를 가리키도록 하기 위해 시계를 몇 번 돌려야 하는지 결정한다.
3. 최소 조작 횟수 업데이트
- 모든 시곗 바늘이 12시를 가리키는 경우에 조작 횟수를 계산 후, 최솟값을 업데이트 한다.

<시간 복잡도>
1. 첫 번째 행 조합: O(4 ** n), n은 최대 8이기 때문에 연산횟수는 최대 65,536번
2. 각 조합에 대한 시계 회전(try_combination): 약 O(n**2)
- 첫 번째 행의 조합대로 회전: O(n)
- 아래의 나머지 행 처리: O(n**2)
- 최종 확인: O(n**2)
-> 전체 시간복잡도: O(4**n * n**2)
"""
from typing import Union


# 특정 시계의 위치를 기준으로 인접한 시곗바늘을 돌리는 함수
def rotate(x: int, y: int, board: list, cnt: int):
    """
    :param x, y: 기준이 되는 시계의 좌표 (x, y)
    :param board: 현재 시곗바늘의 상태를 나타내는 2차원 리스트
    :param cnt: 회전 횟수
    :return: 시뮬레이션 이후 시곗바늘의 상태를 나타내는 2차원 리스트
    """
    # 기준 시계와 인접한 상하좌우의 시곗바늘을 회전시킴
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy # 인접한 칸의 좌표
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            board[nx][ny] = (board[nx][ny] + cnt) % 4 # 현재 칸과 범위 내의 인접한 칸과 시계 방향으로 90도 회전


def rotate_by_combinations(bitmask: int, clock: list) -> Union[int, float]:
    """
    :param bitmask: 첫 번째 행의 조합(비트마스크)
    :param clock: 현재 시계 상태
    :return: 시계를 회전시키는 최소 횟수
    """
    board = [row[:] for row in clock]
    moves = 0

    n = len(clock)
    # 첫 번째 행 조합대로 회전
    for i in range(n): # 각 시계의 회전 상태를 2비트로 표현(0: 00, 1: 01, 2: 10, 3:11)
        rot_cnt = (bitmask >> (2 * i)) & 3 # i번째 시계의 회전 횟수
        rotate(0, i, board, rot_cnt) # (0, i) 칸을 회전시킴
        moves += rot_cnt

    # 아래의 나머지 행
    for i in range(1, n):
        for j in range(n):
            rotations = (4 - board[i-1][j]) % 4 # 바로 위의 시계가 0이 되도록 하는데 필요한 회전 횟수
            rotate(i, j, board, rotations)
            moves += rotations

    # 모든 시곗바늘이 12시를 가리키는지 확인
    if all(board[i][j] == 0 for i in range(n) for j in range(n)):
        return moves
    return float('inf')


def solution(clockHands: list) -> int:
    """
    :param clockHands: 시곗바늘들의 행렬
    :return: 퍼즐을 해결하기 위한 최소한의 조작 횟수
    """
    n = len(clockHands) # 행렬의 길이(시계 개수)
    answer = float('inf') # 조작 횟수를 무한으로 초기화

    # 첫 번째 행을 기준으로 모든 조합 시도
    for case in range(4 ** n): # O(4**n) = 65,536
        answer = min(answer, rotate_by_combinations(case, clockHands)) # O(n**2)
    return answer