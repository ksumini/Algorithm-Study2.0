class Node:
    def __init__(self, key, word=None):
        self.key = key
        self.children = {}
        self.word = word


class Trie:
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.word = word

    def dfs(self, node, result, cnt):
        if node.word:
            result.append(node.word)
            cnt += 1

        if cnt < 3 and node.children:
            for next_node in node.children.values():
                cnt = self.dfs(next_node, result, cnt)
                if cnt >= 3:
                    break
        
        return cnt

    def get_max_three_words(self, node):
        result = []
        self.dfs(node, result, 0)
        return result
    
    def search(self, word):
        result = []
        node = self.root
        for idx, char in enumerate(word):  # O(1e3 * 3 * 3e3)
            if char not in node.children:
                left_word_num = len(word[idx:])
                result.extend([[] for _ in range(left_word_num)])
                return result
            node = node.children[char]
            result.append(self.get_max_three_words(node))
        
        return result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for product in products:  # O(2 * 1e4)
            trie.insert(product)
        return trie.search(searchWord)
