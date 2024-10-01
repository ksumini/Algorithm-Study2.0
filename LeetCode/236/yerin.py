from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 부모 노드를 저장하는 딕셔너리
        parent = {root: None}
        que = deque([root])

        while p not in parent or q not in parent:
            node = que.popleft()
            if node.left:
                parent[node.left] = node  # 부모 노드를 저장
                que.append(node.left)
            if node.right:
                parent[node.right] = node
                que.append(node.right)

        # p의 모든 조상 노드를 저장
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # 공통 조상 탐색. 없으면 한 계층 위 노드로 갱신
        while q not in ancestors:
            q = parent[q]

        return q

