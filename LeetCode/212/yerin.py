from typing import List

class Solution:
    WORD_KEY = '$'

    def __init__(self):
        self.trie = None
        self.board = None
        self.found_words = None
        self.m, self.n = None, None

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = self._build_trie(words)
        self.board = board
        self.found_words = []
        self.m, self.n = len(board), len(board[0])

        # 보드 전체를 탐색하면서 dfs 호출
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] in self.trie:
                    self._dfs(i, j, self.trie)

        return self.found_words

    def _build_trie(self, words: List[str]) -> dict:
        """단어 목록으로부터 Trie 구조를 생성합니다."""
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[self.WORD_KEY] = word
        return trie

    def _dfs(self, i: int, j: int, node: dict) -> None:
        letter = self.board[i][j]
        curr_node = node[letter]

        # 단어가 완성된 경우 결과에 추가
        word_match = curr_node.pop(self.WORD_KEY, False)
        if word_match:
            self.found_words.append(word_match)

        # 현재 위치를 방문 처리
        self.board[i][j] = '#'

        # 인접한 위치로 이동하며 dfs 수행
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.m and 0 <= nj < self.n and self.board[ni][nj] in curr_node:
                self._dfs(ni, nj, curr_node)

        # 방문 처리 해제
        self.board[i][j] = letter

        # 탐색이 끝난 후, 자식 노드가 없으면 현재 노드를 Trie에서 제거
        if not curr_node:
            node.pop(letter)