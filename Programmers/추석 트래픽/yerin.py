import heapq

def get_start_end_time(info):
    _, end_time, spent_time = info.split()
    hours, minutes, seconds = map(float, end_time.split(':'))
    spent_time = float(spent_time[:-1])

    end_milliseconds = int(hours * 3600 * 1000 + minutes * 60 * 1000 + seconds * 1000)
    start_milliseconds = end_milliseconds - int(spent_time * 1000) + 1

    return start_milliseconds, end_milliseconds

def solution(lines):
    times = []
    for line in lines:
        start_time, end_time = get_start_end_time(line)
        times.append((start_time, 1))
        times.append((end_time + 1000, -1))

    times.sort()

    count = 0
    max_count = 0

    for _, val in times:
        count += val
        max_count = max(max_count, count)

    return max_count
