from sys import stdin

text = stdin.readline().strip()
bomb = stdin.readline().strip()
bomb_len = len(bomb)
stack = []


for char in text:
    stack.append(char)
    
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]  



result = ''.join(stack) 
result = result if result else "FRULA"
print(result) 