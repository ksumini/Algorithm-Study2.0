# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 1 -> 1 / 2~3 -> 2 / 4~7 -> 3 ...
        LCA = root.val
        if root.val == p.val or root.val == q.val:
            return root

        if self.findDescendant(p, q):
            return p
        if self.findDescendant(q, p):
            return q

        findInQueue = deque()
        findInQueue.append(root)
        while findInQueue:
            nowDescendant = findInQueue.pop()

            if nowDescendant.left != None:
                findInQueue.append(nowDescendant.left)
            if nowDescendant.right != None:
                findInQueue.append(nowDescendant.right)

            if self.findDescendant(nowDescendant, p) and self.findDescendant(nowDescendant, q):
                LCA = nowDescendant

        return LCA

    def findDescendant(self, p, q):
        """
        p에 q가 있는지 확인
        """
        findInQueue = deque()
        findInQueue.append(p)
        while findInQueue:
            nowDescendant = findInQueue.pop()
            if nowDescendant.val == q.val:
                return True

            if nowDescendant.left != None:
                findInQueue.append(nowDescendant.left)
            if nowDescendant.right != None:
                findInQueue.append(nowDescendant.right)

        return False