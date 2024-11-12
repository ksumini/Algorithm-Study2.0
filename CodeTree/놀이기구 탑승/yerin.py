import heapq

n = int(input())
answer = 0

order = []  # 탑승 순서
fav_friends = {}  # 학생별 좋아하는 친구 목록
coord_by_student = {}  # 학생별 자리 좌표
unoccupied_seats = {}  # 좌석별 인근 빈 좌석 수

board = [[-1] * n for _ in range(n)]
directions = [(1,0), (-1,0), (0,1), (0,-1)]

# 좌석별 인근 빈 좌석 수
for i in range(n):
    for j in range(n):
        # 내부 : 4, 가장자리 : 3, 모서리 : 2
        unoccupied_seats[(i, j)] = 4 - (i == 0) - (i == n-1) - (j == 0) - (j == n-1)

# 점수 체계
scores_by_friends_cnt = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}

for _ in range(n*n):
    students = list(map(int, input().split()))
    order.append(students[0])
    fav_friends[students[0]] = set(students[1:])

for student in order:
    weight_board = [[0] * n for _ in range(n)]  # 현재 학생이 좋아하는 친구가 주변에 있으면 해당 좌표의 값 + 1 (가중치)
    heap = []  # 주변 친구 수(큰 순), 비어있는 칸 수(큰 순), 행 번호(작은 순), 열 번호(작은 순) <- 우선순위에 따른 최적의 답 하나만 필요하므로 heapq 사용

    # 가중치 보드 값 갱신
    for friend in fav_friends[student]:
        if friend in coord_by_student:
            friend_r, friend_c = coord_by_student[friend]
            for dr, dc in directions:
                nr, nc = friend_r + dr, friend_c + dc
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == -1:
                    weight_board[nr][nc] += 1

    # 자리 모두 돌면서 우선순위 순서대로 데이터 삽입. 인근 친구 수, 빈 좌석 수는 클수록 우선순위가 높으므로 -로 삽입
    for row in range(n):
        for col in range(n):
            if board[row][col] == -1:
                heapq.heappush(heap, (-weight_board[row][col], -unoccupied_seats[(row, col)], row, col))

    # heap에서 가장 첫 번째 값 꺼내서 자리 할당
    _, _, x, y = heapq.heappop(heap)
    board[x][y] = student
    coord_by_student[student] = (x, y)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
            unoccupied_seats[(nx, ny)] -= 1

# 점수 계산
for student in order:
    r, c = coord_by_student[student]
    near_friends_cnt = sum(1 for dr, dc in directions
                           if 0 <= r+dr < n and 0 <= c+dc < n and board[r+dr][c+dc] in fav_friends[student])
    answer += scores_by_friends_cnt[near_friends_cnt]

print(answer)