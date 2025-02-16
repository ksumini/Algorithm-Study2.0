import sys
input = sys.stdin.readline

N = int(input())

awards = []
cum_awards = []
diffs = []  # i번째 대회까지 계속 참가했을 때와 x_i 차이 
first_neg_idx = N

for i in range(N):
    x_i, p_i = map(int, input().split())
    awards.append(p_i)
    if cum_awards:
        cum_awards.append(cum_awards[i-1] + p_i)
        diff = x_i - cum_awards[i -1]
    else:
        cum_awards.append(p_i)
        diff = x_i
    diffs.append(diff)

    if first_neg_idx is None and diff < 0:
        first_neg_idx = i

# 첫 번째로 참가못하게 되는 대회는 first_neg_idx 번째 대회이다. 
if first_neg_idx <= N-1:
    # first_neg_idx가 N-1보다 작으면 참가못하는 대회가 없거나,
    # 마지막 대회를 포기한다.
    print("Kkeo-eok")
else:
    # first_neg_idx가 N-1보다 작으면,
    # 해당 대회를 포함해서 앞쪽에 있는 대회들 중 하나를 포기해야 한다.
    # 본인 또는 greedy하게 상금을 가장 많이 주는 대회를 포기한다.
    
    # 본인을 포기 했을 때 (x_i가 작은 경우를 고려)
    cancel_p = awards[first_neg_idx]
    min_diff_p = sorted(diffs[first_neg_idx+1:])[0]
    if -min_diff_p <= cancel_p:
        print("Kkeo-eok")
    else:
        # 본인보다 앞에 있는 대회 중 하나를 포기했을 때
        cancel_p = sorted(awards[:first_neg_idx+1])[-1]

        # max_p를 가지는 대회를 포기했을 때, 나중 대회를 모두 참가할 수 있는지 본다.
        # 이후 대회에서의 diffs 중 가장 작은 값의 절대값이 max_p 이하이면 참가할 수 있다.
        # 그렇지 않으면 참가할 수 없다.
        min_diff_p = sorted(diffs[first_neg_idx:])[0]

        if -min_diff_p <= cancel_p:
            print("Kkeo-eok")
        else:
            print("Zzz")
