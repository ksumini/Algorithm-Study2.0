from collections import defaultdict

n, m = map(int, input().split())

a = list(map(int, input().split()))

sum_ = [0]  # 누적합의 나머지

for a_i in a:
    sum_.append((sum_[-1] + a_i)%m) # S_i = S_i-1 + a_i / 누적합의 나머지 값을 구하기

answer = 0

rest_dict = defaultdict(int)    # {누적합의 나머지 : 개수}

for sum_i in sum_:
    rest_dict[sum_i] += 1   # 나머지 개수 구하기

for val in rest_dict.values():
    answer += val * (val-1) // 2    # 조합 nC2

print(answer)