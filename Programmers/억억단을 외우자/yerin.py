'''
1억 * 1억
s <= e
s <= ? <= e, min(가장 많이 등장)

'''

def count_divisors(n): # 약수 개수 구하는 함수
    '''
    :param n: e
    :return: 인덱스에 해당하는 값의 약수의 개수가 담긴 리스트
    '''
    divisors = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisors[j] += 1
    return divisors


def solution(e, starts):
    divisors = count_divisors(e)

    max_num_with_max_divisors = [0] * (e + 1)
    max_cnt = e  # 뒤에서부터 탐색하므로 e로 설정
    # e부터 1까지 탐색
    # i~e 중 가장 많은 약수를 가진 수 중, 가장 작은 값을 i 인덱스의 value로 저장
    for i in range(e, 0, -1):
        if divisors[i] >= divisors[max_cnt]:
            max_cnt = i
        max_num_with_max_divisors[i] = max_cnt

    answer = [max_num_with_max_divisors[start] for start in starts]

    return answer

print(solution(8, [1, 3, 7]))
