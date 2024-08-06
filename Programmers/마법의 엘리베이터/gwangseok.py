# O(logN)

def down_floor(answer, floor, storey):
    answer += floor
    storey //= 10
    
    return answer, storey


def up_floor(answer, floor, storey):
    answer += (10 - floor)
    storey //= 10
    storey += 1
    
    return answer, storey

def solution(storey):
    # 5 -> 5층 아래로
    # 55 -> 5층 위로, 40층 위로, 100층 아래로
    # 555 -> 5층 위로, 40층 위로, 40층 위로, 1000층 아래로 -> 차이나기 시작
    answer = 0
    while storey:
        floor = storey % 10
        if floor < 5:
            answer, storey = down_floor(answer, floor, storey)
        elif floor > 5:
            answer, storey = up_floor(answer, floor, storey)
        else:
            next_floor = (storey // 10) % 10
            if next_floor < 5:
                answer, storey = down_floor(answer, floor, storey)
            else:
                answer, storey = up_floor(answer, floor, storey)

    return answer
