def update_cell(grp_cell: dict, cell_grpnval: dict, r: int, c: int, v: str):
    # cell 값 업데이트
    cur_k = (r, c)
    g_idx, cur_v = cell_grpnval[cur_k][0], cell_grpnval[cur_k][1]
    
    # 그룹에 속하면 해당하는 cell값도 업데이트
    for k in grp_cell[g_idx]:
        cell_grpnval[k][1] = v
    

def update_value(cell_grpnval: dict, v1: str, v2: str):
    # v1에 해당하는 것들 v2로 업데이트
    for k in cell_grpnval.keys():
        if cell_grpnval[k][1] == v1:
            cell_grpnval[k][1] = v2    
    

def merge(grp_cell: dict, cell_grpnval: dict, r1: int, c1: int, r2: int, c2: int):
    key1 = (r1, c1)
    key2 = (r2, c2)
    
    # 같은 그룹이면 아무 것도 안 함.
    if cell_grpnval[key1][0] == cell_grpnval[key2][0]:
        return
    
    # key2 그룹 애들을 key1 그룹 으로 넣음
    grp_idx1 = cell_grpnval[key1][0]
    grp_idx2 = cell_grpnval[key2][0]
    grp_cell[grp_idx1].extend(grp_cell[grp_idx2])
    
    # key2에 속하는 cell의 grp 업데이트
    for k in grp_cell[grp_idx2]:
        cell_grpnval[k][0] = grp_idx1
    
    # key1, key2 그룹의 value를 바꿈.
    if cell_grpnval[key1][1]:
        # key1 값 있음 -> key1 값으로 업데이트
        for k in grp_cell[grp_idx2]:
            cell_grpnval[k][1] = cell_grpnval[key1][1]
    else:
        if cell_grpnval[key2][1]:
            # key2 값만 있음 -> key2 값으로 업데이트
            for k in grp_cell[grp_idx1]:
                cell_grpnval[k][1] = cell_grpnval[key2][1]
    
    del grp_cell[grp_idx2]
    
    
def unmerge(grp_cell: dict, cell_grpnval: dict, r: int, c: int, new_grp_idx: int):
    key = (r, c)
    cur_gidx = cell_grpnval[key][0]
    
    # unmerge 하면서 새로운 grp으로 각각 할당
    # key 값에 해당하는 것은 value 그대로 유지
    for k in grp_cell[cur_gidx]:
        if k == key:            
            cell_grpnval[k][0] = new_grp_idx
        else:
            cell_grpnval[k] = [new_grp_idx, None]
            
        grp_cell[new_grp_idx] = [k]
        new_grp_idx += 1
        
    del grp_cell[cur_gidx]
    
    return new_grp_idx
    

def print_cell(cell_grpnval: dict, r: int, c: int):
    k = (r, c)
    v = cell_grpnval[k]
    
    if v[1] is None:
        return 'EMPTY'
    else:
        return v[1]
    

def initialize(size):
    # EMPTY를 그룹 짓기 위해 처음에 초기화 해줌
    grp_cell = {}  # k: grp idx, v: grp에 속하는 cell 좌표
    cell_grpnval = {}  # k: cell 좌표, v: [grp idx, 값]
    
    idx = 0
    for r in range(1, size + 1):
        for c in range(1, size + 1):
            grp_cell[idx] = [(r, c)]
            cell_grpnval[(r, c)] = [idx, None]
            idx += 1
    
    return grp_cell, cell_grpnval
    

def solution(commands):
    size = 50
    grp_cell, cell_grpnval = initialize(size)
    new_grp_idx = size ** 2
    answer = []
    
    for command in commands:
        cmd = command.split(' ')
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                update_cell(grp_cell, cell_grpnval, int(cmd[1]), int(cmd[2]), cmd[3])
            else:
                update_value(cell_grpnval, cmd[1], cmd[2])
        elif cmd[0] == 'MERGE':
            merge(grp_cell, cell_grpnval, int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
        elif cmd[0] == 'UNMERGE':
            new_grp_idx = unmerge(grp_cell, cell_grpnval, int(cmd[1]), int(cmd[2]), new_grp_idx)
        else:
            answer.append(print_cell(cell_grpnval, int(cmd[1]), int(cmd[2])))

    return answer
