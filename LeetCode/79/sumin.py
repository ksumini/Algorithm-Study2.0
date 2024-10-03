"""
<문제>
m x n의 board에 word가 있으면 True를 반환, 없으면 False를 반환
단어는 연속적으로 인접한 셀의 문자로 구성될 수 있다.
동일한 문자 셀은 두 번 이상 사용될 수 없다.

<풀이 시간>
45분

<풀이>
백트래킹으로 풀이
1. 현재 위치의 문자가 단어의 현재 인덱스와 해당하는 문자와 일치하는지 확인
2. 문자가 일치하면 그 셀을 '#'로 바꿔 다시 방문하지 않도록 한다.
3. 상하좌우로 이동하며 다음 문자를 찾는다.
4. 모든 문자를 찾으면 True를 반환하고, 찾지 못하면 False를 반환

<시간복잡도>

"""
from typing import List


class Solution:
    def backtrack(self, i: int, j: int, word_length: int) -> bool:
        # Base Condition: 단어의 모든 알파벳을 찾은 경우
        if word_length == len(self.word):
            return True

        # 보드의 범위를 벗어나거나 문자가 일치하지 않는 경우 탐색 x
        if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]) or self.board[i][j] != self.word[word_length]:
            return False

        # 현재 셀 방문 표시
        temp = self.board[i][j]
        self.board[i][j] = '#'

        # 4개의 가능한 방향 (위, 아래, 왼쪽, 오른쪽) 탐색
        found = (
            self.backtrack(i + 1, j, word_length + 1) or
            self.backtrack(i - 1, j, word_length + 1) or
            self.backtrack(i, j + 1, word_length + 1) or
            self.backtrack(i, j - 1, word_length + 1)
        )

        # 백트래킹: 재귀 호출 후 이전 상태로 되돌리기 (원래 문자를 복원)
        self.board[i][j] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for i in range(len(board)):
            for j in range(len(board[0])):
                # word를 찾으면 True를 반환하고 종료
                if self.backtrack(i, j, 0):
                    return True
        # 끝까지 못 찾으면 False 반환
        return False