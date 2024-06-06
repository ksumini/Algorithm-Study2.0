import math

import math
def solution(numbers):
    answer = []
    for number in numbers:
        num_bin = bin(number)[2:]
        while 1:
            if not check_node_cnt(len(num_bin)):
                num_bin = '0' + num_bin
            else:
                break

        if dfs(num_bin):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer

def check_node_cnt(node_cnt)->bool:
    node_cnt += 1
    while node_cnt > 1:
        node_cnt, remainder = divmod(node_cnt, 2)
        if remainder != 0:
            return False
    return True

def dfs(nodes):
    if len(nodes) == 1:
        return True
    mid = math.ceil(len(nodes)/2) - 1
    if nodes[mid] == '0':
        if nodes[:mid].count('1') == 0 and nodes[mid+1:].count('1') == 0:
            return True
        else:
            return False
    return dfs(nodes[:mid]) and dfs(nodes[mid+1:])

print(solution([7, 42, 5])) # [1, 1, 0]
print(solution([63, 111, 95])) # [1, 1, 0]