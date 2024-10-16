import sys

input = sys.stdin.readline

m = int(input())

s = set()

for _ in range(m):
    tmp = input().strip()
    command =tmp.split()
    if(len(command)==2):
        command[1]=int(command[1])
        if(command[0]=="add"):
            s.add(command[1])
        elif(command[0]=="check"):
            if command[1] in s:
                print(1)
            else:
                print(0)
        elif(command[0]=="remove"):
            s.discard(command[1])
        elif(command[0]=="toggle"):
            if(command[1] in s):
                s.discard(command[1])
            else:
                s.add(command[1])
    else:
        if(command[0]=='all'):
            s=set([i for i in range(1,21)])
        else:
            s.clear()
        