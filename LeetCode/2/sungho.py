# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def get_num_from_node(self, leaf):
        result = []
        while True:
            result.append(leaf.val)
            leaf = leaf.next
            if leaf == None:
                break

        result = list(map(str, result))
        return int(''.join(result[::-1]))

    def makeLinkedLists(self, num):
        lists = list(str(num))[::-1]

        idx = 0
        LinkedList = ListNode(int(lists[idx]))
        head = LinkedList

        while True:
            idx += 1
            if idx == len(lists):
                break
            else:
                LinkedList.next = ListNode(int(lists[idx]))
                LinkedList = LinkedList.next

        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num_l1 = self.get_num_from_node(l1)
        num_l2 = self.get_num_from_node(l2)

        return self.makeLinkedLists(num_l1 + num_l2)
