"""
<문제>
두 개의 비어있지 않은 링크드 리스트가 주어진다.
각 노드는 0 또는 자연수로 채워져있다.
숫자는 역순으로 저장돼있고, 두 노드의 각 숫자의 합을 연결 리스트로 반환한다.

<풀이 시간>
35분

<풀이>
l1과 l2를 순차적으로 순회하면서, 각 자리의 값을 더하고 그 합을 노드로 만든다.
만약 합이 10을 넘어가면 이후 숫자간의 합에 반영하기 위해 flag 변수에 기록한다.

<시간 복잡도>
O(max(l1의 길이, l2의 길이))
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param l1: first linked list
        :param l2: second linked list
        :return: sum of both linked lists
        """
        flag = 0 # 자릿수 올림을 저장할 변수
        answer = ListNode() # 더미 헤드 노드
        current = answer

        while l1 or l2 or flag:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 현재 자리의 합 계산
            total = val1 + val2 + flag
            flag = 1 if total > 9 else 0
            current.next = ListNode(total % 10)

            # 다음 노드로 이동
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return answer.next