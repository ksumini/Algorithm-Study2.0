class ListNode:
    """
    단일 연결 리스트 노드를 나타내는 클래스
    """

    def __init__(self, val=0, next=None):
        self.val = val  # 노드의 값
        self.next = next  # 다음 노드への 연결


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        두 개의 비-공백 연결 리스트를 더하여 합계를 연결 리스트 형태로 반환합니다.

        각 연결 리스트의 노드는 역순으로 숫자의 한 자리를 저장하며, 
        두 연결 리스트를 더한 결과 또한 역순으로 연결 리스트 형태로 반환됩니다.

        Args:
          l1: 첫 번째 연결 리스트
          l2: 두 번째 연결 리스트

        Returns:
          두 연결 리스트의 합계를 나타내는 새로운 연결 리스트
        """

        dummy = ListNode(0)  # 결과 연결 리스트의 가짜 헤더 노드 생성
        answer = dummy  # 결과 연결 리스트의 실제 헤더 노드 (dummy 다음)

        carry = 0  # 이전 연산의 넘겨지는 값

        while l1 or l2 or carry:  # l1, l2 또는 carry가 0이 될 때까지 반복
            node_sum = carry  # 현재 계산 값 (초기값은 이전 넘겨지는 값)

            if l1:  # l1이 존재하면 값 더하기
                node_sum += l1.val
                l1 = l1.next

            if l2:  # l2가 존재하면 값 더하기
                node_sum += l2.val
                l2 = l2.next

            carry, digit = divmod(node_sum, 10)  # 현재 계산 값을 10으로 나눈 몫과 나머지 분리

            dummy.next = ListNode(digit)  # 계산된 합계의 단위 자리 값을 결과 연결 리스트에 추가
            dummy = dummy.next  # 결과 연결 리스트의 포인터를 다음 노드로 이동

        return answer.next  # 가짜 헤더 노드를 제외한 실제 결과 연결 리스트 반환
