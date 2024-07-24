def solution(beginning, target):
    """
    주어진 시작 상태 `beginning` 과 목표 상태 `target` 의 2차원 배열에서,
    행과 열을 뒤집는 최소 연산 횟수를 계산하는 함수입니다.

    Args:
        beginning: 시작 상태의 2차원 배열입니다.
        target: 목표 상태의 2차원 배열입니다.

    Returns:
        최소 연산 횟수를 반환합니다. 만약 불가능한 경우 -1을 반환합니다.
    """

    if beginning == target:
        return 0  # 시작 상태와 목표 상태가 동일한 경우 0번의 연산

    n, m = len(beginning), len(beginning[0])  # 배열의 행과 열 크기

    def reverse_rows(maps, idxs):
        """
        지정된 행들을 뒤집는 함수입니다.
        """
        return [[1 - cell if row_idx in idxs else cell for cell in row] for row_idx, row in enumerate(maps)]

    def reverse_columns(maps, idxs):
        """
        지정된 열들을 뒤집는 함수입니다.
        """
        return [[1 - cell if col_idx in idxs else cell for col_idx, cell in enumerate(row)] for row in maps]

    def get_diff_rows(maps, target):
        """
        두 배열의 첫 번째 행이 다른 경우 해당 행의 인덱스를 반환하는 함수입니다.
        """
        return [row_idx for row_idx, (row, target_row) in enumerate(zip(maps, target)) if row[0] != target_row[0]]

    def get_diff_columns(maps, target):
        """
        두 배열의 첫 번째 열이 다른 경우 해당 열의 인덱스를 반환하는 함수입니다.
        """
        return [col_idx for col_idx in range(len(maps[0])) if maps[0][col_idx] != target[0][col_idx]]

    def count_operations(beginning, target):
        """
        시작 상태에서 목표 상태로 변환하기 위한 최소 연산 횟수를 계산하는 함수입니다.

        Args:
            beginning: 시작 상태의 2차원 배열입니다.
            target: 목표 상태의 2차원 배열입니다.

        Returns:
            최소 연산 횟수를 반환합니다.
        """
        operations = 0

        # 첫 번째 열을 맞추기 위해 필요한 열 뒤집기 연산
        col_indices = get_diff_columns(beginning, target)
        beginning = reverse_columns(beginning, col_indices)
        operations += len(col_indices)

        # 첫 번째 행을 맞추기 위해 필요한 행 뒤집기 연산
        row_indices = get_diff_rows(beginning, target)
        beginning = reverse_rows(beginning, row_indices)
        operations += len(row_indices)

        # 모든 요소가 일치하는지 확인
        if beginning == target:
            return operations

        # 불가능한 경우
        return float('inf')

    # 첫 번째 행을 뒤집은 경우와 뒤집지 않은 경우의 최소 연산 횟수 비교
    min_operations = min(
        count_operations(beginning, target),
        count_operations(reverse_rows(beginning, [0]), target) + 1
    )

    return min_operations if min_operations != float('inf') else -1