from collections import deque

string = deque(input().strip())
bomb = input().strip()
bomb_len = len(bomb)
stack = []

while string:
    stack.append(string.popleft())
    while ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

print(''.join(stack)) if stack else print('FRULA')