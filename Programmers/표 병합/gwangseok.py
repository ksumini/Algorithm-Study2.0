def update_cell(r: int, c: int, v: str):
    # cell 값 업데이트
    cur_k = (r, c)
    group_idx = cell__group_and_value[cur_k][0]
    
    # 그룹에 속하면 해당하는 cell값도 업데이트
    for k in group__cell[group_idx]:
        cell__group_and_value[k][1] = v
    

def update_value(v1: str, v2: str):
    # v1에 해당하는 것들 v2로 업데이트
    for k in cell__group_and_value.keys():
        if cell__group_and_value[k][1] == v1:
            cell__group_and_value[k][1] = v2    
    

def merge(r1: int, c1: int, r2: int, c2: int):
    key1 = (r1, c1)
    key2 = (r2, c2)
    grp_idx1 = cell__group_and_value[key1][0]
    grp_idx2 = cell__group_and_value[key2][0]
    
    # 같은 그룹이면 아무 것도 안 함.
    if grp_idx1 == grp_idx2:
        return
    
    value1 = cell__group_and_value[key1][1]
    value2 = cell__group_and_value[key2][1]
    
    # key2 그룹 애들을 key1 그룹 으로 넣음
    group__cell[grp_idx1].extend(group__cell[grp_idx2])
    
    # key2에 속하는 cell의 grp 업데이트
    for k in group__cell[grp_idx2]:
        cell__group_and_value[k][0] = grp_idx1
    
    # key1, key2 그룹의 value를 바꿈.
    if value1:
        # key1 값 있음 -> key1 값으로 업데이트
        update_cell(*key2, value1)
    else:
        if value2:
            # key2 값만 있음 -> key2 값으로 업데이트
            update_cell(*key1, value2)
    
    del group__cell[grp_idx2]
    
    
def unmerge(r: int, c: int, new_grp_idx: int):
    key = (r, c)
    cur_gidx = cell__group_and_value[key][0]
    
    # unmerge 하면서 새로운 grp으로 각각 할당
    # key 값에 해당하는 것은 value 그대로 유지
    for k in group__cell[cur_gidx]:
        if k == key:            
            cell__group_and_value[k][0] = new_grp_idx
        else:
            cell__group_and_value[k] = [new_grp_idx, None]
            
        group__cell[new_grp_idx] = [k]
        new_grp_idx += 1
        
    del group__cell[cur_gidx]
    
    return new_grp_idx
    

def print_cell(r: int, c: int):
    k = (r, c)
    v = cell__group_and_value[k]
    
    if v[1] is None:
        return 'EMPTY'
    else:
        return v[1]
    

def initialize(size):
    # EMPTY를 그룹 짓기 위해 처음에 초기화 해줌
    group__cell = {}  # k: grp idx, v: grp에 속하는 cell 좌표
    cell__group_and_value = {}  # k: cell 좌표, v: [grp idx, 값]
    
    idx = 0
    for r in range(1, size + 1):
        for c in range(1, size + 1):
            group__cell[idx] = [(r, c)]
            cell__group_and_value[(r, c)] = [idx, None]
            idx += 1
    
    return group__cell, cell__group_and_value
    

def solution(commands):
    global group__cell, cell__group_and_value
    size = 50
    group__cell, cell__group_and_value = initialize(size)
    new_grp_idx = size ** 2
    answer = []
    
    for command in commands:
        cmd = command.split(' ')
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                update_cell(int(cmd[1]), int(cmd[2]), cmd[3])
            else:
                update_value(cmd[1], cmd[2])
        elif cmd[0] == 'MERGE':
            merge(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
        elif cmd[0] == 'UNMERGE':
            new_grp_idx = unmerge(int(cmd[1]), int(cmd[2]), new_grp_idx)
        else:
            answer.append(print_cell(int(cmd[1]), int(cmd[2])))

    return answer
