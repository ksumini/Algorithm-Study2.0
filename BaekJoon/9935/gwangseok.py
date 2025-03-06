import sys
input = sys.stdin.readline


arr = input().strip()
target = input().strip()

stack = []

for c in arr: # O(n)
    stack.append(c)
    cur_idx = len(target)-1
    tmp_stack = []

    while stack and cur_idx >= 0: # O(m)
        cur_c = stack.pop()
        tmp_stack.append(cur_c)
        if cur_c == target[cur_idx]:
            cur_idx -= 1
        else:
            break
    
    if cur_idx != -1:
        while tmp_stack:
            stack.append(tmp_stack.pop())


if stack:
    print(''.join(stack))
else:
    print('FRULA')
