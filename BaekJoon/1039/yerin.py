from collections import deque

n, k = map(int, input().split())
n = str(n)
length = len(n)

queue = deque()
queue.append((n, 0))

visited = [set() for _ in range(k + 1)]
visited[0].add(n)

max_value = -1

while queue:
    current, depth = queue.popleft()

    if depth == k:
        max_value = max(max_value, int(current))
        continue

    for i in range(length):
        for j in range(i + 1, length):
            swapped = list(current)
            swapped[i], swapped[j] = swapped[j], swapped[i]

            if swapped[0] == '0':
                continue

            next_num = ''.join(swapped)
            if next_num not in visited[depth + 1]:
                visited[depth + 1].add(next_num)
                queue.append((next_num, depth + 1))

print(max_value)
