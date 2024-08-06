def solution(storey):
    answer = 0
    while storey:
        left_floor = storey % 10
        if left_floor > 5:
            storey += (10 - left_floor)
            answer += (10 - left_floor)
        elif left_floor == 5 and ((storey // 10) % 10 >= 5):
            storey += 5
            answer += 5
        else:
            answer += left_floor

        storey //= 10

    return answer

print(solution(485))

'''
555
(-)
1) 550 -> 5
2) 500 -> 5
3) 0 -> 5

(+)
1) 560 -> 5
2) 600 -> 4
3) 0 -> 6
'''