from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 부모 노드 정보를 저장할 딕셔너리
        parent_map = {root: None}
        queue = deque([root])
        
        # p와 q의 부모 노드를 찾을 때까지 BFS 탐색
        while p not in parent_map or q not in parent_map:
            node = queue.popleft()
            
            if node.left:
                parent_map[node.left] = node  # 왼쪽 자식의 부모로 현재 노드를 저장
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node  # 오른쪽 자식의 부모로 현재 노드를 저장
                queue.append(node.right)
        
        # p의 모든 조상 노드를 set에 저장
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_map[p]
        
        # q의 조상 중 p와 공통되는 첫 번째 노드를 찾음
        while q not in ancestors:
            q = parent_map[q]
        
        return q  # 가장 가까운 공통 조상