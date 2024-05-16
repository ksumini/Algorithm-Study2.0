def solution(m, n, startX, startY, balls):
    
    
    def reflect_point():
        reflect_point = []
        reflect_point.append([-startX, startY])
        reflect_point.append([startX, -startY])
        reflect_point.append([2*m - startX, startY])
        reflect_point.append([startX, 2*n - startY])
        return reflect_point
    
    answer = []
    points = reflect_point()
    
    for x, y in balls:
        distance = float('INF')
        for rx, ry in points:
            if ry == y and (rx < x < startX or startX < x < rx):
                continue
            if rx == x and (ry < y < startY or startY < y < ry):
                continue
            distance = min(distance, pow(x-rx, 2) + pow(y-ry, 2))
        answer.append(distance)
        
    return answer