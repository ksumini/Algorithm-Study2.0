from datetime import datetime, timedelta

def solution(lines):
    logs = []

    for line in lines:
        date, time, duration = line.split()
        end_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S.%f")
        duration = float(duration.replace("s", ""))
        start_time = end_time - timedelta(seconds=duration - 0.001)  # 처리 시간 포함
        logs.append((start_time, end_time))

    max_requests = 0

    for start, end in logs:
        end_margin = end + timedelta(seconds=1)  # 요청이 끝나고 1초안까지 범위
        count = 0
        for _start, _end in logs:
            if _start < end_margin and _end >= end:  # 구간안에 시작과 끝이 들어 있는 경우
                count += 1
        max_requests = max(max_requests, count)

    return max_requests
