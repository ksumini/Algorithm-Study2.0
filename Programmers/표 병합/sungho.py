from collections import defaultdict

GROUP = defaultdict(lambda: None)  # MERGE_NUM: [(r1, c1), (r2, c2) ...]
GROUP_IDX = defaultdict(lambda: None)  # (r,c): MERGE_NUM
MERGE_NUM = 1

board = [[0] * 51 for i in range(51)]  # 0 means 'blank'

def Rule1(q: list):
    """
    Update cell[r][c] as value

    Params:
        list q : ["UPDATE", "r", "c", "value"]
    """
    global board, GROUP, GROUP_IDX
    r, c, value = int(q[1]), int(q[2]), q[3]

    if GROUP_IDX[(r, c)]:  # if (r,c) is in merge group
        merge_num = GROUP_IDX[(r, c)]
        group = GROUP[merge_num]
        for RC in group:
            board[RC[0]][RC[1]] = value  # change elements of merge group as value
    else:  # if (r,c) is not in merge group
        board[r][c] = value
    return None

def Rule2(q: list):
    """
    Update value1 to value2

    Params:
        list q : ["UPDATE", "value1", "value2"]
    """
    global board
    value1, value2 = q[1], q[2]

    for i in range(1, 51):
        for j in range(1, 51):
            if board[i][j] == value1:
                board[i][j] = value2  # change value1 to value2
    return None

def Rule3(q: list):
    """
    Merge (r1,c1) to (r2, c2)
    if board[r1][c1] has no value(=0), use value board[r2][c2]

    Params:
        list q : ["MERGE", "r1", "c1", "r2", "c2"]
    """
    global board, GROUP, GROUP_IDX, MERGE_NUM
    r1, c1, r2, c2 = int(q[1]), int(q[2]), int(q[3]), int(q[4])

    if r1 == r2 and c1 == c2:  # same cell
        return None
    if GROUP_IDX[(r1, c1)] and GROUP_IDX[(r1, c1)] == GROUP_IDX[(r2, c2)]:  # same merge group
        return None

    # group1(in r1, c1)
    group1 = [(r1, c1)]
    merge_num1 = None
    if GROUP_IDX[(r1, c1)]:
        merge_num1 = GROUP_IDX[(r1, c1)]
        group1 = GROUP[merge_num1]

    # group2(in r2, c2)
    group2 = [(r2, c2)]
    merge_num2 = None
    if GROUP_IDX[(r2, c2)]:
        merge_num2 = GROUP_IDX[(r2, c2)]
        group2 = GROUP[merge_num2]

    if board[r1][c1] != 0: # board[r1][c1] has value
        if merge_num1 == None: # if r1, c1 is no merge group, need to new merge group
            merge_num1 = MERGE_NUM
            GROUP_IDX[(r1, c1)] = merge_num1
            GROUP[merge_num1] = [(r1, c1)]
            MERGE_NUM += 1

        for RC in group2:
            GROUP_IDX[(RC[0], RC[1])] = merge_num1 # change merge_num(merge_num2 -> merge_num1) in group2 elements
            GROUP[merge_num1].append(RC) # append (r2, c2) group elements in merge group 1
            board[RC[0]][RC[1]] = board[r1][c1] # set (r2, c2) group elements as (r1, c1) value

        if merge_num2 != None: # if r2, c2 is merge group, need to remove merge group of r2, c2
            GROUP[merge_num2] = None
    else: # board[r1][c1] has no value. (='blank')
        if merge_num2 == None: # if r2, c2 is no merge group, need to new merge group
            merge_num2 = MERGE_NUM
            GROUP_IDX[(r2, c2)] = merge_num2
            GROUP[merge_num2] = [(r2, c2)]
            MERGE_NUM += 1

        for RC in group1:
            GROUP_IDX[(RC[0], RC[1])] = merge_num2  # change merge_num(merge_num2 -> merge_num1) in group2 elements
            GROUP[merge_num2].append(RC)  # append (r2, c2) group elements in merge group 1
            board[RC[0]][RC[1]] = board[r2][c2]  # set (r2, c2) group elements as (r1, c1) value

        if merge_num1 != None: # if r1, c1 is merge group, need to remove merge group of r2, c2
            GROUP[merge_num1] = None
    return None

def Rule4(q: list):
    """
    Unmerge board[r][c]
    if board[r][c] is on group, set board[r][c] as the value of the group and others of the group as 0(blank)

    Params:
        list q : ["UNMERGE", "r", "c"]
    """
    global board, GROUP, GROUP_IDX
    r, c = int(q[1]), int(q[2])

    if GROUP_IDX[(r, c)]:  # r,c has merge group
        merge_num = GROUP_IDX[(r, c)]
        group = GROUP[merge_num]
        for RCs in group:
            if RCs == (r, c):
                pass
            else:
                board[RCs[0]][RCs[1]] = 0
            del GROUP_IDX[(RCs[0], RCs[1])]
        del GROUP[merge_num]
    else:  # r,c has no merge group
        pass

    return None

def Rule5(q: list, answer: list) -> list:
    """
    save print results of board[r][c]. if board[r][c] is blank, save "EMPTY"

    Params:
        list q : ["PRINT", "r", "c"]
    """
    global board
    r, c = int(q[1]), int(q[2])

    if board[r][c] == 0:  # blank
        answer.append("EMPTY")
    else:  # no blank
        answer.append(board[r][c])
    return answer

def show_board(r=6, c=6):
    """
    Show board. set the row, col

    Params:
        int r: row of board
        int c: col of board
    """
    global board
    print("============ NOW BOARD ============")
    for i in range(1, r):
        print(board[i][1:c])
    return None

def show_status(group = True, group_idx = True):
    """
    Show status GROUP, GROUP_IDX

    Params:
        bool group : option
        bool group_idx : option

    """
    global GROUP, GROUP_IDX
    if group == True:
        print("SHOW GROUP : ", GROUP)
    if group_idx == True:
        print("SHOW GROUP_IDX : ", GROUP_IDX)
    return None

def solution(commands):
    """
    solve commands

    Params:
        list commands : ["UPDATE 1 1 menu", "UPDATE 1 2 category", ...
    """
    stop = -1 # if you want to show intermediate results, you can set 'stop'(=iteration)
    answer = []
    for i, q in enumerate(commands):
        q = q.split()
        if q[0] == 'UPDATE':  # Rule1 or Rule2
            if len(q) == 4:  # Rule1
                Rule1(q)
            else:
                Rule2(q)
        elif q[0] == 'MERGE':
            Rule3(q)
        elif q[0] == 'UNMERGE':
            Rule4(q)
        elif q[0] == 'PRINT':
            answer = Rule5(q, answer)

        if stop == i:
            print("STOP NOW ", i, " command. : ", q)
            show_board()
            show_status()

    #print(answer)
    return answer