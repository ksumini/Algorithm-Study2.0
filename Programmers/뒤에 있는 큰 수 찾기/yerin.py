def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    # 반복문을 통해 뒤에 큰 수가 있는 경우, 값을 갱신. 없는 경우 -1로 유지
    for i in range(len(numbers)):
        # 스택에 담긴 수가 현재 수보다 작은 경우 모두 꺼내고 answer 갱신
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))