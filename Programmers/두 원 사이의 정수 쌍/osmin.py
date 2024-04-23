
def circle_inner_dots(r):
    y = r
    r2 = r ** 2
    cnt, on_the_circle = 0, 0
    for x in range(r + 1):
        while x ** 2 + y ** 2 > r2:
            y -= 1
        if x ** 2 + y ** 2 == r2:
            on_the_circle += 1
        cnt += y
    return cnt * 4 + 1, (on_the_circle - 1) * 4

def solution(r1, r2):
    outer_dots, outer_circle_dots = circle_inner_dots(r2)
    inner_dots, inner_circle_dots = circle_inner_dots(r1)    
    return outer_dots - inner_dots + inner_circle_dots

# 원 내부에 포함되는 점 구하기
# 바깥 원 내부에 포함되는 점(원 포함) - 안쪽 원 내부에 포함되는 점(원 포함) + 원 위에 있는 점
# 반지름 백만이기 때문에 일일이 계산하는 방법으론 접근 불가.
# 하나의 사분면에서의 점 개수 * 4
# 점 내부에 포함되는 가장 큰 정사각형의 길이를 구하면 될 듯. 아님.
# 가장 큰 정사각형의 대각선 길이: 2r
# 가장 큰 정사각형의 한 변의 길이: 루트2 * r
# 원점과의 거리 = a^2 + b^2 < r^2여야 원 내부에 존재.
