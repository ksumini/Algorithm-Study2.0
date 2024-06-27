'''
<문제 내용>
최소한의 객실
다음 이용 가능 시간 = 이전 퇴실 시간 + 10분

book_time : [입실 시각, 퇴실 시각]
시간 : HH:MM (24시간 표기법 - 00:00 ~ 23:59)

퇴실 시각이 다른 예약 입실 시각 이전.
입실 시각이 다른 예약 퇴실 시각 이후.

<반환>
필요한 최소 객실 수
'''

def solution(book_time: list):
    # 입실 시간이 빠른 순서로 정렬
    book_time.sort()
    # key: 방번호, value: 다음 이용가능 시간(이전 예약 퇴실 시간 + 10분)
    room = {}
    new_room = 0

    for check_in, check_out in book_time:
        check_in_hour, check_in_min = map(int, check_in.split(":"))
        check_out_hour, check_out_min = map(int, check_out.split(":"))
        # 분 단위로 맞춤
        check_in_time = check_in_hour * 60 + check_in_min
        next_available_time = check_out_hour * 60 + check_out_min + 10

        # 첫 예약일 때
        if len(room.keys()) == 0:
            room[new_room] = next_available_time
            new_room += 1
            continue
        # 현재 쓰고 있는 방들 value 기준으로 정렬(오름차순). num : 방 번호, earlier_time : 가장 빠른 퇴실 시간
        num, earlier_time = sorted(room.items(), key=lambda x:x[1])[0]
        # 기존 방을 이어 쓰는 경우 (체크인 전, 이전 타임이 퇴실 가능한 경우)
        if earlier_time <= check_in_time:
            room[num] = next_available_time
        # 새로운 방 배정
        else:
            room[new_room] = next_available_time
            new_room += 1 # 새로운 방 번호 업데이트

    return len(room.keys())
