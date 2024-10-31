"""
<문제>
word search 1과 비슷한 문제지만 단어가 여러개 주어진다.

<풀이>
풀이 시간: 1시간 30분
단순히 백트래킹만으로는 시간 초과가 나기 때문에 트라이를 통해서 프루닝을 해줘야 한다.
1. 단어들을 Trie에 저장
2. 보드의 각 셀을 시작점으로 백트래킹

<시간 복잡도>
1. Trie 생성: O(N * K)
- N: words의 단어 개수
- K: 각 단어의 평균 길이
2. 보드 탐색: O(M * 4**L)
- M: 보드의 총 셀 개수
- L: words 중 가장 긴 단어

전체 시간복잡도: O(M * 4**L + N * K)
"""
from typing import List


class TrieNode: # 트라이를 저장할 노드
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode() # 루트

    def insert(self, word) -> None: # 삽입 메소드
        node = self.root # 루트노드부터 자식 노드가 점점 깊어지면서 문자 단위의 다진 트리 형태
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie에 모든 단어 삽입
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()  # 중복 단어 방지
        rows, cols = len(board), len(board[0])

        # 백트래킹 함수
        def backtrack(x, y, node, path):
            if node.is_end: # 단어의 끝이라면
                result.add(path)
                node.is_end = False  # 중복 단어 방지

            # 현재 셀을 방문 처리
            temp, board[x][y] = board[x][y], '#'

            # 상하좌우로 이동
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] in node.children:
                    backtrack(nx, ny, node.children[board[nx][ny]], path + board[nx][ny])

            # 셀 방문 해제
            board[x][y] = temp

        # 보드의 각 셀에서 백트래킹 시작
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie.root.children:
                    backtrack(i, j, trie.root.children[board[i][j]], board[i][j])

        return list(result)