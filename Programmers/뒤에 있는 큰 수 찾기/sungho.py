# 배열의 각 원소들에 대해 자신보다 뒤에 있는 수 중에 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수.
# 없으면 -1
def solution(numbers: list) -> list:
    """
    현재 자리에서 뒤에 자리를 비교하므로 가장 뒤에서부터 시작.
    뒤에서부터 수를 하나씩 읽으며 스택으로 값을 저장해가며 앞 수를 읽어가며 가장 큰 뒷수 읽기

    시간복잡도 : O(n)

    params numbers: 문자열
    returns answers: 뒤에 있는 큰 수
    """
    n = len(numbers)
    answers = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        if len(stack) == 0:  # 현재 값보다(i) 뒤에 더 큰 수가 없음
            stack.append(numbers[i])  # -1 그대로, 현재 값을 stack에 저장
            continue

        while len(stack) != 0:
            if stack[-1] > numbers[i]:  # 스택에서 가장 위의 수가 현재 수보다 크면 뒤에 큰 수
                answers[i] = stack[-1]
                break
            else:
                stack.pop()  # 스택에서 가장 위의 수보다 현재 수가 크거나 같으면 다음 스택 값 비교

        stack.append(numbers[i])  # 현재 수를 저장
    return answers