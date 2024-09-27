'''
## 접근 방식
- 1st method - dp
  - y를 만드는 최적의 방법은 이전의 값으로 구할 수 있으므로 DP로 접근
  - 갱신이 안 된 dp 값은 연산할 필요 없음
  - 최소값으로 갱신

- 2nd method - bfs
  - x에서 y 모두를 확인하지 않고 구하는 방법
  - bfs로 접근하여 이동 마다 반복
  - 방문 가능한 위치 저장
  - 방문 불가 -1

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`
'''

# dp
# 시간 복잡도 O(y)
def solution(x, y, n):
    dp = [1000001] * (y + 1)    # dp 할당
    dp[x] = 0                   # x 값 0
    for idx in range(x, y): 
        if dp[idx] != 1000001:  # 변환된 값인지 판별
            for new_idx in [idx + n, idx * 2, idx * 3]: # 세 가지 이동 방법 (n만큼 더하기, 2배, 3배)
                if new_idx <= y and dp[new_idx] > dp[i] + 1:    # new_idx가 y 보다 작고 기존 값 보다 작으면 갱신
                    dp[new_idx] = dp[i] + 1

    return dp[y] if dp[y] != 1000001 else -1

# bfs
# 시간 복잡도 O(y)
def solution(x, y, n):
    """
    주어진 시작 위치 `x`에서 타겟 위치 `y`까지 이동하는 최소 점프 횟수를 찾는 함수입니다. 
    이동 방법은 현재 위치에서 n만큼 더하기, 2배 하기, 3배 하기 중 하나를 선택하여 이동하며, 
    1 ≤ x ≤ y ≤ 1,000,000
    1 ≤ n < y

    Args:
        x: 시작 위치입니다.
        y: 도착하려는 타겟 위치입니다.
        n: 한 번 이동할 수 있는 값입니다.

    Returns:
        시작 위치에서 타겟 위치까지 이동하는 최소 점프 횟수입니다. 만약 이동 불가능한 경우 -1을 반환합니다.
    """

    # 방문한 위치 집합 (처음에는 시작 위치만 포함)
    visited_positions = set([x])

    # 탐색 단계 반복 (방문해야 할 위치가 남아 있을 때까지)
    answer = 0  # 이동 횟수를 카운트하는 변수
    
    # 시작 위치 = 타켓 위치
    if x == y:
        return 0
    
    while visited_positions:
        # 현재 단계에서 방문한 위치 정보 이용
        previous_visited = visited_positions
        visited_positions = set()  # 다음 단계 방문 위치 집합 초기화

        # 현재 단계에서 방문한 모든 위치에 대해 세 가지 이동 방법 시뮬레이션
        for current_position in previous_visited:
            for new_position in [current_position + n, current_position * 2, current_position * 3]:
                if new_position == y:
                    return answer + 1
                # 이동 범위 제한 조건 검사 (0 이상 y 이하)
                if new_position <= y and new_position not in previous_visited:
                    visited_positions.add(new_position)

        answer += 1  # 한 단계 완료, 이동 횟수 증가

    # 모든 경우를 탐색했는데도 타겟 위치 도달 불가능
    return -1
