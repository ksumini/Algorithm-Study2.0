class Node:
    def __init__(self, ID, capability, parent, child):
        self.ID = ID
        self.capability = capability
        self.parent = parent
        self.child = child


Nodes = {}  # ID: Node

def create_Nodes(num, links):
    """
    Create Nodes(ID=Node).

    :param num:
    :param links:
    :return:
    """
    global Nodes
    N = len(num)

    for i in range(N):  # id: 0 ~ N-1
        Nodes[i] = Node(i, num[i], -1, links[i])

    for i, link in enumerate(links):  # find parent
        if link[0] != -1:  # left child
            Nodes[link[0]].parent = i
        if link[1] != -1:  # right child
            Nodes[link[1]].parent = i

    return None

def solution(k, num, links):
    global Nodes
    create_Nodes(num, links)
    

    answer = 0
    return answer

def show_Nodes():
    """
    Show Nodes
    :return:
    """
    global Nodes
    for k, v in Nodes.items():
        print("Node", k, "(num, parent, child) :", v.capability, v.parent, v.child)
    return None

def string_to_list(s: str) -> list:
    # 문자열의 대괄호를 제거하고 쉼표로 분할
    elements = s.strip('[]').split('], [')

    # 각 부분 문자열을 리스트로 변환
    result = []
    for element in elements:
        # 각 요소의 대괄호를 제거하고 쉼표로 분할
        sub_elements = element.replace('[', '').replace(']', '').split(', ')
        # 정수로 변환하여 리스트에 추가
        sublist = [int(sub_element) for sub_element in sub_elements]
        result.append(sublist)

    return result

import sys
sys.stdin = open("example.txt")
k = int(input())
num = string_to_list(input())[0]
links = string_to_list(input())

solution(k, num, links)
show_Nodes()