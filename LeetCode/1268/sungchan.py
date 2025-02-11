class TrieNode:
    def __init__(self, key: str, data: str | None = None):
        self.key = key
        self.data = data
        self.child: dict[str: TrieNode] = {}


class Trie:
    def __init__(self):
        self.head: TrieNode = TrieNode(None)

    def insert(self, data: str) -> bool:
        node: TrieNode = self.head

        for char in data:
            if char not in node.child:
                # 노드 생성
                node.child[char] = TrieNode(char)
            # 다음 노드
            node = node.child[char]

            # 마지막 노드에 데이터 삽입
        node.data = data

    def search(self, word: str) -> TrieNode | None:
        node = self.head

        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                return None

        return node

    def starts_with(self, prefix: str, limit: int) -> list[str]:
        node = self.search(prefix)

        # prefix 일치 노드가 없을 때
        if node is None:
            return []

        # 사전순으로 DFS 탐색
        def dfs(node: TrieNode, limit: int) -> list[str]:
            find_words: list[str] = []

            # 있는 데이터
            if node.data:
                find_words.append(node.data)

            # child 정렬
            node.child = dict(sorted(node.child.items()))

            # 사전순으로 접근
            for _, next_node in node.child.items():
                find_words += dfs(next_node, limit)

                # limit 보다 크면 탈출
                if len(find_words) >= limit:
                    break

            return find_words[:limit]

        return dfs(node, limit)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        suggested_products: list[list[str]] = []

        trie = Trie()

        for product in products:
            trie.insert(product)

        word = ""

        for char in searchWord:
            word += char
            suggested_products.append(trie.starts_with(word, 3))

        return suggested_products



