# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
0 또는 양수
거꾸로 저장됨
하나의 노드에 하나의 숫자
'''


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 결과 리스트의 첫 노드 생성
        node = ListNode(0)
        current = node  # 결과 리스트의 현재 노드를 가리킴
        up = 0  # 자리 올림수

        while l1 or l2 or up:
            total = up  # 현재 합계에 자리 올림수를 더함
            if l1:
                total += l1.val
                l1 = l1.next  # l1의 다음 노드로 이동
            if l2:
                total += l2.val
                l2 = l2.next  # l2의 다음 노드로 이동

            up, current.val = divmod(total, 10)  # 자리 올림수와 현재 노드의 값 계산

            if l1 or l2 or up:  # 다음 노드가 필요한 경우에만 새 노드 생성
                current.next = ListNode(0)
                current = current.next  # 다음 노드로 이동

        return node  # 결과 리스트의 첫 노드를 반환