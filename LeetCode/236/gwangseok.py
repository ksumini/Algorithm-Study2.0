# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.set_depth(root)
        answer = self.lca(p, q)

        return answer

    @staticmethod
    def lca(p, q):

        # 깊이가 같아지도록 만들기
        while p.depth != q.depth:
            if p.depth > q.depth:
                p = p.parent
            else:
                q = q.parent
        
        # 같아지는 노드 찾기
        while p != q:
            p = p.parent
            q = q.parent
        
        return p

    def set_depth(self, root):
        q = deque([[root, 0]])

        while q:
            cur_node, cur_depth = q.popleft()
            cur_node.depth = cur_depth

            if cur_node.left:
                cur_node.left.parent = cur_node
                q.append([cur_node.left, cur_depth + 1])
            if cur_node.right:
                q.append([cur_node.right, cur_depth + 1])
                cur_node.right.parent = cur_node
