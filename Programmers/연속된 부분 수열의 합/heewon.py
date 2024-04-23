'''
## 접근 방식
- `Sliding Window` 방식 적용
    - 부분수열의 합 < k : right 1 증가
    - 부분수열의 합 == k : 최소 길이 배열이면 저장, 길이가 1이면 바로 return
    - 부분수열의 합 > k : left 1 증가

## 추가 정보
- 시간: 1 hour 이하
- 힌트: `None`
'''

def solution(sequence, k):
    """
    주어진 수열(sequence)에서 연속된 부분수열 중 합이 k와 같은 경우가 가장 짧은 부분수열의 시작 인덱스와 끝 인덱스를 반환합니다.

    Args:
        sequence (list): 정수로 이루어진 수열
        k (int): 합이 k와 같은 경우를 찾기 위한 값

    Returns:
        list: 가장 짧은 부분수열의 시작 인덱스와 끝 인덱스를 담은 리스트
    """
    answer = []  # 결과를 담을 리스트
    N = len(sequence)
    min_len = 1000000  # 가장 짧은 부분수열의 길이를 저장할 변수
    start = 0  # 부분수열의 시작 인덱스
    end = 0  # 부분수열의 끝 인덱스
    window_sum = sequence[start]  # 부분수열의 합을 저장할 변수

    while end < N:
        if window_sum == k and min_len > end - start: # 합이 k와 같고 현재 길이가 최소 길이보다 작은 경우
            if start == end:  # 부분수열의 길이가 1인 경우
                return [start, end]  # 시작 인덱스와 끝 인덱스를 반환
            min_len = end - start  # 최소 길이 갱신
            answer = [start, end]  # 결과를 갱신
        if window_sum < k:  # 합이 k보다 작은 경우
            if end == N - 1:  # 수열의 끝에 도달한 경우
                break
            window_sum += sequence[end + 1]  # 다음 요소를 합에 추가
            end += 1  # 끝 인덱스 증가
        else: # 합이 k보다 크거나 같은 경우
            window_sum -= sequence[start]  # 시작 요소를 합에서 제거
            start += 1  # 시작 인덱스 증가


    return answer  # 결과 반환