from typing import List, Tuple

n = int(input())

student_likes = dict()

board = [[0 for _ in range(n)]for _ in range(n)]

# [x, y]에서 학생의 좋아하는 사람 수, 빈 자리 수 구하기
def get_like_blank(x:int, y:int, targets:List)->Tuple:
    likes, blanks = 0, 0
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n:
            if board[nx][ny] in targets:
                likes += 1
            if board[nx][ny] == 0:
                blanks += 1
    return likes, blanks

# 최고의 좌표 구하기
def get_coordinate(student_like:List)->Tuple:
    points = [] # [좋아하는 사람 수, 빈 자리 수, 행, 열]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                points.append([*get_like_blank(i, j, student_like), i, j])
            else:
                points.append([-1, -1, i, j])
    _, _, x, y = sorted(points, key= lambda x: (-x[0], -x[1]))[0]
    return x, y

# [x, y] 학생의 점수 구하기
def get_score(x:int, y:int, student_like:List)->int:
    cnt = 0
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny] in student_like:
            cnt += 1

    return pow(10, cnt - 1) if cnt else 0

# 첫 학생은 무조건 [1, 1] 좌표에 배치
student = list(map(int, input().split()))
board[1][1] = student[0]
student_likes[student[0]] = student[1:]

# 두 번째 학생부터 마지막까지 배치
for _ in range(1, n*n):
    student = list(map(int, input().split()))
    x, y = get_coordinate(student[1:])
    board[x][y] = student[0]
    student_likes[student[0]] = tuple(student[1:])

total_score = 0
for i in range(n):
    for j in range(n):
        total_score += get_score(i, j, student_likes.get(board[i][j]))

print(total_score)