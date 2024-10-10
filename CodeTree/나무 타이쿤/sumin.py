"""
<문제>
n x n 격자 칸에 리브로수(나무)를 키우려고 한다.
격자에는 서로 다른 높이를 가진 리브로수가 주어진다.
'특수 영양제'를 사용해 리브로수를 키울 수 있다.
- 리브로수가 있으면 높이를 1 증가 시킨다.
- 리브로수가 없으면(씨앗만 있으면, 높이=0) 높이 1의 리브로수를 만들어낸다.
- 초기 '특수 영양제'는 n x n 격자의 좌하단의 4칸

특수 영양제는 '이동 규칙'에 따라 움직인다.
- '이동 방향'과 '이동 칸 수'가 주어진다.
    - '이동 방향': 1~8(→ ↗ ↑ ↖ ← ↙ ↓ ↘)

격자의 모든 행, 열은 각각 끝과 끝이 연결돼있다.

<1년 동안 아래의 단계로 성장>
1. '특수 영양제'를 '이동 규칙'에 따라 이동시킨다.
2. '특수 영양제'를 이동 시킨 후 해당 땅에 '특수 영양제' 투입(투입 후 특수 영양제는 사라짐)한다.
3. '특수 영양제'를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는만큼 높이가 더 성장한다.
(대각선 인접칸이 격자를 벗어나는 경우는 세지 않는다)
4. '특수 영양제'를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 '특수 영양제'를 사고, 해당 위치에 특수 영양제를 올려둔다.

주어진 '리브로수를 키우는 총 년수가 모두 지나고 난뒤 남아있는 리보로수 높이들의 총 합'을 구하라

<제한 사항>
3 ≤ n ≤ 15
1 ≤ m ≤ 100
0 ≤ 초기에 주어지는 리브로수의 높이 ≤ 100
1 ≤ d ≤ 8
1 ≤ p ≤ min(n, 10)

<풀이>
풀이 시간: 1시간 25분

<시간 복잡도>
O(m x n**2)
"""
# n: 격자의 크기, m: 리브로수를 키우는 총 년 수
n, m = map(int, input().split())

# 리브로수의 높이
height = [list(map(int, input().split())) for _ in range(n)]

# 각 년도의 이동 규칙 (d: 이동 방향, p: 이동 칸 수)
rules = [list(map(int, input().split())) for _ in range(m)]

# 이동 방향 (→ ↗ ↑ ↖ ← ↙ ↓ ↘)
directions = {1: (0, 1), 2: (-1, 1), 3: (-1, 0), 4: (-1, -1), 5: (0, -1), 6: (1, -1), 7: (1, 0),
              8: (1, 1)} 

# 특수 영양제 초기화 (n x n 격자의 좌하단 4칸)
supplements = [(n - 2, 0), (n - 1, 0), (n - 2, 1), (n - 1, 1)]

# m년 동안 리브로수를 키우는 규칙 반복
for i in range(m):
    d, p = rules[i]  # 이동 방향, 이동 칸 수
    dx, dy = directions[d]
    dx, dy = dx * p, dy * p
    # 1. '특수 영양제'를 '이동 규칙에 따라 이동'
    for j in range(len(supplements)):
        x, y = supplements[j]
        nx, ny = (x+dx) % n, (y+dy) % n
        supplements[j] = (nx, ny)
        # 2. '해당 땅에 특수 영양제 투입'
        height[nx][ny] += 1
    # 3. 대각선으로 인접한 방향의 높이가 1 이상인 리브로수의 개수만큼 높이 성장
    adj_height = []
    for k in range(len(supplements)):
        # 현재 확인하고 있는 특수 영양제가 있는 땅의 좌표
        cur_x, cur_y = supplements[k]
        cnt = 0 # 인접한 방향의 높이가 1 이상인 리브로수의 개수
        # 대각선 방향(2: ↗, 4: ↖, 6: ↙, 8: ↘)
        for diag in [2, 4, 6, 8]:
            diag_x, diag_y = directions[diag]
            new_x, new_y = cur_x + diag_x, cur_y + diag_y
            # 격자 범위내의 리브로수만 카운트
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue
            if height[new_x][new_y] >= 1:
                cnt += 1
        adj_height.append(cnt)
    for l in range(len(supplements)):
        cur_x, cur_y = supplements[l]
        height[cur_x][cur_y] += adj_height[l]

    # 4. 특수 영양제를 투입한 리브로수 제외, 높이가 2 이상인 리브로수는 높이를 2로 잘라내고 해당 위치에 특수 영양제 투입
    new_supplements = []
    for i in range(n):
        for j in range(n):
            if height[i][j] >= 2 and (i, j) not in supplements:
                height[i][j] -= 2
                new_supplements.append((i,j))
    supplements = new_supplements

# 5. 남아있는 리브로수의 높이의 총합
total_height = 0
for row in height:
    total_height += sum(row)

print(total_height)