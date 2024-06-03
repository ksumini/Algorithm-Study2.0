'''
[2024-06-04] heewon #78

## 함수 설명
- `check_line`: 입력되는 라인이 `O`, `X` 빙고인지 확인

## 접근 방식
- 각각의 `O`와 `X`의 개수 구하기
- 마지막으로 `O`를 둔 경우
    - `O` 개수 = `X` 개수 + 1 
    - `X`는 빙고 불가
- 마지막으로 `X`를 둔 경우
    - `O` 개수 = `X` 개수
    - `O`는 빙고 불가
- 나머지 경우는 불가

## 사용한 모듈
`None`

## 추가 정보
- 시간: 1 hour 이상(반례 못 찾음 + 코드 Refactoring)
- 힌트: `반례 case`
'''

def solution(board) -> int:
    """
    틱택토 게임 판 (board)을 입력받아 혼자서 진행 가능 여부를 반환하는 함수

    Args:
        board: 3x3 List로, 각 원소는 'O', 'X', '.' (빈칸) 문자열

    Returns:
        0: 불가능 1: 가능
    """
    o_cnt = 0
    x_cnt = 0
    o_bingo = False
    x_bingo = False

    def check_line(line) -> None:
        """
        한 줄 (행 또는 열, 대각선)에서 빙고 확인하는 함수

        Args:
            line: 검사할 한 줄 (List)
        """
        nonlocal o_bingo, x_bingo
        if line.count('O') == 3:    o_bingo = True
        elif line.count('X') == 3:  x_bingo = True

    for i in range(3):
        o_cnt += board[i].count('O')
        x_cnt += board[i].count('X')
        check_line(board[i])                        # 가로
        check_line([board[j][i] for j in range(3)]) # 세로
    check_line([board[i][i] for i in range(3)])     # 대각선
    check_line([board[i][2 - i] for i in range(3)]) # 반대 대각선

    if o_cnt == x_cnt and not o_bingo:     return 1 # X 표시 후
    if o_cnt == x_cnt + 1 and not x_bingo: return 1 # O 표시 후
    return 0