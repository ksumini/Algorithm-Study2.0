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