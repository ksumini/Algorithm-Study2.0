"""
<문제>
1~n까지 서로 다른 번호가 매겨진 등대 n개가 존재한다.
뱃길은 n-1개 존재하며, 어느 등대에서 출발해도 다른 모든 등대까지 이동할 수 있다.
한 뱃길의 양쪽 끝 등대 중 적어도 하나는 켜져있도록 등대를 켜두어야 한다.

<제한 사항>
- 2 ≤ n ≤ 100,000
- lighthouse의 길이 = n – 1
- lighthouse 배열의 각 행 [a, b]는 a번 등대와 b번 등대가 뱃길로 연결되어 있다는 의미
- 1 ≤ a ≠ b ≤ n
- 모든 등대는 서로 다른 등대로 이동할 수 있는 뱃길이 존재하도록 입력이 주어진다.

<풀이 시간>
2시간 이상

<풀이>
처음에는 리프노드를 찾고 모든 리프노드의 부모 노드를 켜주면 되는 그리디 문제라고 생각해 그리디로 풀이를 접근했다.
예제로 다 통과하고, 다른 반례를 찾지 못해서 맞왜틀만 하다가, 결국 아이디어를 참고해서 DP로 풀이해야함을 알았다.
1. DP 테이블 정의
- dp[node][0]: node가 꺼져있을 때, node를 루트로 하는 서브트리에서 최소로 불이 켜진 개수
- dp[node][1]: node가 켜져있을 때, node를 루트로 하는 서브트리에서 최소로 불이 켜진 개수

2. 초기값 정의
dp[node][0] = 0
dp[node][1] = 1

# 3. 점화식
dp[node][0] += dp[child][1]
- node가 꺼져있기 때문에 child가 켜져있어야 함
dp[node][1] += min(dp[child][0], dp[child][1])
- node가 켜져있을 때, child가 켜지거나 꺼지거나 더 작은 걸 선택

<시간 복잡도>
1. 그래프 정의: O(n)
2. DFS 순회: O(n)
3. DP 테이블 업데이트: O(n)
-> O(n) + O(n) + O(n) = O(n)
"""


def dfs(node, parent, graph, dp):
    dp[node][0] = 0 # 해당 노드에 불이 꺼져있을 때, node를 루트로 하는 서브트리에서 최소로 불이 켜진 개수
    dp[node][1] = 1 # 해당 노드에 불이 켜져있을 때, node를 루트로 하는 서브트리에서 최소로 불이 켜진 개수

    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node, graph, dp)

        dp[node][0] += dp[child][1] # 자식 노드들이 켜져있어야 하므로
        dp[node][1] += min(dp[child][0], dp[child][1]) # 자식 노드들이 꺼져있거나 켜져있을 수 있으므로


# def dfs_stack(start_node, graph, dp):
#     stack = [(start_node, -1)]
#     order = []
#
#     while stack:
#         node, parent = stack.pop()
#         order.append((node, parent))
#         for child in graph[node]:
#             if child != parent:
#                 stack.append((child, node))
#
#     # 역순으로 순회하며 DP 업데이트
#     while order:
#         node, parent = order.pop()
#         dp[node][0], dp[node][1] = 0, 1
#         for child in graph[node]:
#             if child != parent:
#                 dp[node][0] += dp[child][1]
#                 dp[node][1] += min(dp[child][0], dp[child][1])


def solution(n: int, lighthouse: list) -> int:
    tree = [[] for _ in range(n+1)]

    for a, b in lighthouse:
        tree[a].append(b)
        tree[b].append(a)

    # DP 테이블 정의
    dp = [[0, 0] for _ in range(n+1)]

    # dfs_stack(1, tree, dp)
    dfs(1, -1, tree, dp)

    return min(dp[1])