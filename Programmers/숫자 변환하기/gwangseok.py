def check_and_update(visit: set, turn: int, tmp_nums: list, tmp_num: int, y: list):
    if tmp_num <= y and tmp_num not in visit :
        tmp_nums.append((turn + 1, tmp_num))
        visit.add(tmp_num)
        

def solution(x, y, n):
    visit = set()
    nums = [(0, x)]
    
    while nums:
        tmp_nums = []
        for turn, num in nums:
            if num == y:
                return turn
            
            tmp_num = num * 3
            check_and_update(visit, turn, tmp_nums, tmp_num, y)
            
            tmp_num = num * 2
            check_and_update(visit, turn, tmp_nums, tmp_num, y)
                
            tmp_num = num + n
            check_and_update(visit, turn, tmp_nums, tmp_num, y)
        
        nums = tmp_nums
            
        
    return -1
