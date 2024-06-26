'''
## 접근 방식
- 문제를 읽고 약수의 개수를 구하는 것임을 빠르게 파악했지만 starts의 최솟값부터 e까지의 풀려고 했으나 시간 복잡도에서 실패하였습니다.
- DP를 적용하여 1부터 e까지의 약수의 개수만 구했지만 테스트 케이스 10에서 시간 초과가 발생하여 다른 방식이 필요하다고 생각했습니다.
- 아무리 생각해 봐도 더 좋은 방식은 떠오르지 않아 막막하던 중 힌트를 보고 제가 생각한 방식이 맞았다는 것을 알게 되어 코드를 작성하였고 정답을 맞힐 수 있었습니다.
- 허무하기도 했지만 이번 경험을 통해 A code에서 시간 초과가 발생해도 A + B 코드가 시간 초과 발생하는 것은 아니라는 사실을 알았습니다.


- DP
    - 1부터 e까지의 약수의 개수를 구한다.
        - 약수의 개수는 DP를 적용하여 구한다.
        - n(1~e)의 배수들에 cnt 1추가 e 이하까지
    - e에서 1까지 확인하며 약수의 개수가 최댓값을 가지는 index를 기억한다.
    - start의 index 에서의 기억한 index값을 return한다.

## 사용한 모듈
`math`

## 추가 정보
- 시간: 2 hour 이하
- 힌트: 
'''


def solution(e, starts):
    # 1부터 e까지의 모든 수의 약수 개수를 저장할 리스트 (초기값은 모두 0)
    division_cnt = [0] * (e + 1)

    # 각 수의 약수 개수를 계산하는 과정
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            division_cnt[j] += 1  # i는 j의 약수이므로 division_cnt[j] 증가

    # 최대 약수 개수를 가지는 숫자 저장을 위한 리스트 초기화 (마지막 값부터 시작)
    max_idx = [0] * (e + 1)
    max_idx[e] = e
    max_val = division_cnt[e]  # 시작에서 최대 약수 개수 (마지막 값)

    # 역순으로 최대 약수 개수, index 정보 업데이트
    for k in range(e - 1, 0, -1):
        if max_val > division_cnt[k]:
            max_idx[k] = max_idx[k + 1]  # 이전 인덱스의 값 유지 (같거나 더 큰 값)
        else:
            max_idx[k] = k  # 현재 값이 index 갱신
            max_val = division_cnt[k]  # 최대 약수 개수 갱신

    # starts 리스트에 있는 수들의 최대 약수 개수를 가진 수의 인덱스 반환
    return [max_idx[s] for s in starts]

# import math

# def get_divisor_count(num):
#   """
#   주어진 양의 정수 num의 약수 개수를 반환합니다.

#   Args:
#       num: 약수 개수를 구하고자 하는 양의 정수입니다.

#   Returns:
#       num의 약수 개수입니다.
#   """

#   cnt = 0
#   for i in range(1, int(math.sqrt(num)) + 1):  # 1부터 num의 제곱근까지 반복
#     if num % i == 0:  # i가 num의 약수라면
#       if num // i == i:  # i가 num의 제곱근이라면 (완제곱)
#         cnt += 1  # 약수는 1개만 있으므로 cnt 1 증가
#       else:
#         cnt += 2  # i와 num // i 모두 약수이므로 cnt 2 증가
#   return cnt

