dy, dx = [0 ,0 ,1 ,-1], [1 ,-1 ,0 ,0]
board = [] # 격자 생성
all_information = {} # all_information[번호] = 좋아하는 학생들

def get_in_board(n, info: list):
    global board, dy, dx, all_information

    location = [0, 0, -n, -n] # liked_cnt, blank_cnt, i, j
    liked_friends = set(info[1:])

    for i in range(1, n+ 1):
        for j in range(1, n + 1):
            liked_cnt, blank_cnt = 0, 0
            if board[i][j] != 0:  # 빈 자리가 아니면 패스
                continue

            for d in range(4):
                ni, nj = i + dy[d], j + dx[d]
                if 1 <= ni <= n and 1 <= nj <= n:  # board 안에 있으면서
                    if board[ni][nj] == 0:  # 옆자리 비어있음
                        blank_cnt += 1
                    elif board[ni][nj] in liked_friends:  # 좋아하는 친구가 옆에 있음
                        liked_cnt += 1

            if location < [liked_cnt, blank_cnt, -i, -j]:
                """
                격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 갑니다.

                만약 1번 조건을 만족하는 칸의 위치가 여러 곳이라면, 그 중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 갑니다. 단 이때 격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다.

                만약 2번 조건까지 동일한 위치가 여러 곳이라면, 그 중 행 번호가 가장 작은 위치로 갑니다.

                만약 3번 조건까지 동일한 위치가 여러 곳이라면, 그 중 열 번호가 가장 작은 위치로 갑니다.
                """
                location = [liked_cnt, blank_cnt, -i, -j]

    board[-location[-2]][-location[-1]] = info[0] #
    all_information[info[0]] = liked_friends # info[0] 학생이 좋아하는 학생들 정보 저장
    return None


def show_board(n: int):
    global board
    for i in range(1, n + 1):
        print(board[i][1:])
    return None

def show_score(n: int):
    global board, all_information, dy, dx

    score_info = [0, 1, 10, 100, 1000]
    total_score = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            liked_cnt = 0
            for d in range(4):
                ni, nj = i + dy[d], j + dx[d]
                if 1 <= ni <= n and 1 <= nj <= n:  # board 안에 있으면서
                    if board[ni][nj] in all_information[board[i][j]]:  # 좋아하는 친구가 옆에 있음
                        liked_cnt += 1 # 좋아하는 친구 숫자 세기
            total_score += score_info[liked_cnt] # board[i][j]의 좋아하는 친구 수에 다라 점수 추가
    print(total_score)
    return None


if __name__ == "__main__":
    n = int(input())
    board = [[0] * (n + 1) for _ in range(n + 1)]

    stop = -1
    for ith in range(1, n * n + 1):
        info = list(map(int, input().split()))  # n0, n1, n2, n3, n4.            1 ~ n*n 사이 수
        get_in_board(n, info)

        if stop == ith:  # 답 확인용
            print("now ", ith, ", info : ", info)
            show_board(n)
            break

    show_score(n)  # 최종점수 출력
