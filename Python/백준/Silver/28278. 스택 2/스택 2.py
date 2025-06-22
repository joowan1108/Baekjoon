import sys

input = sys.stdin.readline

n = int(input())
stack = []
top = -1
for _ in range(n):
    cmd = input().split()
    # 명령어 1
    if len(cmd)>1:
        stack.append(cmd[1])
        top+=1
    else:
        if cmd[0] == '2':
            if stack:
                print(stack.pop())
                top-=1
            else:
                print(-1)
        elif cmd[0] == '3':
            print(top+1)
        elif cmd[0] == '4':
            if top==-1:
                print(1)
            else:
                print(0)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)
