def get_flip_num(board):
    flip_num = 0
    for row in range(len(board)):
        if board[row][0] == 1:
            flip_num += 1
            for col in range(len(board[0])):
                board[row][col] = abs(board[row][col] - 1)
    
    for col in range(len(board[0])):
        if board[0][col] == 1:
            flip_num += 1
            for row in range(len(board)):
                board[row][col] = abs(board[row][col] - 1)
    
    return flip_num


def is_same(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                return False
    
    return True
            

def solution(beginning, target):
    flip_board = [[0] * len(beginning[0]) for _ in range(len(beginning))]
    
    # 뒤집어야 하는지 아닌지를 저장한다.
    for row in range(len(beginning)):
        for col in range(len(beginning[0])):
            flip_board[row][col] = abs(target[row][col] - beginning[row][col]) # 모두 0이 되어야 함.
    
    # Row를 기준으로 첫 번째 col의 값이 다르면 뒤집는다.
    # 이후, col을 기준으로 첫 번째 row의 값이 다르면 뒤집는다.
    # 먼저, 뒤집으면 row와 col의 첫 번째 행도 영향을 받기 때문에 이를 기준으로 뒤집는다.
    # 뒤집어야 하는 row, col이 정해졌으면 어떤 순서로 뒤집든 그 결과는 같다.
    # 따라서 row를 기준으로 다른 것을 모두 뒤집고 이후 col을 기준으로 다른 것을 모두 뒤집는다.
    flip_num = get_flip_num(flip_board)
    
    if is_same(flip_board):
        # flip_board가 모두 0인지 확인한다.
        # 이전과 유사하지만 기준을 col, row로 뒀을 때는 이전에 뒤집지 않은 row, col를 뒤집어야 한다.
        # 따라서 row 개수 + col 개수 - flip_num이 이에 해당한다.
        # 둘 중 적은 값을 answer로 return한다.
        return min(flip_num, len(beginning[0]) + len(beginning) - flip_num)
    else:
        return -1
