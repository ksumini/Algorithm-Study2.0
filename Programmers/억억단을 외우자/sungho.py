# e이하 임의의 수 s. s에 대해 s보다 크고 e보다 작은 수 중에서 억억단에서 가장 많이 등장한 수
# 가장 많이 등장한 수가 여러 개라면 그 중 가장 작은 수

def get_divisor(v: int) -> int:
    """
    v 의 약수 갯수

    :param v: 상수 v
    :return: v의 약수 갯수
    """
    answer = 0
    for i in range(1, int(v**0.5)+1): # 1 ~ v**0.5 + 1 까지 약수가 존재하는지 확인
        if v%i == 0: # v를 i로 나눌 수 있다면 2개의 약수가 존재함
            answer += 2
    if int(v**0.5) == v**0.5: # 만약 제곱수의 경우(4,9,16 ...) 2개의 약수가 같은 수이므로 1개 제외
        answer -= 1
    return answer



def get_divisor_list(end: int) -> list:
    """
    1 ~ end 까지 수들의 약수 갯수

    :param end: 끝 수
    :return: 1 ~ end 까지 수들의 약수 갯수 list
    """
    divisor_list = [0] * (end + 1)
    for i in range(1, end + 1):
        for j in range(i, end + 1, i):
            divisor_list[j] += 1
    return divisor_list


def get_largest_divisors(starts: list, end: int) -> list:
    """
    start 수보다 뒤에 있는 수 들 중에 가장 약수 갯수가 많은 수. 약수 갯수가 같다면 가장 작은 수

    :param starts: start가 되는 수들 list
    :param end: 범위의 끝 수
    :return: 1 ~ end까지 수들의 뒤에 있는 수 들 중에 가장 약수 갯수가 많은 수. 약수 갯수가 같다면 가장 작은 수
    """
    divisor_list = get_divisor_list(end)

    min_start = min(starts)  # starts : list 에서 가장 작은 수
    result_info = [0] * (end + 1)  # result_info[start] = result

    max_cnt = 0 # start보다 큰 수들 중 가장 큰 약수 갯수
    max_cnt_num = 0 # start 보다 가장 큰 약수 갯수 가진 수 중에 가장 작은 수
    for i in range(end, min_start-1, -1):
        #num_divisor = get_divisor(i) # i의 약수 갯수
        num_divisor = divisor_list[i] # i의 약수 갯수`
        if max_cnt <= num_divisor: # 이전 가장 큰 약수 갯수보다 크거나 같은 경우, 정보들 업데이트
            max_cnt = num_divisor
            max_cnt_num = i
        result_info[i] = max_cnt_num # i가 start일 때 결과값 저장
    return result_info


def solution(end: int, starts: list) -> list:
    """
    start 수보다 뒤에 있는 수 들 중에 가장 약수 갯수가 많은 수. 약수 갯수가 같다면 가장 작은 수

    :param end: 범위의 끝 수
    :param starts: start가 되는 수들 list
    :return: starts list 수들의 뒤에 있는 수 들 중에 가장 약수 갯수가 많은 수. 약수 갯수가 같다면 가장 작은 수
    """
    divisor_list = [0] * (end + 1) # idx 약수 갯수
    for i in range(1, end + 1):
        for j in range(i, end + 1, i):
            divisor_list[j] += 1

    min_start = min(starts)  # starts : list 에서 가장 작은 수

    max_div_list = [0] * (end + 1) # idx 수보다 뒤에 있는 수 들 중에 가장 약수 갯수가 많은 수. 약수 갯수가 같다면 가장 작은 수
    max_div_list[-1] = end
    for i in range(end - 1, min_start - 1, -1):
        if divisor_list[max_div_list[i + 1]] <= divisor_list[i]:
            max_div_list[i] = i
        else:
            max_div_list[i] = max_div_list[i + 1]

    return [max_div_list[s] for s in starts]