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

def store_max_divisors(divisors, n):
    '''
    :param divisors: 인덱스에 해당하는 정수의 약수의 개수가 저장되어 있는 리스트
    :param n: e
    :return: 특정 인덱스와 n 사이에서 가장 많은 약수를 가지고, 가장 작은 값을 값으로 저장한 리스트
    '''
    max_divisors_from_start = [0] * (n + 1)
    max_num = n # 뒤에서부터 탐색하므로 e로 설정
    for i in range(n, 0, -1): # n부터 1까지 탐색
        if divisors[i] >= divisors[max_num]:
            max_num = i
        max_divisors_from_start[i] = max_num
    return max_divisors_from_start

def solution(e, starts):
    divisors = count_divisors(e)
    max_divisors_from_start = store_max_divisors(divisors, e)
    answer = [max_divisors_from_start[start] for start in starts]

    return answer

print(solution(8, [1, 3, 7]))
