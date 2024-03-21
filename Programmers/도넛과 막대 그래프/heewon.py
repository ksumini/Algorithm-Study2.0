from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]

    # node in, out 선언
    node_in = defaultdict(list)
    node_out = defaultdict(list)

    # node 집합 생성
    nodes = set()
    
    # edges로 node in, out
    for a, b in edges:
        node_out[a].append(b)
        node_in[b].append(a)
        nodes.add(a)
        nodes.add(b)
    
    # 모양 갯수
    shape_cnt = 0
    
    # 모든 노드를 확인
    for node in nodes:
        # 생성한 정점의 번호 와 모양 갯수 찾기
        if not node_in[node] and len(node_out[node]) >= 2:
            answer[0] = node
            shape_cnt = len(node_out[node])
        # 막대 모양 그래프 갯수 찾기
        elif len(node_out[node]) == 0: answer[2] += 1
        # 8자 모양 그래프 갯수 찾기
        elif len(node_out[node]) + len(node_in[node]) >= 4: answer[3] += 1
    
    # 도넛 모양 그래프 갯수 찾기
    answer[1] = shape_cnt - answer[2] - answer[3]
    
    return answer

# 지수님 방법 보고 시도 -시간 복잡도 감소

from collections import defaultdict, deque

def validate(root, st_dict, en_dict):
    nodes = {root}
    queue = deque([root])
    # 노드의 수 / 간선의 수
    node_cnt = 0
    edge_cnt = 0

    # BFS로 그래프에 포함된 정점 찾기(DFS 재귀 활용시 최대 재귀 깊이 에러)
    while queue:
        cur = queue.popleft()
        node_cnt += 1
        edge_cnt += len(st_dict[cur])

        for v in st_dict[cur]:
            if v not in nodes:
                nodes.add(v)
                queue.append(v)

    # 도넛의 조건
    if node_cnt == edge_cnt:
        return 1
    # 8자의 조건
    elif node_cnt + 1 == edge_cnt:
        return 3
    # 나머지 경우 = 막대 경우
    else:
        return 2

def solution(edges):
    # 생성된 정점 찾기
    st_dict = defaultdict(list)
    en_dict = defaultdict(int)

    for st, en in edges:
        st_dict[st].append(en)
        en_dict[en] += 1

    for st, lst in st_dict.items():
        if len(lst) >= 2 and st not in en_dict:
            root = st

    answer = [root, 0, 0, 0]  # [정점, 도넛, 막대, 8자]

    # 생성된 정점에서 뻗은 간선 제거
    for en in st_dict[root]:
        en_dict[en] -= 1

    # 그래프 탐색
    for other_root in st_dict[root]:
        idx = validate(other_root, st_dict, en_dict)
        answer[idx] += 1

    return answer