from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = defaultdict(int)

answer = []

for _ in range(m):
  _, *seq = list(map(int, input().split()))
  for i in range(len(seq)-1):
      graph[seq[i]].append(seq[i+1])
      indegree[seq[i+1]] += 1

q = deque([i for i in range(1, n+1) if indegree[i]==0])

while q:
    singer = q.popleft()
    
    q.append(singer)

    for next_ in graph[singer]:
        indegree[next_] -= 1
        if indegree[next_] == 0:
            q.append(singer)

if n == len(answer):
    print(*i, sep='\n')
else:
    print(0)