import sys
input = sys.stdin.readline


def solution(N: str, K: int):
    if len(N) == 1 or (len(N) == 2 and N[1] == '0'):
        return -1
    
    cand = set()
    cand.add(N)
    
    for _ in range(K):  # O(K)
        next_cand = set()
        for cur_n in cand:  # O(7C2)
            cur_n = list(cur_n)
            for i in range(len(N)): # O(7C2)
                for j in range(i+1, len(N)):
                    if i == 0 and cur_n[j] == '0':
                        continue

                    cur_n[i], cur_n[j] = cur_n[j], cur_n[i]
                    next_cand.add(''.join(cur_n))
                    cur_n[i], cur_n[j] = cur_n[j], cur_n[i]
        
        cand = next_cand
    
    return max(cand) # O(7C2)


N, K = input().split()
print(solution(N, int(K)))
