"""
<문제>
정수로 이루어진 배열 numbers
모든 원소에 대해 뒷 큰수들을 차례대로 담은 배열을 return
(단, 뒷 큰수가 존재하지 않는 원소는 -1을 담는다)

<제한 사항>
- 4 ≤ numbers의 길이 ≤ 1,000,000
    - 1 ≤ numbers[i] ≤ 1,000,000

<풀이 시간>
25분

<풀이>
스택을 이용한 풀이
numbers의 길이가 최대 1,000,000이기 때문에 최악의 경우 O(NlogN)으로 풀이해야 한다.
코드에서는 stack을 이용해 O(N)으로 풀이했다.
맨 뒤의 수는 항상 뒷큰수를 가질 수 없기 때문에 -1로 고정하고, 뒤에서부터 역순으로 탐색한다.
각 원소는 한 번 추가되고 한 번 제거되므로 총 제거 작업의 횟수는 최대 'n'번

1. 바로 뒤 원소가 더 크면 뒷 큰수를 해당 수로 업데이트한다.
2. 그렇지 않다면, 스택에 들어온 순서대로 탐색하며, numbers[i]보다 크면서 가장 가까운 원소를 찾는다.

<시간 복잡도>
O(N)
"""


def solution(numbers: list) -> list:
    answer = [-1] * len(numbers)
    stack = [numbers[-1]]
    for i in range(len(numbers)-2, -1, -1):
        # 스택에 들어온 순서대로 탐색, numbers[i]보다 큰 원소를 발견할 때까지
        while stack and stack[-1] <= numbers[i]:
            stack.pop() # 원소 제거, 어차피 다음 순회할 원소 입장에서도 필요 없는 수이기 때문
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])
    return answer
