'''
n : 퍼즐 개수
diff: 난이도
time_cur: 현재 퍼즐 소요 시간
time_prev: 이전 퍼즐 소요 시간
숙련도: level

return 숙련도 최솟값
난이도, 소요 시간, 숙련도 > 0

<풀이>
가장 어려운 난이도를 기준으로 이분탐색
left > right일 때 반복문 탈출해서 수 출력
'''


def calculate_total_time(diffs, times, level):
    time = 0

    for i, diff in enumerate(diffs):
        if diff <= level:
            time += times[i]
        else:
            prev_time = times[i - 1] if i > 0 else 0
            time += (times[i] + prev_time) * (diff - level) + times[i]

    return time


def binary_search(times, diffs, limit):
    left = 1
    right = max(diffs)

    while left <= right:
        level = (left + right) // 2
        time = calculate_total_time(diffs, times, level)

        if time > limit:
            left = level + 1
        else:
            right = level - 1

    return left


def solution(diffs, times, limit):
    return binary_search(times, diffs, limit)


if __name__ == '__main__':
    # print(solution([1, 5, 3], [2, 4, 7], 30))
    print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))

