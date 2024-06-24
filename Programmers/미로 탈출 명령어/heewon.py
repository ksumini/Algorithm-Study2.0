'''
## 접근 방식
- 하, 좌, 우, 상 (d, l, r, u) 순서로 우선 순위를 가진다.
- BFS, DFS는 같은 좌표를 다시 가도 되므로 시간 복잡도가 클 것으로 판단
- 장애물이 없기 때문에 그리디로 접근
- 'impossible' 경우
    - 필수 이동 수보다 k가 작은 경우
    - 추가 이동이 홀수인 경우
- 다음 순서 대로 움직인다.
    1. 필수 하향 이동
    2. 가능한 만큼 추가 하향 이동
        - x값이 n이 되거나 추가 이동할 수 있을 만큼
        - 추가 하향을 한 만큼 마지막(9)에 추가 상향을 해야 함 why? u는 우선 순위 최하
    3. 필수 좌향 이동
    4. 가능한 만큼 추가 좌향 이동
        - y값이 1이 되거나 추가 이동할 수 있을 만큼
        - 추가 좌향을 한 만큼 나중(7)에 추가 우향을 해야 함
    5. 추가 이동이 남으면 가능한 만큼 우향, 좌향 이동 반복
        - 여기서 남은 추가 이동 횟수 소진
    6. 필수 우향 이동
    7. 추가 우향 이동
        - 4에서 이동한 만큼 우향 이동
    8. 필수 상향 이동
    9. 추가 상향 이동
        - 2에서 이동한 만큼 상향 이동
- 변수 실수로 test case 4번을 fail 했다. 반례 문제가 아니라 실수 때문에 시간을 날렸다. 실수를 조심하자!


## 추가 정보
- 시간: 1 hour
- 힌트: `None`
'''
# 이동 방향: 하, 좌, 우, 상 (d, l, r, u)

def solution(n, m, x, y, r, c, k):
    # 이동 경로를 저장할 변수
    answer = ''
    
    # 목표 지점까지의 필수 이동 거리
    essential_dx = r - x
    essential_dy = c - y
    
    # 추가 이동 가능 횟수
    additional_move = k - abs(essential_dx) - abs(essential_dy)
    
    # 추가 이동 횟수가 부족하거나, 남은 이동 횟수로 목적지에 도달할 수 없는 경우
    if additional_move < 0 or additional_move % 2 == 1:
        return 'impossible'
    
    # 현재 위치
    now_x = x
    now_y = y
    
    # 추가 이동 거리 초기화
    additional_d = 0
    additional_l = 0
    additional_r = 0
    additional_u = 0
    
    # 필수 이동 (하향)
    if essential_dx > 0:
        now_x += essential_dx
        answer += 'd' * essential_dx
    
    # 추가 이동 (하향)
    if additional_move > 0 and now_x < n:
        additional_d = min(k // 2, n - now_x)
        answer += 'd' * additional_d
        additional_move -= 2 * additional_d
        additional_u += additional_d
    
    # 필수 이동 (좌향)
    if essential_dy < 0:
        now_y += essential_dy
        answer += 'l' * -essential_dy
    
    # 추가 이동 (좌향)
    if additional_move > 0 and now_y > 1:
        additional_l = min(additional_move // 2, now_y - 1)
        answer += 'l' * additional_l
        additional_move -= 2 * additional_l
        additional_r += additional_l
    
    # 추가 이동 (우좌 반복)
    answer += 'rl' * (additional_move//2)
        
    # 필수 이동 (우향)
    if essential_dy > 0:
        answer += 'r' * essential_dy
    
    # 추가 이동 (우향)
    answer += 'r' * additional_r
    
    # 필수 이동 (상향)
    if essential_dx < 0:
        answer += 'u' * -essential_dx
    
    # 추가 이동 (상향)
    answer += 'u' * additional_u
    
    return answer
