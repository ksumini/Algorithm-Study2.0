"""
- 실내공조 제어 시스템 : 차내에 승객이 탑승 중일 때 t1~t2를 유지 / 0분 시점 실내온도 = 실외온도
- 희망온도 설정 : 1본 뒤 희망 온도와 같아지는 방향으로 1도 상승 or 하강, 같다면 변하지 않음
- 전원 끔 : 실외 온도와 같아지는 방향으로 매분 1도 상승 or 하강, 같다면 변하지 않음
- 소비 전력 : 희망온도 != 실내온도 -> 매분 a 소비, else b 소비

[접근 방식 - DP (ref)](https://school.programmers.co.kr/questions/52432)
- case 분할
    - 1. 에어컨을 끄고, 실내 온도 방향으로 1도 변경하는 경우
    - 2. 에어컨을 끄고, 온도를 유지하는 경우 (실내온도 == 현재온도)
    - 3. 에어컨을 키고, 온도를 유지하는 경우
    - 4. 에어컨을 키고, 온도를 1도 변경하는 경우
- 2차원 DP 테이블
    - 행 : 시간
    - 열 : 온도 (온도의 범위는 -10~40도 -> 0 ~ 50으로 표현)
    - DP[i][j] = i분 상태의 j를 만들어 낼 수 있는 최소 소비 전력
        - DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1] 세 가지 상황에서만 DP[i][j]를 만들 수 있다.
        - 각 비용을 계산해 최소 비용을 DP[i][j]로 업데이트
"""
from typing import List


def solution(temperature: int, t1: int, t2: int, a: int, b: int, onboard: List[List[int]]) -> int:

    N = len(onboard)
    dp = [[int(10e9) for _ in range(90)] for _ in range(N)]     # 가능한 온도 범위는 -20 ~ 80도, 최대 1000분
    dp[0][temperature] = 0
    # 업데이트 할 시간 범위
    # 0분일 때는 0
    for i in range(1, N):
        # 업데이트 할 온도 범위 제한
        # onboard[i] == 1 일 때에는 t1~t2로 업데이트 될 수밖에 없음
        start = t1 if onboard[i] else min(t1, temperature)
        end = t2 if onboard[i] else max(t2, temperature)

        for j in range(start, end+1):
            # dp[i-1][j-1] -> dp[i][j] (온도를 상승시켜야 하는 경우)
            # 실외 온도보다 목표 온도가 높은 경우 에어컨으로 온도 높히기 필요
            temp_up = dp[i-1][j-1] + a if temperature < j else dp[i-1][j-1]
            # dp[i-1][j] -> dp[i][j] (온도를 유지하는 경우)
            # 실외 온도와 같으면 0, 같지 않다면 에어컨을 켜서 유지
            temp_stay = dp[i-1][j] if temperature == j else dp[i-1][j] + b
            # dp[i-1][j+1] -> dp[i][j] (온도를 낮추는 경우)
            # 실외 온도보다 목표 온도가 낮은 경우 에어컨으로 온도 낮추기 필요
            temp_down = dp[i-1][j+1] + a if temperature > j else dp[i-1][j+1]

            # i분에 j를 만드는 모든 경우 중 최소 값으로 업데이트
            dp[i][j] = min(temp_up, temp_stay, temp_down)

    return min(dp[N-1])


def main():
    case1 = [28, 18, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1]]
    case2 = [-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0]]
    case3 = [11, 8, 10, 10, 1, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]]
    case4 = [11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]]

    print(solution(*case1))
    print(solution(*case2))
    print(solution(*case3))
    print(solution(*case4))


main()
