from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_parent = []   # p의 부모 노드들 (자신 포함)
        q_parent = []   # q의 부모 노드들 (자신 포함)
        
        queue = deque() # 노드 탐색
        queue.append([root, [root]])    # 노드, 노드의 부모 노드들 (자신 포함)
        p_check, q_check = True, True   # 노드 탐색 여부
        
        while queue and (p_check or q_check):
            node, parent = queue.popleft()
            if node == q:
                q_check = False
                q_parent = parent
            if node == p:
                p_check = False
                p_parent = parent
            if node.left:
                queue.append([node.left, parent+[node.left]])

            if node.right:
                queue.append([node.right, parent+[node.right]])
                
        for i in range(min(len(p_parent), len(q_parent))-1, -1, -1):    # 최소 깊이 부터 부모 확인
            if p_parent[i] == q_parent[i]:
                return p_parent[i]
        return root