import heapq as hq


def can_next_time(end_time: str, start_time: str) -> int:
    """
    check next book_time (end_time + 10 min <= next start_time)

    Params
        end_time : end time of book time
        start_time : start time of next book time

    Returns
        bool : if can do next time, return 1. else, return 0.

    """
    end_time = end_time.split(':');
    end_time_minute = 60 * int(end_time[0]) + int(end_time[1])
    start_time = start_time.split(':');
    start_time_minute = 60 * int(start_time[0]) + int(start_time[1])

    if end_time_minute + 10 <= start_time_minute:
        return 1
    return 0


def solution(book_time: list) -> int:
    """
    get minimum the number of rooms

    Params
        list book_time : the list of book times
    Returns
        int len(rooms) : the number of rooms
    """
    rooms = []  # save end time
    book_time = sorted(book_time)  # sort book time

    for start, end in book_time:
        # if no room or need to more room
        if len(rooms) == 0 or can_next_time(rooms[0], start) == 0:
            hq.heappush(rooms, end)
        elif can_next_time(rooms[0], start) == 1:  # can do next book time in one room
            hq.heappop(rooms)
            hq.heappush(rooms, end)

    return len(rooms)
