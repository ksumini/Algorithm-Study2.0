'''
return 최대 점수, 가장 긴 단어, 찾은 단어 개수
'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

score_table = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}

# 상하좌우 + 대각선
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


# Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True


w = int(input())
trie = Trie()
words_set = set()
for _ in range(w):
    word = input().strip()
    words_set.add(word)
    trie.insert(word)

input()  # 빈 줄

b = int(input())


def dfs(x, y, node, visited, word, found):
    if node.end:
        found.add(word)

    # 최대 8글자
    if len(word) >= 8:
        return

    for dir in range(8):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
            next_char = board[nx][ny]
            if next_char in node.children:
                visited[nx][ny] = True
                dfs(nx, ny, node.children[next_char], visited, word + next_char, found)
                visited[nx][ny] = False


for _ in range(b):
    board = [list(input().strip()) for _ in range(4)]
    input()  # 빈 줄

    found_words = set()
    visited = [[False] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            ch = board[i][j]
            if ch in trie.root.children:
                visited[i][j] = True
                dfs(i, j, trie.root.children[ch], visited, ch, found_words)
                visited[i][j] = False

    total_score = 0
    longest_word = ''
    for w in found_words:
        total_score += score_table[len(w)]
        if len(w) > len(longest_word):
            longest_word = w
        elif len(w) == len(longest_word) and w < longest_word:
            longest_word = w

    print(f"{total_score} {longest_word} {len(found_words)}")