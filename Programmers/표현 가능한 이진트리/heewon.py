'''
[2024-06-06] heewon #84

## 함수 설명
- `get_node_depth`: 완전 이진 트리를 만족하게 하는 트리의 높이 구하기
- `dfs`: 해당 트리가 표현 가능한지 확인

## 접근 방식
- number 값을 이진수로 변경하고 '0' 값을 앞에 얼마나 추가할지 구해줘야 함
    - 완전 트리의 노드 개수는 2^n - 1을 만족한다는 성질을 이용
    - 초기 구현: while 문을 이용하여 '0'을 추가해 줬지만 큰 number에 대해서는 불필요하게 많은 시간을 이용함
    - 트리의 높이를 이용 -> number 값을 2로 계속 나누어 주어 높이를 구함 단, 완전 노드 트리의 개수와 같으면 추가 X
- 노드를 확인하는 방법
    - 노드의 가운데 값은 항상 트리의 root 노드이다! -> 노드의 중간 값은 부모 노드이다
    - 부모 노드가 0인데 자식 노드가 1 -> 표현 불가능
    - 노드를 확인하는 과정에서 부모 확인하고 2개의 트리가 생기는 방식 -> DFS로 구현
- 느낀 점
    - 노드 확인하는 방법은 바로 생각함
    - number 앞에 0을 여러 개 추가할 수 있다는 점을 놓침 -> 반례 참고
    

## 사용한 모듈
`None`

## 추가 정보
- 시간: 1 hour 이상(반례 못 찾음 + 코드 Refactoring)
- 힌트: `반례 case`
'''

import math

def solution(numbers:list)->list:
    """
    하나의 이진트리로 표현 가능한지 확인

    Args:
        numbers: 이진트리로 만들고 싶은 수를 담은 1차원 정수 배열

    Returns:
        하나의 이진트리로 해당 수를 표현할 수 있다면 1을, 표현할 수 없다면 0을 1차원 정수 배열
    """
    answer = []
    for number in numbers:
        num_bin = bin(number)[2:]  # 숫자를 이진수 문자열로 변환
        node_depth = get_node_cnt(len(num_bin))  # 완전 이진 트리를 만들기 위한 높이 확인
        num_bin = '0' * (pow(2, node_depth) - 1 - len(num_bin)) + num_bin  # 완전 이진 트리를 만들기 위한 추가 노드 개수 추가
        if dfs(num_bin):  # DFS로 트리 구조 확인
            answer.append(1)  # 조건을 만족하면 1 추가
        else:
            answer.append(0)  # 조건을 만족하지 않으면 0 추가
    return answer

def get_node_depth(node_cnt:int) -> int:
    """
    완전 이진 트리를 만족하게 하는 트리의 높이 구하기

    Args:
        노드 수: 노드의 수

    Returns:
        높이: 완전 이진 트리를 만족하게 하는 트리의 높이
    """
    node_cnt += 1
    depth = 0
    check = True
    while node_cnt > 1:
        depth += 1
        node_cnt, remainder = divmod(node_cnt, 2)  # 노드를 2로 나누어 트리 깊이 계산
        if remainder != 0:
            check = False  # 나머지가 0이 아니면 완전 이진 트리가 아님
    if check:
        return depth  # 완전 이진 트리이면 현재 시간 반환
    return depth + 1  # 완전 이진 트리가 아니면 시간에 1을 더해서 반환

def dfs(nodes:str)->bool:
    """
    해당 트리가 표현 가능한지 확인

    Args:
        nodes: node의 유무를 1, 0으로 표현한 str 값

    Returns:
        False: 불가능 True: 가능
    """
    if len(nodes) == 1:
        return True  # 노드가 하나만 있으면 트리 구조를 만족
    mid = math.ceil(len(nodes) / 2) - 1  # 중간 노드 계산
    if nodes[mid] == '0':  # 중간 노드가 0이면
        if nodes[:mid].count('1') == 0 and nodes[mid+1:].count('1') == 0:  # 좌우 서브트리 모두 1이 없는 경우
            return True  # 트리 구조를 만족
        else:
            return False  # 하나라도 1이 있으면 트리 구조를 만족하지 않음
    return dfs(nodes[:mid]) and dfs(nodes[mid+1:])  # 중간 노드가 1이면 좌우 서브트리를 재귀적으로 검사

print(solution([7, 42, 5])) # [1, 1, 0]
print(solution([63, 111, 95])) # [1, 1, 0]