class Node:
    def __init__(self, num):
        self.cur = num
        self.prev = None
        self.next = None

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}

        for num in nums:
            hash_map[num] = Node(num)

            if num - 1 in hash_map:
                hash_map[num].prev = hash_map[num-1]
                hash_map[num-1].next = hash_map[num]
            
            if num + 1 in hash_map:
                hash_map[num].next = hash_map[num+1]
                hash_map[num+1].prev = hash_map[num]
        
        max_len = 0
        for key, cur_node in hash_map.items():
            if cur_node.prev is None:
                cnt = 1
                while cur_node.next:
                    cur_node = cur_node.next
                    cnt += 1
                max_len = max(max_len, cnt)
        
        return max_len
