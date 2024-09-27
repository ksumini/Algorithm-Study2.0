from collections import defaultdict


def make_dict(lighthouse):
    graph = defaultdict(set)
    for node1, node2 in lighthouse:
        graph[node1].add(node2)
        graph[node2].add(node1)
        
    return graph


def cal_light(graph):
    is_light = [0] * (len(graph) + 1)
        
    while graph:
        # leaf node를 구한다.
        leaf_nodes = [idx for idx in graph.keys() if len(graph[idx]) == 1]
        
        light_nodes = [] # leaf node의 이웃 node가 저장된다.
        for leaf_node in leaf_nodes:
            for light_node in graph[leaf_node]:
                # 1. greedy하게 leaf node와 이웃한 node를 킨다.
                is_light[light_node] = 1
                light_nodes.append(light_node)
                # 2. leaf_node를 삭제한다.
                graph[light_node].discard(leaf_node)            
            del graph[leaf_node]
            
        for light_node in light_nodes:
            for node in graph[light_node]:
                # 2. 켜진 node를 삭제 한다.
                graph[node].discard(light_node)
                if len(graph[node]) == 0:
                    # 3. 아무것도 연결되지 않은 node는 키지 않는다. 
                    # -> 삭제한다.
                    del graph[node]
                    
            del graph[light_node]
    
    return sum(is_light)


def solution(n, lighthouse):    
    # node number: 이웃 node
    graph = make_dict(lighthouse)
    # 힌트: leaf node를 키면 이득이 없다. 
    # 1. greedy하게 leaf node와 이웃한 node를 킨다.
    # 2. leaf node와 켜진 node를 삭제 한다.
    # 3. 아무것도 연결되지 않은 node는 키지 않는다. -> 삭제한다.
    # -> 켜진 nodes만 연결되어 있기 때문에 2번에 의해 연결된 node가 없다.
    # 4. graph node가 없어질 때까지 2~3 반복한다.
    return cal_light(graph)
