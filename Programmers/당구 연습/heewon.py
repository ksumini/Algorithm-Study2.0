from typing import List

def solution(m:int, n:int, startX:int, startY:int, balls:List)->List:
    
    def reflect_point()->List:
        reflect_point = []
        reflect_point.append([-startX, startY])         # y축 대칭
        reflect_point.append([startX, -startY])         # x축 대칭
        reflect_point.append([2*m - startX, startY])    # x = m 대칭
        reflect_point.append([startX, 2*n - startY])    # y = n 대칭
        return reflect_point
    
    answer = []
    points = reflect_point()
    
    for x, y in balls:
        distance = float('INF')
        for rx, ry in points:
            if ry == y and (rx < x < startX or startX < x < rx):    # 쿠션 전에 부딪히는 경우 1 / x축 평행
                continue
            if rx == x and (ry < y < startY or startY < y < ry):    # 쿠션 전에 부딪히는 경우 2 / y축 평행
                continue
            distance = min(distance, pow(x-rx, 2) + pow(y-ry, 2))
        answer.append(distance)
        
    return answer