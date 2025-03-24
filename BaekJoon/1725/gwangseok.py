import sys
input = sys.stdin.readline


N = int(input())

heights = [-1] + [0] * (N + 1)
for idx in range(1, N + 1):
    heights[idx] = int(input())

stack_indices = [0] # 오름차순으로 저장 됨.
answer = 0

for idx in range(1, N + 2):
    new_height = heights[idx]
    while stack_indices and heights[stack_indices[-1]] >= new_height:
        cur_height = heights[stack_indices.pop()]
        answer = max(answer, (idx - stack_indices[-1] - 1) * cur_height)
        # 밑변: idx - stack_indices[-1] - 1, 높이: cur_height

    stack_indices.append(idx)

print(answer)
