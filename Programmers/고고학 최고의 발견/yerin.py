from itertools import product


def solution(clockHands):
    n = len(clockHands)  # 시계바늘 배열의 크기 (n x n)
    min_flips = float('inf')  # 최소 회전 수를 무한대로 초기화

    def toggle(x, y, grid, rotations):
        # 주어진 위치 (x, y)에서 시계바늘을 회전시키고 인접한 시계바늘의 상태를 업데이트하는 함수
        directions = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                grid[nx][ny] = (grid[nx][ny] + rotations) % 4

    def apply_flips(initial_flips):
        # 첫 번째 행의 시계바늘 회전 상태를 설정하고 전체 그리드의 상태를 조정하는 함수
        grid = [row[:] for row in clockHands]  # 원본 시계바늘 배열을 복사
        flips = sum(initial_flips)  # 첫 번째 행의 회전 수 합계

        # 첫 번째 행의 시계바늘 상태 설정
        for i in range(n):
            toggle(0, i, grid, initial_flips[i])

        # 두 번째 행부터 마지막 행까지 처리
        for i in range(1, n):
            for j in range(n):
                if grid[i - 1][j] != 0:  # 이전 행의 시계바늘이 12시 방향이 아닌 경우
                    rotations = (4 - grid[i - 1][j]) % 4  # 필요한 회전 수 계산
                    flips += rotations
                    toggle(i, j, grid, rotations)  # 현재 위치와 인접한 시계바늘 상태 업데이트

        # 마지막 행의 모든 시계바늘이 12시 방향인지 확인
        if all(grid[n - 1][j] == 0 for j in range(n)):
            return flips  # 모든 시계바늘이 12시 방향인 경우 회전 수 반환
        return float('inf')

    # 첫 번째 행의 모든 가능한 조합을 생성하여 처리
    for initial_flips in product(range(4), repeat=n):
        print("initial flips :", initial_flips)
        min_flips = min(min_flips, apply_flips(initial_flips))

    return min_flips


print(solution([[0, 3, 3, 0], [3, 2, 2, 3], [0, 3, 2, 0], [0, 3, 3, 3]]))
