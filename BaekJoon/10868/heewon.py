import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

range_ = [tuple(map(int, input().split())) for _ in range(m)]

# 세그먼트 트리 초기화
tree = [float('inf')] * (4 * n)

# 세그먼트 트리 빌드
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        build(left_child, start, mid)
        build(right_child, mid + 1, end)
        tree[node] = min(tree[left_child], tree[right_child])

# 구간 최소값 쿼리
def query(node, start, end, left, right):
    if right < start or end < left:  # 범위를 벗어난 경우
        return float('inf')
    if left <= start and end <= right:  # 완전히 포함된 경우
        return tree[node]
    
    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2
    left_min = query(left_child, start, mid, left, right)
    right_min = query(right_child, mid + 1, end, left, right)
    return min(left_min, right_min)

# 트리 생성
build(0, 0, n - 1)

# 쿼리 처리
for a, b in range_:
    print(query(0, 0, n - 1, a - 1, b - 1))