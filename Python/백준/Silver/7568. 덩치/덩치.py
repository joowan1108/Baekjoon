import sys
input=sys.stdin.readline

N=int(input().strip())

sizes=[]
for _ in range(N):
    sizes.append(list(map(int, input().split())))

rank=1
for i in sizes:
    count=0
    for j in sizes:
        if(i[0]<j[0] and i[1]<j[1]):
            count+=1
    print(rank+count, end=' ')
        
