import sys
read_line = sys.stdin.readline


class Node:
    def __init__(self, word=None):
        self.children = {}
        self.word = word  # 끝에 도달했을 때 해당하는 단어 저장.
        self.is_hit = False
    
    def clear_hit(self):
        self.is_hit = False
        for child_ch in self.children:
            self.children[child_ch].clear_hit()


class Trie:
    def __init__(self,):
        self.node = Node()

    def insert(self, word):
        node = self.node
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.word = word

    def search(self, board, row, col, visited, node, 
               max_length, max_word, score, num_hit, depth):

        if depth >= 8:
            return max_length, max_word, score, num_hit
        
        visited[row][col] = True
        if node.word is not None and node.is_hit is False:
            scores = [0, 0, 0, 1, 1, 2, 3, 5, 11]
            if max_length < len(node.word) or \
            (max_length == len(node.word) and node.word < max_word):
                max_length = len(node.word)
                max_word = node.word
            score += scores[len(node.word)]
            num_hit += 1
            node.is_hit = True

        mv_row = [1, 1, 1, 0, 0, -1, -1, -1]
        mv_col = [1, 0, -1, 1, -1, 1, 0, -1]

        for dr, dc in zip(mv_row, mv_col):
            next_row = row + dr
            next_col = col + dc

            if 0 <= next_row < 4 and 0 <= next_col < 4:
                if not visited[next_row][next_col] and \
                    board[next_row][next_col] in node.children:

                    next_node = node.children[board[next_row][next_col]]
                    max_length, max_word, score, num_hit = self.search(
                        board, next_row, next_col, visited, next_node, max_length, max_word, score, num_hit, depth + 1
                    )
        
        visited[row][col] = False
        return max_length, max_word, score, num_hit


trie = Trie()
for _ in range(int(read_line())):
    trie.insert(read_line().strip())

read_line()  # 의미 없는 엔터 값

num_board = int(read_line())
root_node = trie.node
for idx in range(num_board):
    max_length = 0
    score = 0
    num_hit = 0
    max_word = None
    board = [read_line().strip() for _ in range(4)]

    if idx < num_board - 1:
        read_line() # 의미 없는 엔터 값

    visited = [[False] * 4 for _ in range(4)]
    for row in range(4):
        for col in range(4):
            if board[row][col] in root_node.children:
                max_length, max_word, score, num_hit = trie.search(board, row, col, visited, root_node.children[board[row][col]], 
                            max_length, max_word, score, num_hit, 0)
    
    print(f"{score} {max_word} {num_hit}")
    root_node.clear_hit()
