'''
[2024-06-13] heewon #96

## 접근 방식
- 좌표의 데이터를 기준으로 딕셔너리를 만들어서 구현을 했지만 fail 다양한 반례를 찾았지만 포기
- union-find 알고리즘 문제 어려워함 -> 연습 필요하다고 생각
  
## 추가 정보
- 시간: 2 hour 이상
- 힌트: [힌트](https://school.programmers.co.kr/questions/56342)
'''

# 부모 노드 정보를 저장하는 사전
parent = {(i, j): (i, j) for i in range(1, 51) for j in range(1, 51)}

# 51 x 51 크기의 2차원 리스트를 사용하여 데이터 저장 (초기값은 'EMPTY')
table = [['EMPTY' for _ in range(51)] for _ in range(51)]


def get_data(cur:tuple)->str:
    """
    주어진 좌표 (cur)의 부모 노드 좌표 데이터를 반환하는 함수

    Args:
        cur: 좌표 (행, 열) 튜플

    Returns:
        해당 좌표의 데이터 (초기값은 'EMPTY')
    """
    r, c = find_parent(cur)  # 실제 부모 노드 좌표 찾기
    return table[r][c]


def find_parent(cur:tuple)->tuple:
    """
    주어진 좌표 (cur)의 최상위 부모 노드 좌표를 반환하는 함수 (Path Compression 이용)

    Args:
        cur: 좌표 (행, 열) 튜플

    Returns:
        최상위 부모 노드 좌표 (행, 열) 튜플
    """
    if parent[cur] == cur:
        return cur
    parent[cur] = find_parent(parent[cur])  # 재귀적으로 부모 노드 찾기
    return parent[cur]  # 최상위 부모 노드 반환


def update1(cur:tuple, val:str)->None:
    """
    주어진 좌표 (cur)의 데이터를 val로 업데이트하는 함수

    Args:
        cur: 좌표 (행, 열) 튜플
        val: 업데이트할 값
    """
    r, c = find_parent(cur)  # 실제 부모 노드 좌표 찾기
    table[r][c] = val


def update2(val1:str, val2:str)->None:
    """
    table 전체를 순회하여 val1 값을 val2 값으로 일괄 변경하는 함수

    Args:
        val1: 변경할 값
        val2: 변경될 값
    """
    for i in range(1, 51):
        for j in range(1, 51):
            if table[i][j] == val1:
                table[i][j] = val2


def merge(cur1:tuple, cur2:tuple)->None:
    """
    두 좌표 (cur1, cur2)를 같은 집합으로 합치하는 함수

    Args:
        cur1: 좌표 (행, 열) 튜플
        cur2: 좌표 (행, 열) 튜플
    """
    p1 = find_parent(cur1)  # cur1의 최상위 부모 노드
    p2 = find_parent(cur2)  # cur2의 최상위 부모 노드
    if get_data(p1) == 'EMPTY':
        parent[p1] = p2  # p1의 부모를 p2로 설정 (좌표1 데이터가 없는 경우)
    else:
        parent[p2] = p1  # p2의 부모를 p1로 설정 (좌표2 데이터가 있는 경우)


def unmerge(cur:tuple)->None:
    """
    주어진 좌표 (cur)를 포함하는 집합을 분리하는 함수

    Args:
        cur: 좌표 (행, 열) 튜플
    """
    pcur = find_parent(cur)  # cur의 최상위 부모 노드
    value = get_data(cur)  # cur의 데이터 저장

    stack = []
    # cur과 같은 집합에 속한 모든 좌표 찾기
    for i in range(1, 51):
        for j in range(1, 51):
            key = (i, j)
            if find_parent(key) == pcur:
                stack.append(key)
                if key == cur:
                    table[i][j] = value  # cur의 원래 데이터 복원
                else:
                    table[i][j] = 'EMPTY'  # 다른 좌표는 'EMPTY'로 변경

    # 분리된 각 좌표의 부모 노드를 자기 자신으로 설정
    for key in stack:
        parent[key] = key


def solution(commands:list)->list:
    answer = []
    for command in commands:
        command, *args = command.split()
        if command == 'UPDATE':
            if len(args) == 3:
                r, c, value = int(args[0]), int(args[1]), args[2]
                update1((r, c), value)
            else:
                value1, value2 = args
                update2(value1, value2)
        elif command == 'MERGE':
            r1, c1, r2, c2 = map(int, args)
            merge((r1, c1), (r2, c2))
        elif command == 'UNMERGE':
            r, c = map(int, args)
            unmerge((r, c))
        elif command == 'PRINT':
            r, c = map(int, args)
            answer.append(get_data((r, c)))
    return answer
