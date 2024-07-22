def solution(cap, n, deliveries, pickups):
    answer = 0
    d_amount, p_amount = 0, 0

    for i in range(n-1, -1, -1):
        d_amount += deliveries[i]
        p_amount += pickups[i]

        while d_amount > 0 or p_amount > 0:
            d_amount -= cap
            p_amount -= cap
            answer += (i + 1) * 2

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))