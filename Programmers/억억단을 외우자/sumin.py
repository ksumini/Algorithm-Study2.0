"""
<문제>
1억 x 1억 크기의 행렬
s보다 크거나 같고 e보다 작거나 같은 수 중에서 억억단에서 가장 많이 등장한 수를 답해야 한다.
만약 가장 많이 등장한 수가 여러 개라면 그 중 가장 작은 수를 답해야 한다.

<제한 사항>
- 1 ≤ e ≤ 5,000,000
- 1 ≤ starts의 길이 ≤ min {e,100,000}
- 1 ≤ starts의 원소 ≤ e
- starts에는 중복되는 원소가 존재하지 않는다.

<풀이 시간>
2시간 이상

<풀이>
starts의 원소는 최대 100,000 -> 최대 O(NlogN)으로 해결해야 한다.
e의 크기는 최대 5,000,000 -> O(NlogN)으로도 해결이 안된다.
왜 O(eloge)는 최악의 경우 약 111,267,483이기 때문에 실행시간이 5초(1억번 연산)가 넘어갈 수 밖에 없음

s부터 e까지 등장하는 원소의 개수는 약수의 개수라는 것은 쉽게 파악할 수 있음
중요한 것은, 위의 내용처럼 e의 제한이 매우 크기 때문에 약수의 개수를 구할 때 시간복잡도를 고려해야 한다는 점
일반적으로 어떤 수 num에 대해 약수를 단순 for문으로 구하게 되면 O(N)이 걸리고, s~e 범위의 모든 수에 대해 매번 약수의 개수를 구하면 최악의 경우 O(N^2)이 된다.
근데 여기에, 1,000,000개의 원소에 대해 모두 확인한다면 당연히 시간초과가 날 수 밖에 없음

1. 따라서, 한번에 1~e까지 모든 수에 대한 약수의 개수를 한 번에 구해야 함
-> 해당 부분은 get_divisors 함수처럼 배수의 성질을 이용해 최적화해서 구할 수 있음 -> O(e**0.5 * log(e))
    - 약수는 기본적으로, 항상 짝을 이루고 있기 때문에 제곱근까지만 확인해서 약수의 개수를 구할 수 있음
    - i의 제곱근 i * i는 약수로 자기 자신을 포함
    - i와 j/i는 약수가 되므로 2를 카운트

2. 가장 많이 등장한 수 찾기 (누적 빈도 배열 생성)
- 특정 구간 내에서 가장 많이 등장한 수를 찾기 위해 역순으로 탐색
"""


def get_divisors(num: int) -> list:
    """
    :param num: 문제에서 주어진 e
    :return: 1이상 num 이하의 모든 수들에 대한 약수의 개수 배열
    """
    divisors = [0] * (num + 1)
    for i in range(1, int(num ** 0.5) + 1):
        # i의 제곱인 i*i는 약수로 자기 자신을 포함(제곱수의 경우, 약수의 개수가 홀수)
        divisors[i * i] += 1
        # i와 j // i는 약수가 되므로 2씩 증가
        for j in range(i * (i + 1), num + 1, i):
            divisors[j] += 2

    return divisors


def solution(e: int, starts: list) -> list:
    # 1. 약수의 개수 계산
    divisors = get_divisors(e)

    # 2. 특정 구간 내에서 가장 많이 등장한 수 찾기
    freq = [0] * (e + 1)
    current_max = 0 # 현재까지 발견된 최대 약수 개수
    current_number = 0 # 현재까지 발견된 최대 약수 개수를 가진 숫자

    for i in range(e, 0, -1):
        # 현재 숫자의 약수 개수가 더 많거나, 약수개수가 같은 경우 더 작은 숫자 선택
        if divisors[i] > current_max or (divisors[i] == current_max and i < current_number):
            current_max = divisors[i]
            current_number = i
        freq[i] = current_number

    answer = []
    for s in starts:
        answer.append(freq[s])

    return answer

