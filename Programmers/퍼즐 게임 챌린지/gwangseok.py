def is_solved(diffs, times, limit, level):
    cost = times[0]  # diff[0] == 1
    
    for idx in range(1, len(times)):
        cost += max(0, diffs[idx] - level) * (times[idx-1] + times[idx]) + times[idx]
        
    if cost <= limit:
        return True
    else:
        return False
        

def solution(diffs, times, limit):
    answer = 0
    
    left = 1
    right = 1e5 # max_level = 1e5
    
    while left <= right:  # O(NlogM)
        mid = (left + right) // 2
        if is_solved(diffs, times, limit, mid): # O(N)
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
