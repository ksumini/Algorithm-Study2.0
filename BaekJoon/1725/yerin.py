import sys

input = sys.stdin.readline

n = int(input())
heights = []  # [[높이, 시작 인덱스]]
max_width = 0

for i in range(n):
    h = int(input())
    start = i

    while heights and heights[-1][0] > h:
        prev_h, start = heights.pop()
        max_width = max(max_width, prev_h * (i - start))
    heights.append([h, start])

while heights:
    prev_h, start = heights.pop()
    max_width = max(max_width, prev_h * (n - start))

print(max_width)
