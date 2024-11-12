def bisect_left(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left

def longest_increasing_subsequence(sequence):
    lis = []  # LIS를 저장할 리스트
    
    for num in sequence:
        pos = bisect_left(lis, num)  # num이 들어갈 위치를 찾음
        
        # 만약 num이 lis의 마지막 원소보다 크다면, lis에 추가
        if pos == len(lis):
            lis.append(num)
        else:
            # lis[pos]에 num을 삽입하여, lis의 값들을 갱신
            lis[pos] = num
    
    return len(lis)

# 입력 부분
N = int(input())
nums = list(map(int, input().split()))

# 결과 출력
print(longest_increasing_subsequence(nums))
