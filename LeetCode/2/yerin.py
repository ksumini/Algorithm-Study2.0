# Definition for singly-linked list.
from typing import Optional


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
        node = head = ListNode(0)
        extra = 0  # 자리 올림수 초기화

        while l1 or l2 or extra:
            total = extra  # 자리 올림수 추가
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            extra, val = divmod(total, 10)  # 올림수와 현재 노드의 값 계산
            head.next = ListNode(val)
            head = head.next  # 현재 노드 이동

        return node.next