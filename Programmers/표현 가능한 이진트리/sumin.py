"""
<문제>
이진 트리로 만들고 싶은 수가 이진 트리로 표현할 수 있다면 1, 없다면 0을 1차원 정수 배열에 담아 return

<제한 사항>
- 1 ≤ numbers의 길이 ≤ 10,000
    - 1 ≤ numbers의 원소 ≤ 1015

<풀이 시간>
1시간 30분

<풀이>
1. 이진수로 변환
2. 포화 이진트리 만들기
3. 포화 이진트리가 제대로 성립하는지 확

<시간복잡도>
O(Nlogm)
- N: 입력 배열 numbers의 길이
- m: 입력 배열에서 가장 큰 숫자
"""
import math


def solution(numbers: list) -> list:
    """
    :param numbers: 이진 트리로 만들고 싶은 수를 담은 1차원 정수 배열
    :return: numbers에 주어진 순서대로 하나의 이진 트리로 해당 수를 표현할 수 있다면 1, 표현할 수 없다면 0을 담은 1차원 정수 배열
    """
    answer = []  # 이진트리로 표현할 수 있는 수(1), 없는 수(0)
    for num in numbers: # 수를 하나씩 확인한다.
        bt = make_tree(num) # 포화 이진트리로 만들어준다.
        if check(bt): # 정상적인 포화 이진트리라면
            answer.append(1) # answer에 1을 추가
        else: # 아니라면
            answer.append(0) # answer에 0을 추가
    return answer


def make_tree(num: int) -> str:
    """
    십진수 num을 이진수로 변환 후, 포화 이진트리로 만드는 함수
    :param num: 주어진 십진수
    :return: (필요한 더미 노드를 추가한) 이진수
    """
    binary_num = bin(num)[2:] # 이진수로 변환
    h = math.ceil(math.log2(len(binary_num) + 1)) # 트리의 높이
    size = 2 ** h - 1 # 노드의 개수
    dummy = size - len(binary_num) # 더미 노드의 개수
    bt = '0' * dummy + binary_num # 포화 이진트리 크기보다 길이가 짧다면 0(더미)를 앞에 붙여준다. (뒤에 붙여주면 값이 변해서 안됨)

    return bt


def check(bt: str) -> bool:
    """
    포화 이진트리가 제대로 성립하는지 확인하는 함수
    :param bt: 이진수
    :return: 해당 이진수로 포화 이진트리가 제대로 성립한다면 True, 아니라면 False
    """
    if len(bt) <= 1: # 노드의 개수가 1개 이하이면 무조건 포화 이진트리임
        return True

    mid = len(bt) // 2
    left_tree = bt[:mid] # 왼쪽 자식 서브트리
    right_tree = bt[mid+1:] # 오른쪽 자식 서브 트리

    root = bt[mid] # 루트 노드
    left = left_tree[len(left_tree)//2] # 왼쪽 서브트리의 부모 노드
    right = right_tree[len(right_tree)//2] # 오른쪽 서브트리의 부모 노드

    if root == '0' and (left == '1' or right == '1'): # 더미노드인 경우 1인 자식 노드를 가질 수 없음
        return False
    else:
        return check(left_tree) and check(right_tree) # 재귀적으로 왼쪽 서브트리와 오른쪽 서브트리를 확인한다.


if __name__ == '__main__':
    print(solution(numbers=[7, 42, 5])) # [1, 1, 0]
    print(solution(numbers=[63, 111, 95])) # [1, 1, 0]