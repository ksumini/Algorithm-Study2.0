"""
<문제>
50 x 50 크기의 표, 모든 셀은 비어있다.
- 각 셀은 '문자열' 값을 가질 수 있다.
- 다른 셀과 병합될 수 있다.

1. UPDATE r c value
- (r, c) 위치의 셀을 선택
- 선택한 셀의 값을 value로 변경

2. UPDATE value1 value2
- value1을 가지고 있는 모든 셀을 선택
- 선택한 셀의 값을 value2로 변경

3. MERGE r1 c1 r2 c2
- (r1, c1)과 (r2, c2) 셀을 병합
- (r1 == r2) & (r2 == c2): 무시
- 인접하지 않은 경우, 그 사이에 위치한 셀들은 영향을 받지 않는다.
- 두 셀 중 한 셀이 값을 가지고 있을 경우, 병합된 셀은 그 값을 갖는다
- 두 셀 모두 값을 가지고 있는 경우, 병합된 셀은 (r1, c1) 셀의 값을 갖는다.
- 이후, (r1, c1)과 (r2, c2) 중 어느 위치를 선택해도 병합된 셀로 접근한다.

4. UNMERGE r c
- (r, c) 셀을 선택해 해당 셀의 모든 병합을 해제한다.
- 선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기 상태로 돌아간다.
- 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가지게 된다.

5. PRINT r c
- (r, c) 셀의 값을 출력한다. (비어있는 경우 "EMPTY" 출력)

<제한 사항>
1 <= commands의 길이 <= 1,000
- commands의 각 원소는 다음의 5가지 중 하나
    - "UPDATE r c value"
    - "UPDATE value1 value2"
    - "MERGE r1 c1 r2 c2"
    - "UNMERGE r c"
    - "PRINT r c"

<풀이 시간>
1시간 20분

<풀이>
각각의 command에 대한 함수 구현(서로소 집합 알고리즘을 사용해서 풀이)
"""

table = [['' for _ in range(51)] for _ in range(51)]    # r, c 좌표를 그대로 사용하기 위해 51x51로 선언
P = [[(r, c) for c in range(51)] for r in range(51)]    # Union-Find Parent Table

answer = []     # 출력을 담을 정답 리스트


def print_cell(r: int, c: int):
    """
    - (r, c) 위치의 셀을 선택하여 셀의 값을 출력, 선택한 셀이 비었을 경우 'EMPTY' 출력
    - 셀이 병합된 경우 루트 좌표만 값을 가지고 있으므로 find를 통해 루트 좌표를 가져와서 해당 값을 출력해야 한다.
    - 출력은 answer 리스트에 담는 것으로 대체
    """
    r, c = find(r, c)
    answer.append(table[r][c]) if table[r][c] else answer.append("EMPTY")


def update_point(r: str, c: str, value: str):
    """
    - (r, c) 위치의 셀을 선택해 value로 값을 바꾼다.
    - 셀이 병합된 경우 루트 좌표만 값을 가지고 있으므로 find를 통해 루트 좌표를 가져와서 해당 값을 변경해야 한다.
    """
    r, c = find(int(r), int(c))
    table[r][c] = value


def update_value(v1: str, v2: str):
    """
    - v1을 값으로 가지고 있는 모든 셀의 값을 v2로 변경
    - 51x51 크기이므로 bruth force로 가능
    - 셀이 병합된경우 루트 좌표만 값을 가지고 있으므로 현재 루트이면서, 값이 v1인 셀들을 변경해줘야한다.
    - 루트 노드를 찾기 위한 find가 여기서도 역시 필요하다.
    """
    for row in range(51):
        for col in range(51):
            # 현재 루트이면서, 값이 v1인 셀들을 변경해줘야 함
            if table[row][col] == v1:
                table[row][col] = v2


def find(r: int, c: int):
    """
    - Parent table `P`의 각 셀은 좌표를 값으로 가지고 있다
    - 셀의 위치와 값이 같은 경우 해당 좌표는 루트 노드
    - 다른 좌표를 값으로 가진 경우 해당 값은 상위(부모)노드의 좌표이며, 값은 상위(부모) 노드를 따라간다
    - find는 값으로 본인의 좌표를 가지는 루트 노드를 탐색해 루트 노드의 좌표를 반환한다
    """
    # 자기 자신의 좌표를 값으로 가지는 루트 노드가 나올 때까지
    while (r, c) != P[r][c]:
        # 상위(부모) 노드를 타고 루트로 올라감
        r, c = P[r][c]
    # 루트 노드 좌표 반환
    return r, c


def union(r1, c1, r2, c2):
    """
    - 두 disjoint set의 루트 노드를 병합함 (r1, c1) <- (r2, c2)
    - (r1, c1), (r2, c2)는 각 set의 루트 노드임을 가정
    """
    # (r2, c2)의 Parent Table 값을 (r1, c1)으로 변경하므로써 두 노드 병합
    P[r2][c2] = P[r1][c1]


def merge(r1, c1, r2, c2):
    """
    - (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합
    - (r1, c1) 위치에 값이 있으면 해당 셀의 값을 따라감
    - 두 좌표가 각각 병합되어있을 수 있으므로 find를 통해 두 좌표의 루트를 찾아 병합
    """
    # 두 좌표가 각각 병합되어있을 수 있으므로 find를 통해 두 좌표의 루트를 찾아 병합
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    # 같은 셀일 경우 무시
    if r1 == r2 and c1 == c2:
        return
    # 위치에 값이 있으면 해당 셀의 값을 따라감
    if table[r1][c1]:
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)


def unmerge(r, c):
    """
    - (r, c) 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제
    - 병합되어있던 모든 셀은 (r, c)를 제외하고 모두 초기값('')을 가짐
    - (r, c)는 기존 값을 가짐
    - 모든 좌표를 순회해 (r, c)의 루트 노드(pr, pc)의 하위 노드를 모두 초기화 해야 함
        - 이 때, 좌표를 먼저 모두 구한 후 다시 그 좌표들을 순회하는 순서로 초기화를 진행해야 함
        - 좌표를 구하면서 초기화를 진행하면 해당 좌표를 상위(부모)노드로 갖고 있던 좌표는 루트를 잃어버림 
    """
    # (r, c)의 부모노드 (pr, pc)
    pr, pc = find(r, c)
    value = table[pr][pc]
    unmerge_list = []

    # (pr, pc)를 루트로 가지는 좌표를 먼저 모두 구한 후
    for row in range(51):
        for col in range(51):
            if find(row, col) == (pr, pc):
                unmerge_list.append((row, col))
    # 다시 그 좌표들을 순회하는 순서로 초기화를 진행
    for row, col in unmerge_list:
        P[row][col] = (row, col)
        table[row][col] = ''
    # (r, c)는 기존 값을 가짐
    table[r][c] = value


def solution(commands: list) -> list:
    for command in commands:
        com, *info = command.split()
        # 1. PRINT
        if com == 'PRINT':
            r, c = map(int, info)
            print_cell(r, c)
        # 2. UPDATE
        elif com == 'UPDATE':
            # 2-1. UPDATE r c value
            if len(info) == 3:
                r, c, value = info
                update_point(r, c, value)
            # 2-2. UPDATE value1 value2
            else:                               
                v1, v2 = info
                update_value(v1, v2)
        # 3. MERGE
        elif com == 'MERGE':
            r1, c1, r2, c2 = map(int, info)
            merge(r1, c1, r2, c2)
        # 4. UNMERGE
        elif com == 'UNMERGE':
            r, c = map(int, info)
            unmerge(r, c)

    return answer


if __name__ == "__main__":
    # 테스트 케이스
    print(solution(commands=["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
    print(solution(commands=["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))