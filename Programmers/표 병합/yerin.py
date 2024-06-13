'''
표 : 50 * 50
r, c : 1~50
cell_val: str, merge O

cmd types:
- "UPDATE r c value"
- "UPDATE value1 value2"
- "MERGE r1 c1 r2 c2"
    한 셀만 값을 가진 경우.
    두 셀 모두 값을 가진 경우.
- "UNMERGE r c"
- "PRINT r c"

한 셀에 병합 여러 번 가능

merge_table: dictionary --> 연결된 인덱스 정보 포

'''
from collections import defaultdict

# "UPDATE r c value" 처리 함수
def update_by_index(r, c, value):
    for nr, nc in merge_table[(r, c)]:
        table[nr][nc] = value

# "UPDATE value1 value2" 처리 함수
def update_by_val(val1, val2):
    if val1 == val2:
        return
    for r in range(1, 51):
        for c in range(1, 51):
            if table[r][c] == val1:
                table[r][c] = val2

# "MERGE r1 c1 r2 c2" 처리 함수
def merge(r1, c1, r2, c2):
    if (r1, c1) == (r2, c2):
        return

    # (r1, c1), (r2, c2)와 각각 병합된 셀 목록 합치기(union 활용)
    merged_set = merge_table[(r1, c1)] | merge_table[(r2, c2)]
    # 병합된 셀 목록 업데이트
    for r, c in merged_set:
        merge_table[(r, c)] = merged_set
    # 병합된 셀과 (r1, c1), (r2, c2)의 값 갱신
    # 둘 다 값이 있을 때는 (r1, c1)의 값으로 갱신
    if table[r1][c1]:
        update_by_index(r1, c1, table[r1][c1])
    else:
        update_by_index(r2, c2, table[r2][c2])

# "UNMERGE r c" 처리 함수
def unmerge(r, c):
    # 병합되지 않은 셀인 경우 리턴
    if merge_table[(r, c)] == {(r, c)}:
        return

    # 기존 값 저장
    original_value = table[r][c]
    # 병합된 셀들의 표 값 빈 문자열로 초기화. 병합된 셀 목록도 자기 자신으로 초기화.
    for nr, nc in merge_table[(r, c)]:
        table[nr][nc] = ""
        merge_table[(nr, nc)] = set([(nr, nc)])
    # (r, c) 표 값 업데이트
    table[r][c] = original_value

def solution(commands):
    global table, merge_table

    answer = []
    # 표 크기 50*50으로 고정. 인덱스가 1부터 시작.
    table = [["" for _ in range(51)] for _ in range(51)]
    # 중복 셀이 없도록 set활용
    merge_table = defaultdict(set)

    # 병합된 셀 목록(merge_table)에 자기 자신을 넣은 것을 기본값으로 설정. 병합할 때 셀 목록 갱신이 용이함
    for r in range(1, 51):
        for c in range(1, 51):
            merge_table[(r, c)].add((r, c))

    # 지시에 따른 케이스 분류
    for cmd in commands:
        parts = cmd.split()
        cmd_type = parts[0]

        if cmd_type == "UPDATE":
            if len(parts) == 4:  # update by index
                r, c = map(int, parts[1:3])
                val = parts[3]
                update_by_index(r, c, val)
            else:
                val1, val2 = parts[1], parts[2]
                update_by_val(val1, val2)

        elif cmd_type == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            merge(r1, c1, r2, c2)

        elif cmd_type == "UNMERGE":
            r, c = map(int, parts[1:])
            unmerge(r, c)

        elif cmd_type == "PRINT":
            r, c = map(int, parts[1:])
            answer.append(table[r][c] if table[r][c] else "EMPTY")

    return answer


print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
