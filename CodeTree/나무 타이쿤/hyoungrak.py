n, m = map(int, input().split())
nnmap = []
for i in range(n):
    nnmap.append(list(map(int, input().split())))

move_rule = ((0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1))  # 움직이는 방향
move = []
for i in range(m):
    move.append(list(map(int, input().split())))

medicine = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]


def moving():  # 특수 영양제 규칙에 맞게 이동
    for i in range(len(medicine)):  # 이동해야 할 규칙에 맞게 이동
        medicine[i][0] += move[0][1] * move_rule[move[0][0] - 1][0]
        medicine[i][1] += move[0][1] * move_rule[move[0][0] - 1][1]

        if medicine[i][0] >= n or medicine[i][0] < 0:  # 격자를 벗어난 좌표값을 0 이상 n-1 이하로 맞춰주기
            medicine[i][0] = medicine[i][0] % n

        if medicine[i][1] >= n or medicine[i][1] < 0:
            medicine[i][1] = medicine[i][1] % n

    move.pop(0)  # 이동한 년도 규칙 삭제


def growing():  # 1 자라고, 인접한 대각선 위치 자라기
    for i in range(len(medicine)):  # 약 있는 위치 1씩 자라기
        nnmap[medicine[i][0]][medicine[i][1]] += 1

    for i in range(len(medicine)):
        grow = 0  # 자라는 수치 초기화
        try:  # 좌표 index가 0 이상 n-1 이하에 존재하는 곳만 체크하려고 try 써줌
            if nnmap[medicine[i][0] - 1][medicine[i][1] - 1] >= 1:
                grow += 1
        except:
            pass

        try:
            if nnmap[medicine[i][0] - 1][medicine[i][1] + 1] >= 1:
                grow += 1
        except:
            pass

        try:
            if nnmap[medicine[i][0] + 1][medicine[i][1] + 1] >= 1:
                grow += 1
        except:
            pass

        try:
            if nnmap[medicine[i][0] + 1][medicine[i][1] - 1] >= 1:
                grow += 1
        except:
            pass

        nnmap[medicine[i][0]][medicine[i][1]] += grow  # 인접 대각에서 높이가 1 이상인 것 만큼 자라기


def cutting():  # 영양제 맞지 않은 땅, 길이 2 이상인 것들 2만큼 자르고, 잘라낸 위치에 약 추가하기
    global medicine
    temp = medicine
    medicine = []
    for i in range(len(nnmap)):
        for j in range(len(nnmap[i])):
            if [i, j] not in temp:
                if nnmap[i][j] >= 2:
                    nnmap[i][j] -= 2  # 자르고
                    medicine.append([i, j])  # 약 추가
            else:
                continue


for i in range(m):
    moving()
    growing()
    cutting()

answer = 0
for i in range(n):
    answer += sum(nnmap[i])
print(answer)
