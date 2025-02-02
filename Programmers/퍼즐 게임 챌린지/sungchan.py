def simulation(diffs, times, level, limit):
    time_prev = 0
    total_time = 0

    for diff, time in zip(diffs, times):
        if total_time > limit:
            break

        if diff <= level:
            total_time += time
        else:
            total_time += (diff - level) * (time + time_prev) + time

        time_prev = time

    return False if total_time > limit else True


def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    success_level = 100_000

    while left <= right:
        mid = (left + right) // 2
        if simulation(diffs, times, mid, limit):
            right = mid - 1
            success_level = min(mid, success_level)
        else:
            left = mid + 1

    return success_level
