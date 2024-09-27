from collections import defaultdict


def solution(n, lighthouse):
    lh_dict = defaultdict(list)
    for a, b in lighthouse:
        lh_dict[a].append(b)
        lh_dict[b].append(a)

    # print(lh_dict)
    stack = [(1, False)]  # (node, is_returning). 1번을 시작값으로 설정
    parent = [-1] * (n + 1)  # 부모 노드 저장
    visited = [False] * (n + 1)
    dp = [[0, 0] for _ in range(n + 1)]  # dp[node] = [min_on, min_off]

    while stack:
        node, is_returning = stack.pop()

        if not is_returning:  # 처음 방문하는 경우
            visited[node] = True
            stack.append((node, True))  # 방문 여부를 True로 하여 스택에 새로 삽입
            for n in lh_dict[node]:
                if not visited[n]:  # 방문한 적이 없는 자식 노드를 스택에 삽입
                    parent[n] = node  # 현 노드를 부모 노드로 설정 (node: 현 노드, n: 자식 노드)
                    stack.append((n, False))  # 자식 노드 스택에 삽입

        else:  # 처음 방문 후, 되돌아 온 경우
            on, off = 1, 0
            for n in lh_dict[node]:  # n: 자식 노드, node: 현 노드
                if n != parent[node]:  # 연결된 노드 중, 현 노드의 부모인 경우 제외. 자식 노드인 경우만 확인
                    on += min(dp[n][0], dp[n][1])  # 현 노드가 켜진 상태. 자식 노드가 켜지거나 꺼진 경우 중 최솟값을 더함
                    off += dp[n][0]  # 현 노드가 꺼진 경우. 자식 노드가 무조건 켜진 상태여야 함.
            dp[node][0], dp[node][1] = on, off  # 0번 인덱스 : on, 1번 인덱스 : off

    return min(dp[1][0], dp[1][1])

print(solution(	8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print("-----")
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
