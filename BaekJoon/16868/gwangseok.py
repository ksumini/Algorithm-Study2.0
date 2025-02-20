import math
import sys
input = sys.stdin.readline


def init(left, right, node):
    if left == right:
        # left와 right가 같으면 1개 중 최소의 값을 구하는 것이다.
        tree[node] = arrs[left]
    else:
        # 중간 값을 구한다.
        mid = (left + right) // 2
        # 왼쪽 자손 중 가장 작은 값
        left_min = init(left, mid, node * 2)
        # 오른쪽 자손 중 가장 작은 값
        right_min = init(mid+1, right, node * 2 + 1)
        # 둘 중 더 작은 값을 해당 node에 저장한다.
        tree[node] = min(left_min, right_min)
    
    return tree[node]


def query(find_left, find_right, node, node_left, node_right):
    if find_left > node_right or find_right < node_left:
        # 구하고자 하는 구간이 탐색하려는 구간을 벗어났을 때
        # 반환 값이 무시되도록 아주 큰 값을 준다.
        return float('inf')

    if find_left <= node_left and node_right <= find_right:
        # 탐색하려는 구간이 구하고자 하는 구간을 완전히 포함할 때
        # 해당 node 값을 반환한다.
        return tree[node]

    # 이 외의 경우
    # 양쪽 구간을 나눠서 푼 뒤 결과를 반환한다.
    mid = (node_left + node_right) // 2
    left_min = query(find_left, find_right, node * 2, node_left, mid)
    right_min = query(find_left, find_right, node * 2 + 1, mid + 1, node_right)
    return min(left_min, right_min)


# 배열의 크기와 원소를 입력 받는다.
n, m = map(int, input().split())
arrs = [int(input()) for _ in range(n)]


# 알맞은 크기의 segment tree의 배열을 할당한다.
size = 4 * n
tree = [None] * size

# 초기화를 한다. (구간 시작, 구간 끝, 저장할 node)
init(0, n-1, 1)

queries = [list(map(int, input().split())) for _ in range(m)]

# 질의를 한다. (찾고자 하는 구간, 시작 노드, 탐색 구간)
for query_start, query_end in queries:
    print(query(query_start, query_end, 1, 1, n))
