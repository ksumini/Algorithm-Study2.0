import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict


def init_tree(edges):
    tree = defaultdict(list)
    
    for n1, n2 in edges:
        tree[n1].append(n2)
        tree[n2].append(n1)
    
    return tree


def dfs(tree, node, checked, edges):
    for neighbor in tree[node]:
        if neighbor not in checked:
            checked.add(neighbor)
            edges.append((node, neighbor))
            dfs(tree, neighbor, checked, edges)


def seperate_group(tree, nodes):
    trees = []
    checked = set()
    
    for node in nodes:
        if node not in checked:
            checked.add(node)
            edges = []
            dfs(tree, node, checked, edges)
            if edges:
                trees.append(init_tree(edges))
            else:
                trees.append({node: []})
    
    return trees
    

def check_both(n1, n2):
    if (n1 % 2 + n2 % 2) % 2 == 0:
        return 1
    else:
        return 0

    
def solution(nodes, edges):
    tree = init_tree(edges)  # 전체적으로 tree를 계산
    trees = seperate_group(tree, nodes) # 서로 독립된 tree끼리 분리해서 홀짝/역홀짝인지 판별
    
    answer = [0, 0]
    for cur_tree in trees:
        root_case = {} # 1 if num of child is 홀짝
        not_root_case = {} # 1 if num of childe is 홀짝 
        
        for node in cur_tree.keys():
            # node가 root 일 때
            root_case[node] = check_both(node, len(cur_tree[node])) # 홀짝 트리면 1 아니면 0
            # node가 root가 아닐 때, 부모 노드를 제외한 child 수 계산
            not_root_case[node] = check_both(node, len(cur_tree[node]) - 1)
        
        total_child = sum(not_root_case.values())
        for node in cur_tree.keys():
            total = root_case[node] + total_child - not_root_case[node]
            if total == len(cur_tree):
                # 모두 홀짝 트리
                answer[0] += 1
            elif total == 0:
                # 모두 역홀짝 트리
                answer[1] += 1
            else:
                continue
    
    return answer
