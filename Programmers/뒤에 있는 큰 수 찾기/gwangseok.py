def solution(numbers):
    answer = [-1] * len(numbers)
    idx = len(numbers)
    stack = []
    
    while idx:
        idx -= 1
        num = numbers[idx]
        while stack and stack[-1] <= num:
            stack.pop()
        
        if stack:
            answer[idx] = stack[-1]
            
        stack.append(num)
    
    return answer
