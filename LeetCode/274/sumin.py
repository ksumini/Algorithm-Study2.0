"""
<문제>
주어진 p와 q의 LCA(Lowest Common Ancestor)를 찾는 문제, LCA는 자기 자신이 될 수도 있다.

<제한 사항>
- 노드의 수는 2개 이상 100,000개 이하
-10**9 <= Node.val <= 10**9
- 모든 Node.val는 unique
- p != q

<풀이>
1. 종료 조건
- 각 노드를 탐색하여 노드의 값이 p나 q라면 반환한다. 또는 해당 노드의 값이 None이라면 더 이상 탐색할 필요가 없기 때문에 None일 때도 반환한다.
2. 왼쪽 서브트리와 오른쪽 서브트리 탐색
- 현재 노드가 p나 q가 아니라면, 그 노드의 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 탐색한다.
3. LCA 결정
- 만약 왼쪽 서브트리에서 p나 q중 하나를 찾고, 오른쪽 서브트리에서 나머지 하나를 찾았다면, 현재 노드는 p와 q의 공통 조상이 된다.
- 그렇지 않으면, 왼쪽 또는 오른쪽 중 한쪽에서만 p 또는 q를 찾았으므로, 찾은 쪽의 노드를 반환한다.


<풀이 시간>
1시간

<시간 복잡도>
O(N): 최악의 경우 모든 노드를 한번씩 방문해야 하기 때문에
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x # 현재 노드의 값
        self.left = None # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base condition: 노드가 None(말단 노드)이거나 p 또는 q를 찾으면 그 노드를 반환
        if root is None or root == p or root == q:
            return root

        # 왼쪽과 오른쪽 서브트리에서 각각 탐색
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p와 q가 각각 다른 서브 트리에 있으면, 현재 노드가 LCA
        if left and right:
            return root

        # 어느 한쪽 서브트리에서만 찾은 경우, 그쪽의 결과를 반환
        if left:
            return left
        else:
            return right