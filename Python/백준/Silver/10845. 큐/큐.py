import sys
input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    cmd = input().strip().split()
    if(len(cmd)==2):
        q.append(int(cmd[1]))
    elif(len(cmd)==1):
        if(cmd[0]=='front'):
            if len(q)==0:
                print(-1)
            else:
                print(q[0])
        elif(cmd[0]=='back'):
            if len(q)==0:
                print(-1)
            else:
                print(q[-1])
        elif(cmd[0]=='size'):
            print(len(q))
        elif(cmd[0]=='empty'):
            if len(q)==0:
                print(1)
            else:
                print(0)
        else:
            if len(q)==0:
                print(-1)
            else:
                print(q[0])
                q = q[1:]
        
    
                    
                    
        
    