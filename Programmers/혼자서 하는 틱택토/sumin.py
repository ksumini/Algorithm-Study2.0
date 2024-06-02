"""
<문제>
선공이 O, 후공이 X를 번갈아가면서 빈칸에 표시하는 게임
가로, 세로, 대각선으로 3개가 같은 표시가 만들어지면 같은 표시를 만든 사람이 승리
누군가 게임을 승리하거나, 9칸이 모두 차서 더 이상 표시를 할 수 없는 경우 무승부로 게임 종료

<제한 사항>
- board의 길이 = board[i]의 길이 = 3
    - board의 원소는 O, X, .(빈칸)으로만 이루어져 있다.

<풀이 방법>
문제의 핵심은 '규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황인가?'
1. O와 X의 개수 확인
- 선공이 O를 표시하기 때문에, (규칙을 지켰다면) 최종적으로 O의 개수는 항상 X의 개수와 같거나 X의 개수보다 하나 더 많다.
2. 게임이 종료되는 경우(누군가 승리하는 경우)
    - 승리조건(가로, 세로, 대각으로 3개가 같은 경우)을 만족하는지 확인한다.
3. 규칙을 준수해서 플레이 했는지 확인
    - 선공(O)이 승리한 경우, O의 개수는 X의 개수보다 1개 많아야 한다.
    - 후공(X)이 승리한 경우, O의 개수는 X의 개수와 같다.

<시간복잡도>
N의 제한이 3으로 매우 작기 때문에 사실상 O(1)인 상수시간과 같다.
- O와 X의 개수 세기: O(N^2) = O(9)
- 승리여부 확인
    - 가로행: O(N^2) = O(9)
    - 세로행: O(N^2) = O(9)
    - 대각선행: O(2 x N) = O(6)
-> 선공과 후공 모두에 대해 확인하기 때문에 O(2 x (9 + 9 + 6)) = O(48)
- 규칙 준수 여부 확인: O(1)
"""


def check_winner(board: list, player: str) -> bool:
    """
    :param board: 게임판
    :param player: 선공, 후공
    :return: player가 이겼다면 True, 졌다면 False 반환
    """
    # 가로 확인
    for row in board:
        if all(each == player for each in row):
            return True
    # 세로 확인
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # 대각선 확인
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def solution(board: list) -> int:
    """
    :param board: 틱택토 게임판의 정보를 담고 있는 문자열 배열
    :return: 규칙을 지켜서 게임을 진행 했을 때, board와 같이 나올 수 있다면 1 아니라면 0
    """
    # 1. O와 X의 개수 확인
    countO = sum(row.count('O') for row in board)
    countX = sum(row.count('X') for row in board)

    # O의 개수가 X의 개수와 같거나 하나 더 많은 경우가 아니라면, 게임은 규칙을 위반한 상황(O가 선공이기 때문에)
    if not (countO == countX or countO == countX + 1):
        return 0

    # 2. 승리 여부 확인
    O_wins = check_winner(board, 'O')
    X_wins = check_winner(board, 'X')

    # 3. 규칙 준수 여부 확인(아래의 경우라면 규칙을 준수하지 않고 플레이한 경우)
    # O가 승리, O의 개수 != X의 개수 +1인 경우
    if O_wins and countO != countX + 1:
        return 0
    # X가 승리, O의 개수 != X의 개수인 경우
    if X_wins and countO != countX:
        return 0
    # 모든 규칙을 준수해서 게임을 한 경우
    return 1


# test case
if __name__ == '__main__':
    print(solution(["O.X", ".O.", "..X"])) # 1
    print(solution(["OOO", "...", "XXX"])) # 0
    print(solution(["...", ".X.", "..."])) # 0
    print(solution(["...", "...", "..."])) # 1