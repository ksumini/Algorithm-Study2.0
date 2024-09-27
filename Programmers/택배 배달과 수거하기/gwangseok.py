# Greedy로 cap만큼 제일 먼 집에 전달하고
# 돌아오는 길에 cap만큼 수거해온다.
# cap = 1, 원소 50 -> O(50 * 100000) = O(5000000)

def update(arr, idx, cap):
    distance = 0
    while cap > 0 and idx >= 0:            
        sub_cap = min(arr[idx], cap)
        if sub_cap > 0 and distance == 0:
            distance = idx + 1
        
        arr[idx] -= sub_cap
        cap -= sub_cap
        
        if arr[idx] == 0:
            idx -= 1
    
    return distance, idx
    


def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliver_idx = n - 1
    pickup_idx = n - 1
    
    while deliver_idx >= 0 or pickup_idx >= 0:
        # Cap만큼 deliveries 원소를 끝에서 부터 뺀다.
        # 끝에서부터 0이상인 deliveries 원소의 index를 저장한다.
        deliver_distance, deliver_idx = update(deliveries, deliver_idx, cap)
        # Deliveries와 같은 방식으로 진행한다.
        pickup_distance, pickup_idx = update(pickups, pickup_idx, cap)
        # 더 큰 거리를 이동해야 하는 경우를 더해준다.
        answer += max(deliver_distance, pickup_distance)    
    
    return answer * 2
