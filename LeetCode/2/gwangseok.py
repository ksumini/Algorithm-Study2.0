# 20분, O(N)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_num_from_listnode(l1)  # O(N)
        num2 = self.get_num_from_listnode(l2)  # O(N)

        return self.make_listnode(num1 + num2) # O(N)
    
    def get_num_from_listnode(self, l: Optional[ListNode]) -> int:
        cur_node = l
        cur_num = ''
        while cur_node:
            cur_num += f'{cur_node.val}'
            cur_node = cur_node.next
        
        return int(cur_num[::-1])
    
    def make_listnode(self, num: int) -> Optional[ListNode]:
        num_str = str(num)
        node = ListNode()
        for digit in num_str:
            node.val = int(digit)
            prev_node = ListNode()
            prev_node.next = node
            node = prev_node
        
        return node.next
