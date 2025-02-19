def solution(diffs, times, limit):
    answer = 0
    def get_time(level):
        
        total_time = 0
        time_prev = 0
        
        for diff, time in zip(diffs, times):
            if diff <= level:
                total_time += time
            else:
                total_time += (diff- level) * (time+time_prev) + time
            time_prev = time
            
        return total_time
    
    min_level = 1
    max_level = max(diffs)
    
    while get_time(min_level) > get_time(max_level):
        mid = (min_level + max_level) // 2
        
        if get_time(mid) == limit:
            return mid
        elif get_time(mid) > limit:
            min_level = mid+1
        else:
            max_level = mid
    
    return min_level