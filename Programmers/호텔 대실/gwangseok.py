# 30분
# 시간 복잡도
# O(N^2 logN)

def change_to_minute(book_time: list) -> list:
    """ 청소 시간까지 고려해서 book_time을 분 단위로 변경한다. """
    
    book_minute = []
    to_minute = lambda x: x[0] * 60 + x[1]  # 분 단위로 변경하는 함수
    
    for t in book_time:
        start = list(map(int, t[0].split(":")))
        end = list(map(int, t[1].split(":")))
        
        start = to_minute(start)
        end = to_minute(end) + 10  # 청소 시간 미리 고려
        
        book_minute.append([start, end])
    
    book_minute.sort()  # Greedy로 하기 위해 청소 시간으로 정렬.
    return book_minute

def solution(book_time):
    book_minute = change_to_minute(book_time) # O(NlogN)
    ends = [book_minute[0][1]]  # 현재 숙소를 사용하고 있는 사람들이 나가는 시간
    answer = 1  # 필요한 방의 개수
    
    for s, e in book_minute[1:]:  # O(N)
        # 현재 시작 시간 s와 끝나는 시간 e를 가져온다.
        idx = 0
        while s >= ends[idx]: # O(N)
            # idx를 하나씩 올리면서 현재 시작 s 보다 일찍 나가는 사람을 계산한다.
            idx += 1
            if idx == len(ends):
                # 모두 나가는 경우
                break
        
        ends = ends[idx:]  # 현재 시간 s가 숙소를 사용할 때 방에 남아 있는 사람들만 남겨둔다.
        ends.append(e)
        answer = max(answer, len(ends))  # 남아 있는 사람의 수를 이전에 필요했던 방의 수보다 많은지 확인한다.
        ends.sort() # O(NlogN)  # ends를 시간 순으로 정렬한다.
        
    return answer
