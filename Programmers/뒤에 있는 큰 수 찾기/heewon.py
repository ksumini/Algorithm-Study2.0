'''
## 접근 방식
- 풀었던 문제였지만 못 풀었고 확실하게 문제를 이해해야겠다고 결심
- 1st method fail
  - 차례대로 각각의 index에서 다음 큰 수를 찾기
  - 여러 조건을 걸며 시간 복잡도를 줄였지만 1 case fail
- 2nd method
  - stack을 이용한 접근
  - 차례대로 각각의 index에서 해당 number가 앞에 위치할 index들 찾기

## 추가 정보
- 시간: 1 hour 이상
- 힌트: `Yes`
'''

def solution(numbers):
  """
  입력 리스트 `numbers`에서 각 원소에 대해 뒤에 있는 큰 수를 찾아 `answer` 리스트에 저장하는 함수입니다.

  Args:
      numbers: 정수로 이루어진 리스트입니다.

  Returns:
      answer: 리스트 `numbers`의 각 원소에 대해 오른쪽 방향으로 처음 나오는 더 큰 원소를 담은 리스트입니다. 
              만약 더 큰 원소가 없다면 -1을 담습니다.
  """

  answer = [-1] * len(numbers)  # 결과를 저장할 answer 리스트를 -1로 초기화
  stack = []  # 더 큰 원소를 추적하기 위한 스택 생성

  for idx, number in enumerate(numbers):
    while stack and numbers[stack[-1]] < number:    # 스택이 비어있지 않고 스택 맨 위 원소보다 현재 원소가 더 크다면
      answer[stack.pop()] = number  # 스택에서 꺼낸 인덱스를 해당 원소의 다음 큰 원소로 표시

    stack.append(idx)   # 현재 원소의 인덱스를 스택에 추가

  return answer  # 계산된 결과 answer 리스트를 반환합니다.

# fail

# def solution(numbers):
#     n = len(numbers)
#     answer = [-1] * n
#     before_num = 1000001
#     s_numbers = sorted(numbers, reverse=True)
#     if numbers == s_numbers:
#         return answer
#     idx = 0
#     max_num = s_numbers[idx]
#     for i in range(n-1):
#         if numbers[i] == max_num:
#             answer[i] = -1
#             idx += 1
#             max_num = s_numbers[idx]
#         elif numbers[i] == before_num or (numbers[i] > before_num and numbers[i] < answer[-1]):
#             answer[i] = answer[i-1]
#         else:
#             for j in range(i+1, n):
#                 if numbers[i] < numbers[j]:
#                     answer[i] = numbers[j]
#                     break
#             else:
#                 answer[i] = -1
#         before_num = numbers[i]
#     return answer